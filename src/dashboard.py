class DashboardController :
    def dummyData(self):
        return {
            "totalExpenses" : 625,
            "monthBudget" : 850,
            "remainingBudget" : 200,
            "expenses": [
                {"name":"Kleidung", "amount": 150},
                {"name":"Freizeit", "amount": 270},
                {"name":"Tomate", "amount": 150},
                {"name":"afroshop", "amount": 150}
            ],
            "categoriesExpenses": [
                {"name": "Lebensmittel", "amount": "150", "color":"bg-blue-600", "percentage" : 30},
                {"name": "Transport", "amount": "80", "color":"bg-green-600", "percentage" : 50},
                {"name": "Unterhaltung", "amount": "200", "color":"bg-purple-600", "percentage" : 90}
            ]
        }