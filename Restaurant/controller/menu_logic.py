from repository.drinkRepo import DrinkRepo
from repository.cookeddishRepo import CookedDishRepo
from models.cookedDish import CookedDish
from models.drink import Drink
from controller.datarepo_logic import ShowData

cookedDishManager = CookedDishRepo('cookeddish.dat')
drinkManager = DrinkRepo('drink.dat')

def showMenu():
    print("CookedDishes: ")
    ShowData(0)

    print("Drinks: ")
    ShowData(1)

def addCookedDish():
    name = input("Name of the cooked dish: ")
    portionSize = int(input("Portion size of the cooked dish: "))
    price = int(input("Price of the cooked dish:"))
    prepTime = int(input("Time of the preparation for the cooked dish:"))

    cookedDishes = cookedDishManager.load() if cookedDishManager.load() else []
    cookedDish = CookedDish(name, portionSize, price, prepTime)
    cookedDishes.append(cookedDish)
    cookedDishManager.sort(cookedDishes)


def addDrink():
    name = input("Name of the drink: ")
    portionSize = int(input("Portion size of the drink: "))
    price = int(input("Price of the drink:"))
    alcoolVolume = int(input("Alcohol volume of the drink:"))

    drinks = drinkManager.load() if drinkManager.load() else []
    drink = Drink(name, portionSize, price, alcoolVolume)
    drinks.append(drink)
    drinkManager.sort(drinks)

def search():
    name = input("Enter the name of the searched item: ")
    cookeddishes = cookedDishManager.load() if cookedDishManager else []#list of objects type cooked dishes
    drinks = drinkManager.load() if drinkManager else [] #list of objects type drinks
    print('\n')
    if cookeddishes:
        print(" cooked Dishes: ", '\n')
        for idx in range(len(cookeddishes)):
            if name.lower() in cookeddishes[idx].id.lower():
                print(idx, str(cookeddishes[idx]))

    if drinks:
        print("Drinks: ", '\n')
        for idx in range(len(drinks)):
            if name.lower() in drinks[idx].id.lower():
                print(idx, str(drinks[idx]))

        return

    print("no such item found")

def updateItem():
    choose = int(input("""
    Enter the type you want to update:
        1 - cooked Dish
        2 - Drink
    """))
    id = int(input("Enter the id you wnat to update"))#id for updated variable variable
    if choose == 1:
        name = input("Enter the new name of the cooked dish: ")
        portionSize = input("Enter the new portion size: ")
        price = input("Enter the new price: ")
        prepTime = input("Enter the new preparation time: ")
        cookedDish = CookedDish(name,  portionSize, price, prepTime)
        cookedDishManager.update(id, cookedDish)

    else:
        name = input(("Enter the new name of the drink: "))
        portionsize = input("Enter the new portion size: ")
        price = input("Enter the new price: ")
        alcoholvolume = input("Enter the new alcohool volume: ")
        drink = Drink(name, portionsize, price, alcoholvolume)
        drinkManager.update(id, drink)

def showupdatedmenu():
    showMenu()
    updateItem()

def deleteItem():
    choose = int(input("""
    Enter the type you want to update:
        1 - cooked Dish
        2 - Drink
    """))

    id = int(input("Enter the id you want to delete:"))#id for deleted item

    if choose == 1:
        cookedDishManager.remove(id)
    else:
        drinkManager.remove(id)

def showmenuafterdelete():
    showMenu()
    deleteItem()