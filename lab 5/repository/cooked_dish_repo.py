import json
from repository.data_repo import Data_Repo
from modele.cooked_dish import Cooked_Dish

class Cooked_Dish_Repo(Data_Repo):
    def __init__(self, filename):
        self.cooked_dishes = [] # we store here cooked dishes
        Data_Repo.__init__(self, filename)

    def create_newdish(self, dish_id, dish_size, dish_price, dish_prep_time): #creates a new dish and adds it to the list where we store the cooked dishes
        new_dish = Cooked_Dish(dish_id, dish_size, dish_price, dish_prep_time)
        self.cooked_dishes.append(new_dish)
        return new_dish

    def read_all(self):#return the cookeddishes
        return self.cooked_dishes

    def read_by_id(self, searched_id): # returns the CookedDish with the specified id if it doesnt find it return None
        return next((dish for dish in self.cooked_dishes if dish.id == searched_id), None)


    def update(self, id, new_dish_size = None, new_dish_price = None, new_dish_prep_time = None): #updates the CookedDishes
        for dish in self.cooked_dishes:
            if dish.id == id:
                if new_dish_size != None:
                    dish.portionsize = new_dish_size
                if new_dish_price != None:
                    dish.price = new_dish_price
                if new_dish_prep_time != None:
                    dish.prep_time = new_dish_prep_time

    def delete(self, id):
        for dish in self.cooked_dishes:
            if dish.id == id:
                self.cooked_dishes.remove(dish)


    def convert_to_string(self, objects):#converts to string/json formated string
        return json.dumps(list(map(lambda obj: {'id': obj.id, 'portion_size': obj.portionsize, 'price': obj.price, 'prep_time': obj.prep_time}, objects)))

    def convert_from_string(self, data):#converts from string to object
        return list(map(lambda item: Cooked_Dish(item['id'], item['portionsize'], item['price'], item['prep_time']), json.loads(data)))