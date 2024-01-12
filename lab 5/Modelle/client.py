from identify import Id

class Client(Id):
    def __init__(self, id, name, adress):
        self.name = name
        self.adress = adress
        Id.__init__(self, id)