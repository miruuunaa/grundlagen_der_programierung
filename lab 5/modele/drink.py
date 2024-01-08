from modele.dish import Dish

class Drink(Dish):
    def __init__(self, id,  portionsize, price, alcohol_volume):
        self.alcohol_volume = alcohol_volume
        Dish.__init__(self, id, portionsize, price)

    def __str__(self):
        return f"{self.id},{self.portionsize},{self.price},{self.alcohol_volume}"
