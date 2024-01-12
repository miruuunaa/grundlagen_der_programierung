import pickle
from abc import abstractmethod

class DataRepo:
    def __init__(self, filename):
        self.filename = filename

    def save(self, objectList):
        with open(self.filename, 'wb') as file:
            pickle.dump(objectList, file)

    def load(self):
        with open(self.filename, 'rb') as file:
            try:
                return pickle.load(file)
            except EOFError:
                print("DATABASE EMPTY")

    def sort(self, objectList):
        objectList = sorted(objectList)
        self.save(objectList)

    def add(self, object):#adding a new object
        objectList: list = self.load()
        objectList.append(object)
        self.sort(objectList)
        print("Added new item")

    def remove(self, id):#removing an item by id
        objectList = self.load()
        if id < len(objectList):# if id is found
            objectList.pop(id)
            self.save(objectList)
            print("Item removed")
            return

        print("Item not found")

    def update(self, id, newObj):
        objectList: list = self.load()
        if id < len(objectList):
            self.remove(id)
            self.add(newObj)
            print("Item updated")
            return

        print("Item not found")

    @abstractmethod
    def convert_to_string(self, list):
        pass

    @abstractmethod
    def convert_from_string(self, string):
        pass