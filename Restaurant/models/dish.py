from models.id import ID
class Dish(ID):
    def __init__(self, id, portionSize, price):
        super().__init__(id)
        self.portionSize = portionSize
        self.price = price
