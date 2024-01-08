from identify import Id
from dish import Dish
from drink import Drink
from functools import reduce

class Order(Id):
    def __init__(self, id, client_id, dish_list_id, drink_list_id, total_price):
        self.client_id = client_id
        self.dish_list_id = dish_list_id
        self.drink_list_id = drink_list_id
        self.total_price = 0
        Id.__init__(self, id)

#trebe facute metodele


