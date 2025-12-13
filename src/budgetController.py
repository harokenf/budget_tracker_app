from src.DatabaseConnection import DatabaseConnection

class BudgetController:
    def __init__(self):
        self.db = DatabaseConnection()

    def get_budget(self):
        row = self.db.fetchone("SELECT amount FROM budget ORDER BY id LIMIT 1")
        return float(row["amount"]) if row and row["amount"] is not None else 0.0

    def set_budget(self, amount: float):
        row = self.db.fetchone("SELECT id FROM budget ORDER BY id LIMIT 1")
        if row:
            self.db.execute("UPDATE budget SET amount=? WHERE id=?", (amount, row["id"]))
        else:
            self.db.execute("INSERT INTO budget (amount) VALUES (?)", (amount,))
        self.db.commit()
