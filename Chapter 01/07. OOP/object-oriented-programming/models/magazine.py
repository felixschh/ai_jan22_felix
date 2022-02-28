from models.product import Product

class Magazine(Product):
    def __init__(self, name, selling_price=0):
        super().__init__(name, selling_price)

