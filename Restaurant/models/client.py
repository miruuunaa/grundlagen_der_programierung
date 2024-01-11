from models.id import ID

class Client(ID):
    def __init__(self, id, name, address):
        super().__init__(id)
        self.name = name
        self.address = address

    def __lt__(self, other):
        return self.name < other.name


    def __str__(self):
        return f"id={self.id}, name={self.name}, adress={self.address}"