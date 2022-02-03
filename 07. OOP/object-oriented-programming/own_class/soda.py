from own_class.drinks import Drink

#
# ABSTRACTION AND ENCAPSULATING
#

class Soda(Drink):
    def __init__(self, name, fillingstation, amount_of_sugar, selling_price=0): # constructor
        super().__init__(name, fillingstation, selling_price)
        self.amount_of_sugar = amount_of_sugar
        if selling_price > 0:
            self.__selling_price = selling_price

    
    @property
    def selling_price(self):
        return self.__selling_price

    @selling_price.setter
    def selling_price(self, price):
        if price <= 0:
            raise ValueError("The price must be greater that 0, at this Company nothing is for free!")
        self.__selling_price = price


    def __str__(self):
        return f'Drink:{self.name}\nProduct Price: {self.selling_price}\nFillingstation: {self.fillingstation}\nAmount of sugar: {self.amount_of_sugar}'