from modele.order import Order
from modele.drink import Drink
from modele.cooked_dish import Cooked_Dish

def main():
    dishes1 = {'dish1': 12, 'dish2': 30}
    drinks1 = {'drink1': 6, 'drink2': 5}
    dishes2 = {'dish1': 56, 'dish2': 90}
    drinks2 = {'drink1': 45, 'drink2': 15}

    order1 = Order('order1', 'bob', dishes1, drinks1)
    order2 = Order('order2', 'dob', dishes2, drinks2)

    order1.calculate_prices()
    print(order1.total_price)

    print(order1.print_receipt())



main()