from models.dish import Dish

class CookedDish(Dish):
    def __init__(self, id, portionSize, price, prepTime):
        super().__init__(id, portionSize, price)
        self.prepTime = prepTime

    def __lt__(self, other):
        return self.id < other.id

    def __iter__(self):#iterates the object in this way(id, price)
        return iter(self.id, self.price)


    def __str__(self):
        return f"id={self.id}, portionsize={self.portionSize}, price={self.price}, preptime={self.prepTime}"