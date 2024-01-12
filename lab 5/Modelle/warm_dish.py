from dish import Dish

class Warm_Dish(Dish):
    def __init__(self, portion_size, price, id, prep_time):
        self.prep_time = prep_time
        Dish.__init__(self, portion_size, price, id)

