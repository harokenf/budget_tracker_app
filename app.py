from flask import Flask, render_template, request, redirect, url_for
from src.dashboard import DashboardController 
from src.reports import ReportsController
from src.category import CategoryController

app = Flask(__name__)
expenses = []
budget = 0
category_controller = CategoryController()

@app.route('/')
def home():
    dashboard_data = DashboardController()
    dummy_data = dashboard_data.dummyData(budget)
    return render_template('dashboard.html', data=dummy_data)

@app.route('/expense', methods=['GET', 'POST'])
def expense():
    if request.method == 'POST':
       name = request.form.get("name")
       date = request.form.get("date")
       amount = request.form.get("amount")
       category = request.form.get("category")
       description = request.form.get("description")

       new_expense = {
           'name': name,
           'date': date,
           'amount': amount,
           'category': category,
           'description': description
       }

       expenses.append(new_expense)
    return render_template('expense.html', expenses=expenses)

@app.route('/reports')
def reports():
    report_data = ReportsController()
    card_data = report_data.displaySummaryCards()
    return render_template('reports.html', data=card_data)



@app.route('/settings', methods=['GET', 'POST'])
def settings():
    global budget
    categories = category_controller.getCategories()

    if request.method == 'POST':
        monthly_budget = request.form.get('monthly_budget')
        if monthly_budget:
            budget = float(monthly_budget)
    return render_template('settings.html', budget=budget, data=categories)



@app.route('/settings/category/<category_name>', methods=['GET', 'POST'])
def editCategory(category_name):

    if request.method == 'POST':
       name = request.form.get("name")
       color = request.form.get("color")
       limit = request.form.get("limit")

       print(f"   search: {category_name}")
       print(f"   new value: name={name}, color={color}, limit={limit}")

       category_controller.updateCategory(category_name, name, color, limit)
       return redirect(url_for('settings'))
    
    category = category_controller.getCategoryByName(category_name)
    if not category:
        return redirect(url_for('settings'))   
    
    return render_template('edit_category.html', category=category )

if __name__ == '__main__':
    app.run(debug=True)
