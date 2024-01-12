from repository.clientRepo import ClientRepo
from repository.drinkRepo import DrinkRepo
from repository.cookeddishRepo import CookedDishRepo
from repository.orderRepo import OrderRepo


def ShowData(Type):#primeste ca parametru timpul de repository
    types = {
        0: CookedDishRepo('cookeddish.dat'),
        1: DrinkRepo('drink.dat'),
        2: ClientRepo('clients.dat'),
        3: OrderRepo('orders.dat')
    }

    repo = types[Type]#maybe change to types[Type] and up without files name

    list = repo.load()
    if list:#sa afiseze variantele de iteme
        for idx in range(len(list)):
            print(idx, str(list[idx]))

    print('\n')
