from collections import Counter

#
# ABSTRACTION AND ENCAPSULATING
#

class Product:
    def __init__(self, name,  selling_price=0): # constructor
        self.name = name
        self.__selling_price = 0 
        self.__rating_stars = [] # __ means private
        if selling_price > 0:
            self.__selling_price = selling_price
    
    @property
    # GETTER
    def selling_price(self):
        return self.__selling_price


    #SETTER
    @selling_price.setter
    def selling_price(self, price):
        if price <= 0:
            raise ValueError("The price must be greater that 0, we don't give away books for free!")
        self.__selling_price = price

    def add_rating(self, stars):
        self.__rating_stars.append(stars)
        # s = [5,5,5,4,4,2,1,3]

    def get_ratings_average(self):
        return sum(self.__rating_stars) / len(self.__rating_stars)

    def get_total_ratings(self):
        return len(self.__rating_stars)

    def get_stars_count(self):
        return dict(Counter(self.__rating_stars))

    def __str__(self):
        return f'Product name:{self.name}\nProduct Price: {self.selling_price}'

