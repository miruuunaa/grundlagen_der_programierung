from repository.dataRepository import DataRepo

class OrderRepo(DataRepo):
 def __init__(self, filename):
        super().__init__(filename)

 def convert_to_string(self, list):
        return map(lambda x: str(x), list)

 def convert_from_string(self, string):
        objectList = []
        return map(lambda x: objectList.append(x), string)