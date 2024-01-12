import json
from repository.data_repo import Data_Repo
from modele.client import Client

class Client_Repo(Data_Repo):
    def __init__(self, filename):
        self.clients = []
        Data_Repo.__init__(self, filename)

    def create_newclient(self, client_id, client_name, client_adress):
        new_client = Client(client_id, client_name, client_adress)
        self.clients.append(new_client)
        return new_client

    def read_all(self):
        return self.clients

    def read_by_id(self, searched_id): # returns the searched id and if he doesn t exist returns None
        return next((client for client in self.clients if client.id == searched_id), None)

    def update(self, id, new_name = None, new_adress = None):
        for client in self.clients:
            if client.id == id:
                if new_name != None:
                    client.name = new_name
                if new_adress != None:
                    client.adress = new_adress

    def delete(self, id):
        for client in self.clients:
            if client.id == id:
                self.clients.remove(client)

    def convert_to_string(self, objects): #converts to string/json formated string
        return json.dumps(list(map(lambda obj: {'id': obj.id, 'name': obj.name, 'adress': obj.adress}, objects)))

    def convert_from_string(self, data):
        return list(map(lambda item: Client(item['id'], item['name'], item['adress']), json.loads(data)))
