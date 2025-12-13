class Expense:
    def __init__(self, id, name, date, amount, category, description):
        self.id = id
        self.__name = name
        self.__amount = amount
        self.__category = category
        self.__date = date
        self.__description = description

    def get_name(self):
       return self.__name
 
    def get_date(self):
       return self.__date

    def get_amount(self):
        return self.__amount    
    
    def get_category(self):
        return self.__category
    
    def get_description(self):
        return self.__description