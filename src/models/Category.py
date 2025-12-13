class Category:
    def __init__(self,id, name, color, max_amount):
        self.__id = id
        self.__name = name
        self.__color = color
        self.__max_amount = max_amount

    def get_color(self):
        return self.__color  

    def get_id(self):
        return self.__id  

    def get_max_amount(self):
        return self.__max_amount
  
    def get_name(self):
        return self.__name
    
    def set_max_amount(self, max_amount):
        self.__max_amount = max_amount