from modele.order import Order
from modele.drink import Drink
from modele.cooked_dish import Cooked_Dish

def main():
    dishes1 = {'dish1': 13, 'dish2': 35}
    drinks1 = {'drink1': 7, 'drink2': 6}
    dishes2 = {'dish1': 57, 'dish2': 95}
    drinks2 = {'drink1': 46, 'drink2': 16}

    order1 = Order('order1', 'bob', dishes1, drinks1)
    order2 = Order('order2', 'dob', dishes2, drinks2)

    order1.calculate_prices()
    print(order1.total_price)

    print(order1.print_receipt())



main()