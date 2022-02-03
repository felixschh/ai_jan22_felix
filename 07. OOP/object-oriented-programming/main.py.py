# import pandas as pd
# import numpy as np
# import math
# import matplotlib as plt
from collections import Counter
from models.book import Book
from models.product import Product

if __name__ == '__main__':
    book = Book('Book name', 'Publisher name', '838283812438', 14.99)
    book2 = Book('Book2 name', 'Publisher name2', '83828382318', 20.99)
    print(book)
    print('\n')
    print(book2)


