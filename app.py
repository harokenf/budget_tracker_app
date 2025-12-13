from flask import Flask, render_template, request, redirect, url_for
from src.dashboard import DashboardController 
from src.reports import ReportsController
from src.categoryController import CategoryController
from src.expenseController import ExpenseController
category_controller = CategoryController()
expense_controller = ExpenseController()

app = Flask(__name__)
expenses = []
budget = 0


@app.route('/')
def home():
    dashboard_data = DashboardController()
    dummy_data = dashboard_data.dummyData(budget, expenses)
    return render_template('dashboard.html', data=dummy_data)


@app.route('/expense', methods=['GET'])
def viewExpense():
    expenses = expense_controller.getExpenses()

    categories = category_controller.getCategories()   
    return render_template('expense.html', expenses=expenses, data=categories)


@app.route('/expense', methods=['POST'])
def createExpense():
    
    
    if request.method == 'POST':
       name = request.form.get("name")
       date = request.form.get("date")
       amount = request.form.get("amount")
       category = request.form.get("category")
       description = request.form.get("description")

       
    expense_controller.addExpenses(name, date, amount, category, description)
    expenses = expense_controller.getExpenses()
    categories = category_controller.getCategories()   
    return render_template('expense.html', expenses=expenses, data=categories)

@app.route('/expense/<id>/delete', methods=['GET'])
def deleteExpense(id):
    expense_controller.deleteExpense(id)
    return redirect(url_for('viewExpense'))

@app.route('/expense/<id>/edit', methods=['GET'])
def editExpense(id):
    edit_expense = expense_controller.getExpense(id)
    categories = category_controller.getCategories()   
    return render_template('edit_expense.html', expense=edit_expense, data=categories)

@app.route('/expense/<id>/edit', methods=['POST'])
def updateExpense(id):

    if request.method == 'POST':
       name = request.form.get("name")
       date = request.form.get("date")
       amount = request.form.get("amount")
       category = request.form.get("category")
       description = request.form.get("description")

    expense_controller.updateExpense(id, name, date, amount, category, description)
    return redirect(url_for('viewExpense'))

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
