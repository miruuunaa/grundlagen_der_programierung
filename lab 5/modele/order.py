from modele.identifiable import Identifiable
from functools import reduce

class Order(Identifiable):
    total_price = 0
    def __init__(self, id, client_id, dishes_ids, drinks_ids):
        self.client_id = client_id
        self.dishes_ids = dishes_ids
        self.drinks_ids = drinks_ids
        Identifiable.__init__(self, id)

    def calculate_prices(self): # trebe construit si un file unde avem doar id ul bauturi/mancari si pretul ei
        dishPrice = reduce(lambda a, b: a + b, self.dishes_ids.values())
        drinkPrice = reduce(lambda a, b: a + b, self.drinks_ids.values())
        self.total_price = dishPrice + drinkPrice

    def __calculate_receipt__(self):
        receiptDishes = list(map(lambda a, b: a + ':' + str(b) + ' lei', self.dishes_ids.keys(), self.dishes_ids.values()))
        receiptDrinks = list(map(lambda a, b: a + ':' + str(b) + ' lei', self.drinks_ids.keys(), self.drinks_ids.values()))
        receipt = receiptDishes + receiptDrinks

        return receipt

    def print_receipt(self):
        return self.__calculate_receipt__()
