from controller.menu_logic import showMenu, addDrink, addCookedDish, search, showupdatedmenu, showmenuafterdelete
from controller.client_logic import showClients, addClient, deleteClient, updateClients
from controller.orders_logic import showOrders, searchbyAddress, searchclientName, newOrder, addCLientsOrder


def Console():
    choose = {
    1: menuConsole,
    2: clientConsole,
    3: orderConsole
    }

    while True:
        print("""
        1 - Menu
        2 - Clients
        3 - Order
        0 - Exit
        """)
        option = int(input("Choose an option"))
        if option == 0:
            exit()

        choose[option]()


def dishType():
    value = int(input("""
    Choose the type of dish you want to add
        1 - Cooked Dish
        2 - Drink
    """))

    options = {
        1: addCookedDish,
        2: addDrink
    }

    options[value]()
    print("Added item")
    menuConsole()


def menuConsole():
    while True:
        value = int(input(""" 
        1 - View Menu
        2 - Search for item
        3 - Add a new item to the menu
        4 - Update an item
        5 - Delete an item
        0 - Back
        """))

        options = {
            1: showMenu,
            2: search,
            3: dishType,
            4: showupdatedmenu,
            5: showmenuafterdelete,
            0: Console
        }


        options[value]()

        menuConsole()

def clientConsole():
    while True:
        value = int(input("""
            1 - View all CLients
            2 - Add a new Client
            3 - Delete a Client
            4 - Update a Client
            0 - Back
        """))

        options = {
            1: showClients,
            2: addClient,
            3: deleteClient,
            4: updateClients,
            0: Console
        }

        options[value]()
        clientConsole()



def orderConsole():
    while True:
        value = int(input(""" 
            1 - View all Orders
            2 - Add a new order
            0 - Back
        """))

        options = {
            1: showOrders,
            2: selectClientConsole,
            0: Console
        }

        options[value]()

def selectClientConsole():
    value = int(input("""  
        1 - Search Client by name
        2 - Search CLient by address
        3 - Add a new Client and Order
        0 - Back
    """))


    options = {
        1: searchclientName,
        2: searchbyAddress,
        3: addCLientsOrder,
        0: orderConsole
    }

    options[value]()

    newOrder()