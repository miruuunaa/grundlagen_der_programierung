from repository.orderRepo import OrderRepo
from repository.clientRepo import ClientRepo
from controller.menu_logic import showMenu, drinkManager, cookedDishManager
from controller.client_logic import addClient
from controller.datarepo_logic import ShowData
from models.order import Order

orderManager = OrderRepo('orders.dat')
clientManager = ClientRepo('clients.dat')

def searchclientName():
    name = input("Enter the name of the searched Client: ")
    clients = clientManager.load() if clientManager.load() else [] #list o items object type clients
    print('\n')
    ids = []
    if clients:
        print("Client", '\n')
        for idx in range(len(clients)):
            if name.lower() in clients[idx].name.lower():
                print(idx, str(clients[idx]))
                ids.append(clients[idx].id)


def searchbyAddress():
    address = input("Enter the clients searched address: ")
    clients = clientManager.load() if clientManager.load() else []
    print('\n')
    ids = []
    if clients:
        print("Client", '\n')
        for idx in range(len(clients)):
            if address.lower() in clients[idx].address.lower():
                print(idx, str(clients[idx]))


def addCLientsOrder():
    print('\n', "Clients: ")
    ShowData(2)
    addClient()

def newOrder():
    value = int(input("Enter the id of the client that orders: "))
    ShowData(2)
    clients = clientManager.load()
    client = clients[value]

    cookeddishesIds = []
    drinksIds = []
    cookeddishes = cookedDishManager.load() if cookedDishManager.load() else []
    drinks = drinkManager.load() if drinkManager.load() else []

    showMenu()

    while True:
        choose = int(input("""
        Enter the item you want to add
        1 - Select a cooked dish
        2 - Select a drink
        0 - Exit
        """))

        if choose == 0:
            break

        if choose == 1:
            id = int(input("id: "))
            if id < len(cookeddishes):
                cookeddishesIds.append(cookeddishes[id].id)
            else:
                print("Not found")
        else:
            id = int(input("id: "))
            if id < len(drinks):
                drinksIds.append(drinks[id].id)
            else:
                print("Not found")

    order = Order(1, client.id, cookeddishesIds, drinksIds)
    orders = orderManager.load() if orderManager.load() else [] #list of objects type order
    orders.append(order)
    orderManager.sort(orders)

    order.printReceipt()



def showOrders():
    print("Orders", '\n')
    ShowData(3)

    orders = orderManager.load()
    value = int(input("Show the receipt of wich order you want: "))
    orders[value].printReceipt()
