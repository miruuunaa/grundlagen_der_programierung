from modele.dish import Dish

class Cooked_Dish(Dish):
    def __init__(self, id, portionsize, price, prep_time):
        self.prep_time = prep_time
        Dish.__init__(self, id, portionsize, price)

    def __str__(self):
        return f"{self.id},{self.portionsize},{self.price},{self.prep_time}"