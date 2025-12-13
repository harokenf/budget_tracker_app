from src.expenseController import ExpenseController

class ReportsController:
    def __init__(self):
        self.exp = ExpenseController()

    def displaySummaryCards(self):
        total_month, total_all, avg_month = self.exp.get_reports_stats()
        return {
            "displayCards": [
                {"name": "Monatliche Ausgaben", "amount": total_month, "backgroundColor": "from-blue-500 to-blue-600"},
                {"name": "Gesamt-Ausgaben", "amount": total_all, "backgroundColor": "from-purple-500 to-purple-600"},
                {"name": "Durchschnitt/Monat", "amount": avg_month, "backgroundColor": "from-green-500 to-green-600"},
            ],
            "displayButton": [
                {"name": "Export", "color": "border-gray-300 hover:bg-gray-50"},
                {"name": "Analyse", "color": "bg-blue-600 hover:bg-blue-700 text-white"}
            ]
        }
#########kenfack /reports devient basé DB sans toucher aux templates.###########
