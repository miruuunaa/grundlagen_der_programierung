from identify import Id

class Dish(Id):
    def __init__(self, portion_size, price, id):
        self.portion_size = portion_size
        self.price = price
        Id.__init__(self, id)


