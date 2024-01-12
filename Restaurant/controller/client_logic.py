from repository.clientRepo import ClientRepo
from models.client import Client
from controller.datarepo_logic import ShowData
from repository.orderRepo import OrderRepo

clientManager = ClientRepo('clients.dat')
orderManager = OrderRepo('orders.dat')
def showClients():
    print("Client: ")
    ShowData(2)

def addClient():
    name = input("Clients Name: ")
    adress = input("Clients Adress: ")

    clients: list = clientManager.load() if clientManager.load() else []
    client = Client(1, name, adress)
    clients.append(client)
    clientManager.sort(clients)

def updateClients():
    showClients()
    idList = int(input("The id of the item you want to update: "))
    clients: list = clientManager.load()

    id = clients[idList].id
    name = input("Enter the new name: ")
    adress = input("Enter the new adress: ")
    client = Client(id, name, adress)
    clientManager.update(idList, client)


def deleteClient():
    showClients()
    id = int(input("Enter the id you want to delete:"))
    clientManager.remove(id)
    orderManager.remove(id)





