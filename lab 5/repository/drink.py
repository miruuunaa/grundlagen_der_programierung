import json
from repository.data_repo import Data_Repo
from modele.drink import Drink

class Drink_Repo(Data_Repo):
    def __init__(self, filename):
        self.drinks = [] #we store here drinks
        Data_Repo.__init__(self, filename)

    def create_newdrink(self, drink_id, drink_size, drink_price, drink_alcvolume):
        new_drink = Drink(drink_id, drink_size,drink_price,drink_alcvolume)
        self.drinks.append(new_drink)
        return new_drink

    def read_all(self):
        return self.drinks

    def read_by_id(self, searched_id): #return the Drink with the searched id and if it doesn t exist return None
       return next((drink for drink in self.drinks if drink.id == searched_id), None)

    def update(self, id, new_drink_size = None, new_drink_price = None, new_drink_alcvolume = None):
        for drink in self.drinks:
            if drink.id == id:
                if new_drink_size != None:
                    drink.portionsize = new_drink_size
                if new_drink_price != None:
                    drink.price = new_drink_price
                if new_drink_alcvolume != None:
                    drink.alcohol_volume = new_drink_alcvolume

    def delete(self, id):
        for drink in self.drinks:
            if drink.id == id:
                self.drinks.remove(drink)

    def convert_to_string(self, objects):# converts to string/json formated string
        return json.dumps(list(map(lambda obj: {'id': obj.id, 'drink_size':obj.portionsize, 'price':obj.price, 'alcvolume':obj.alcohol_volume}, objects)))

    def convert_from_string(self, data): #vonverts from string to object
        return list(map(lambda item: Drink(item['id'], item['drink_size'], item['price'], item['alc_volume']), json.loads(data)))