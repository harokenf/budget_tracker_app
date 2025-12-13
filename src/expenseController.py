# from src.DatabaseConnection import DatabaseConnection
# from src.models.expense import Expense
# from datetime import date as dt_date
# import logging

# class ExpenseController:
#     def __init__(self):
#       self.db = DatabaseConnection()
      
#     def addExpenses(self, name, date, amount, category, description):
#         insert_param="INSERT into expenses (name, date, amount, category, description ) values(?,?,?,?,?);"
#         self.db.execute(insert_param, (name,date, amount, category, description,))
#         self.db.commit()
#         return True
    
#     def getExpenses(self):
#         query = "SELECT id, name, date, amount, category, description FROM expenses"
#         rows = self.db.fetchall(query)
#         expenses = []
#         for row in rows:
            
#             expense = Expense(row["id"], row["name"], row["date"], row["amount"], row["category"], row["description"])
#             logging.warning(expense.get_name())
#             expenses.append(expense)
#         return expenses

#     def getExpense(self, id):
#        query = "SELECT * FROM expenses WHERE id = ?"
#        row = self.db.fetchone(query, (id,))
#        if row:
#             return Expense(row["id"], row["name"], row["date"], row["amount"], row["category"], row["description"])
#        return None 
    
#     def updateExpense(self, id, name, date, amount, category, description):
#         update_statement = 'UPDATE expenses SET name=?, date=?, amount=?, category=?, description=? WHERE id = ?'
#         self.db.execute(update_statement, (name, date, amount, category, description, id,))
#         self.db.commit()
#         return True
      
#     def deleteExpense(self, id):
#         query = "DELETE FROM expenses WHERE id = ?" 
#         self.db.execute(query, (id,))   
#         self.db.commit()
#         return True
    
# ########## sa ne chengera presque rien ici kenfack ########## 

#     def get_month_total(self, year: int, month: int) -> float:
#         # format YYYY-MM
#         ym = f"{year:04d}-{month:02d}"
#         row = self.db.fetchone(
#             "SELECT COALESCE(SUM(amount), 0) AS total FROM expenses WHERE date LIKE ?",
#             (f"{ym}-%",)
#         )
#         return float(row["total"]) if row else 0.0

#     def get_month_by_category(self, year: int, month: int):
#         ym = f"{year:04d}-{month:02d}"
#         rows = self.db.fetchall(
#             """
#             SELECT category, COALESCE(SUM(amount),0) AS total
#             FROM expenses
#             WHERE date LIKE ?
#             GROUP BY category
#             ORDER BY total DESC
#             """,
#             (f"{ym}-%",)
#         )
#         return [{"name": r["category"], "amount": float(r["total"])} for r in rows]
    

#     def get_reports_stats(self):
#     # total global
#         row_total = self.db.fetchone("SELECT COALESCE(SUM(amount),0) AS total FROM expenses")
#         total_all = float(row_total["total"]) if row_total else 0.0

#     # total mois courant
#         from datetime import date as dt_date
#         today = dt_date.today()
#         ym = f"{today.year:04d}-{today.month:02d}"
#         row_month = self.db.fetchone(
#         "SELECT COALESCE(SUM(amount),0) AS total FROM expenses WHERE date LIKE ?",
#         (f"{ym}-%",)
#     )
#     total_month = float(row_month["total"]) if row_month else 0.0

#     # moyenne mensuelle (sur les mois qui existent)
#     row_avg = self.db.fetchone(
#         """
#         SELECT COALESCE(AVG(month_total),0) AS avg_month
#         FROM (
#             SELECT substr(date,1,7) AS ym, SUM(amount) AS month_total
#             FROM expenses
#             GROUP BY substr(date,1,7)
#         )
#         """
#     )
#     avg_month = float(row_avg["avg_month"]) if row_avg else 0.0

#     return total_month, total_all, avg_month



#     # def get_reports_stats(self):
#     #     # total global
#     #     row_total = self.db.fetchone(
#     #         "SELECT COALESCE(SUM(amount),0) AS total FROM expenses"
#     #     )
#     #     total_all = float(row_total["total"]) if row_total else 0.0

#     #     # total mois courant
#     #     from datetime import date as dt_date
#     #     today = dt_date.today()
#     #     ym = f"{today.year:04d}-{today.month:02d}"

#     #     row_month = self.db.fetchone(
#     #         "SELECT COALESCE(SUM(amount),0) AS total FROM expenses WHERE date LIKE ?",
#     #         (f"{ym}-%",)
#     #     )
#     #     total_month = float(row_month["total"]) if row_month else 0.0

#     #     # moyenne mensuelle (sur les mois qui existent)
#     #     row_avg = self.db.fetchone(
#     #         """
#     #         SELECT COALESCE(AVG(month_total),0) AS avg_month
#     #         FROM (
#     #             SELECT substr(date,1,7) AS ym, SUM(amount) AS month_total
#     #             FROM expenses
#     #             GROUP BY substr(date,1,7)
#     #         )
#     #         """
#     #     )
#     #     avg_month = float(row_avg["avg_month"]) if row_avg else 0.0

#     #     return total_month, total_all, avg_month


import logging
from datetime import date as dt_date

from src.DatabaseConnection import DatabaseConnection
from src.models.expense import Expense


class ExpenseController:
    def __init__(self):
        self.db = DatabaseConnection()

    def addExpenses(self, name, date, amount, category, description):
        insert_param = """
            INSERT INTO expenses (name, date, amount, category, description)
            VALUES (?, ?, ?, ?, ?);
        """
        self.db.execute(insert_param, (name, date, amount, category, description))
        self.db.commit()
        return True

    def getExpenses(self):
        query = "SELECT id, name, date, amount, category, description FROM expenses"
        rows = self.db.fetchall(query)
        expenses = []
        for row in rows:
            expense = Expense(
                row["id"], row["name"], row["date"], row["amount"], row["category"], row["description"]
            )
            logging.warning(expense.get_name())
            expenses.append(expense)
        return expenses

    def getExpense(self, id):
        query = "SELECT * FROM expenses WHERE id = ?"
        row = self.db.fetchone(query, (id,))
        if row:
            return Expense(
                row["id"], row["name"], row["date"], row["amount"], row["category"], row["description"]
            )
        return None

    def updateExpense(self, id, name, date, amount, category, description):
        update_statement = """
            UPDATE expenses
            SET name=?, date=?, amount=?, category=?, description=?
            WHERE id = ?
        """
        self.db.execute(update_statement, (name, date, amount, category, description, id))
        self.db.commit()
        return True

    def deleteExpense(self, id):
        query = "DELETE FROM expenses WHERE id = ?"
        self.db.execute(query, (id,))
        self.db.commit()
        return True

    # ---------- Dashboard helpers ----------

    def get_month_total(self, year: int, month: int) -> float:
        ym = f"{year:04d}-{month:02d}"
        row = self.db.fetchone(
            "SELECT COALESCE(SUM(amount), 0) AS total FROM expenses WHERE date LIKE ?",
            (f"{ym}-%",),
        )
        return float(row["total"]) if row else 0.0

    def get_month_by_category(self, year: int, month: int):
        ym = f"{year:04d}-{month:02d}"
        rows = self.db.fetchall(
            """
            SELECT category, COALESCE(SUM(amount), 0) AS total
            FROM expenses
            WHERE date LIKE ?
            GROUP BY category
            ORDER BY total DESC
            """,
            (f"{ym}-%",),
        )
        return [{"name": r["category"], "amount": float(r["total"])} for r in rows]

    def get_reports_stats(self):
        row_total = self.db.fetchone("SELECT COALESCE(SUM(amount), 0) AS total FROM expenses")
        total_all = float(row_total["total"]) if row_total else 0.0

        today = dt_date.today()
        ym = f"{today.year:04d}-{today.month:02d}"

        row_month = self.db.fetchone(
            "SELECT COALESCE(SUM(amount), 0) AS total FROM expenses WHERE date LIKE ?",
            (f"{ym}-%",),
        )
        total_month = float(row_month["total"]) if row_month else 0.0

        row_avg = self.db.fetchone(
            """
            SELECT COALESCE(AVG(month_total), 0) AS avg_month
            FROM (
                SELECT substr(date, 1, 7) AS ym, SUM(amount) AS month_total
                FROM expenses
                GROUP BY substr(date, 1, 7)
            )
            """
        )
        avg_month = float(row_avg["avg_month"]) if row_avg else 0.0

        return total_month, total_all, avg_month
