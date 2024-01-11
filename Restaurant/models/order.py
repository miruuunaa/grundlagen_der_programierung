from models.id import ID
from functools import reduce
from controller.menu_logic import drinkManager, cookedDishManager

class Order(ID):
    total = 0
    def __init__(self, id, clientId, dishIds, drinkIds):
        super().__init__(id)
        self.clientId = clientId
        self.dishIds = dishIds
        self.drinkIds = drinkIds

    def calculateCost(self):
        cookeddishList = cookedDishManager.load()
        drinkList = drinkManager.load()
        prices = []

        for dish in cookeddishList:
            if dish.id in self.dishIds:
                prices.append(int(dish.price))

        for drink in drinkList:
            if drink.id in self.drinkIds:
                prices.append(int(drink.price))


        self.total = reduce(lambda x, y: x + y, prices)


    def __generateReceipt(self):#private methode
        self.calculateCost()
        cookeddishList = cookedDishManager.load()
        drinkList = drinkManager.load()
        receipt = f"Order: {self.id} for the client with the id {self.clientId}" + '\n'

        ids = []
        prices = []

        for dish in cookeddishList:
            if dish.id in self.dishIds:
                ids.append(dish.id)
                prices.append(str(dish.price))

        for drink in drinkList:
            if drink.id in self.drinkIds:
                ids.append(drink.id)
                prices.append(str(drink.price))

        items = list(map(lambda x, y: f"Item: {x}  Price: {y}" + '\n', ids, prices))

        receipt += "".join(items)
        receipt += f"TotalL {str(self.total)}"

        return receipt

    def printReceipt(self):
        receipt = self.__generateReceipt()
        print(receipt)

    def __lt__(self, other):
        return self.id < other.id

    def __str__(self):
        return f"Order: {self.id} Client: {self.clientId} Dishes: {self.dishIds} Drinks: {self.drinkIds}"