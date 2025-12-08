class CategoryController:
    def __init__(self):
        self.categories = [
            {"id": 1, "name": "Lebensmittel", "color": "#3B82F6", "limit": 0.00},
            {"id": 2, "name": "Transport", "color": "#8B5CF6", "limit": 0.00},
            {"id": 3, "name": "Wohnen", "color": "#10B981", "limit": 0.00},
            {"id": 4, "name": "Gesundheit", "color": "#EF4444", "limit": 0.00},
            {"id": 5, "name": "Shopping", "color": "#EC4899", "limit": 0.00},
            {"id": 6, "name": "Reisen", "color": "#06B6D4", "limit": 0.00},
            {"id": 7, "name": "Unterhaltung", "color": "#F97316", "limit": 0.00},
            {"id": 8, "name": "Allgemeines Sparen", "color": "#2B323F", "limit": 0.00},
            {"id": 9, "name": "Sonstiges", "color": "#CACFD7", "limit": 0.00},

        ]

    def getCategories(self):
        return {"categories":self.categories}
    
    def getCategoryByName(self, name):
        for category in self.categories:
            if category['name'] == name:
                return category
        return None     


    def updateCategory(self, old_name, new_name, color, limit):
        """Updates a category"""
        for category in self.categories:            
            if category['name'] == old_name:                               
                category['name'] = new_name
                category['color'] = color
                category['limit'] = float(limit)
                return True
        
        return False
