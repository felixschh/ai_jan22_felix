from models.book import Book
from models.product import Product

if __name__ == '__main__':
    book = Book('Book name', 'Publisher name', '838283812438', 14.99)
    product = Product('Product Name', 20.99)

    all_products = [book, product]

    for i in all_products:
        print(i)
        print("#########################")


