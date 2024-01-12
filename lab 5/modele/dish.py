from modele.identifiable import Identifiable

class Dish(Identifiable):
    def __init__(self, id, portionsize, price):
        self.portionsize = portionsize
        self.price = price
        Identifiable.__init__(self, id)

    def __str__(self):
        return f"{self.id},{self.portionsize},{self.price}"