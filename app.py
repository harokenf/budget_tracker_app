from flask import Flask, render_template, request, redirect, url_for
from src.dashboard import DashboardController 
from src.reports import ReportsController
from src.categoryController import CategoryController
category_controller = CategoryController()

app = Flask(__name__)
expenses = []
budget = 0


@app.route('/')
def home():
    dashboard_data = DashboardController()
    dummy_data = dashboard_data.dummyData(budget, expenses)
    return render_template('dashboard.html', data=dummy_data)

@app.route('/expense', methods=['GET', 'POST'])
def expense():
    global expenses
    categories = category_controller.getCategories()
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
       print("Expenses:", expenses)
    return render_template('expense.html', expenses=expenses, data=categories)

@app.route('/reports')
def reports():
    report_data = ReportsController()
    card_data = report_data.displaySummaryCards()
    return render_template('reports.html', data=card_data)



@app.route('/settings', methods=['GET', 'POST'])
def settings():
    global budget
    

    if request.method == 'POST':
        monthly_budget = request.form.get('monthly_budget')
        if monthly_budget:
            budget = float(monthly_budget)

    categories = category_controller.getCategories()        
    return render_template('settings.html', budget=budget, data=categories)



@app.route('/settings/category/<category_name>', methods=['GET'])
def viewCategory(category_name):
    category = category_controller.getCategoryByName(category_name)
    if not category:
        return redirect(url_for('settings'))
    return render_template('edit_category.html', category=category )


@app.route('/settings/category/<category_name>', methods=['POST'])
def editCategory(category_name):
    if request.method == 'POST':
       max_amount = request.form.get("max_amount")
       category_controller.updateCategory(category_name, max_amount)
    return redirect(url_for('settings'))
    

if __name__ == '__main__':
    app.run(debug=True)
