from own_class.drinks import Drink
from own_class.soda import Soda

if __name__ == '__main__':
    water = Drink('Water ', 'Hamburg', 1.00)
    soda = Soda('Coke', 'Munich', '40g/100ml', 1.50)

    all_drinks = [water, soda]

    for drink in all_drinks:
        print(drink)
        print("------------------")
