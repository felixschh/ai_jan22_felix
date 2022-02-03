class Drink:
    def __init__(self, name, fillingstation, selling_price=0): # constructor
        self.name = name
        self.fillingstation = fillingstation
        self.__selling_price = 0 
        if selling_price > 0:
            self.__selling_price = selling_price
    
    @property
    # GETTER
    def selling_price(self):
        return self.__selling_price


    #SETTER
    @selling_price.setter
    def selling_price(self, price):
        self.__selling_price = price

    def __str__(self):
        return f'Drink:{self.name}\nProduct Price: {self.selling_price}\nFillingstation: {self.fillingstation}'

