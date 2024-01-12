from dish import Dish

class Drink(Dish):

    def __init__(self, portion_size, price, id, alcohol_volume):
         self.alcohol_volume = alcohol_volume
         Dish.__init__(self, portion_size, price, id)