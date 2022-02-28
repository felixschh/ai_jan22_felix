from models.product import Product

#
# ABSTRACTION AND ENCAPSULATING
#

class Book(Product):
    def __init__(self, name, publisher, isbn, selling_price=0): # constructor
        super().__init__(name, selling_price)
        self.publisher = publisher
        self.isbn = isbn
        if selling_price > 0:
            self.__selling_price = selling_price
    
    @property
    def selling_price(self):
        return self.__selling_price


    #SETTER
    @selling_price.setter
    def selling_price(self, price):
        if price <= 0:
            raise ValueError("The price must be greater that 0, we don't give away books for free!")
        self.__selling_price = price


    def __str__(self):
        return f'Book name:{self.name}\nBook Publisher: {self.publisher}\nBook ISBN: {self.isbn}\nBook Price: {self.selling_price}'
