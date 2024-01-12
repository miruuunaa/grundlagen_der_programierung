from models.dish import Dish

class Drink(Dish):
    def __init__(self, id, portionSize, price, alcoolVolume):
        super().__init__(id, portionSize, price)
        self.alcoolVolume = alcoolVolume

    def __lt__(self, other):
        return self.id < other.id

    def __iter__(self):#iterates the object in this way(id, price)
        return iter(self.id, self.price)



    def __str__(self):
        return f"id={self.id}, portionsize={self.portionSize}, price={self.price}, alcoolvolume={self.alcoolVolume}"
