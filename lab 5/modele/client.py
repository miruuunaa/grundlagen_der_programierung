from modele.identifiable import Identifiable

class Client(Identifiable):
    def __init__(self, id, name, adress):
        self.name = name
        self.adress = adress
        Identifiable.__init__(self, id)

    def __str__(self):
        return f"{self.id},{self.name},{self.adress}"