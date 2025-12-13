from src.DatabaseConnection import DatabaseConnection
from src.models.expense import Expense
import logging

class ExpenseController:
    def __init__(self):
      self.db = DatabaseConnection()
      
    def addExpenses(self, name, date, amount, category, description):
        insert_param="INSERT into expenses (name, date, amount, category, description ) values(?,?,?,?,?);"
        self.db.execute(insert_param, (name,date, amount, category, description,))
        self.db.commit()
        return True
    
    def getExpenses(self):
        query = "SELECT id, name, date, amount, category, description FROM expenses"
        rows = self.db.fetchall(query)
        expenses = []
        for row in rows:
            
            expense = Expense(row["id"], row["name"], row["date"], row["amount"], row["category"], row["description"])
            logging.warning(expense.get_name())
            expenses.append(expense)
        return expenses

    def getExpense(self, id):
       query = "SELECT * FROM expenses WHERE id = ?"
       row = self.db.fetchone(query, (id,))
       if row:
            return Expense(row["id"], row["name"], row["date"], row["amount"], row["category"], row["description"])
       return None 
    
    def updateExpense(self, id, name, date, amount, category, description):
        update_statement = 'UPDATE expenses SET name=?, date=?, amount=?, category=?, description=? WHERE id = ?'
        self.db.execute(update_statement, (name, date, amount, category, description, id,))
        self.db.commit()
        return True
      
    def deleteExpense(self, id):
        query = "DELETE FROM expenses WHERE id = ?" 
        self.db.execute(query, (id,))   
        self.db.commit()
        return True