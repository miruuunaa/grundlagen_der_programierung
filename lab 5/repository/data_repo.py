from abc import  abstractmethod
class Data_Repo():
    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def convert_to_string(self, objects):
        pass

    @abstractmethod
    def convert_from_string(self, data):
        pass

    def read_file(self): # reads the jsonfile and return the content
        with open(self.filename, 'r') as file:
            return file.read()

    def write_to_file(self,string): # writes a string in the json file and overwrites the file
        with open(self.filename,'w') as file:
            file.write(string)

    def save_to_file(self, object_list_to_save):
        data_string = self.convert_to_string(object_list_to_save)
        self.write_to_file(data_string)

    def load_to_file(self):
        data_string = self.read_file()
        return self.convert_from_string(data_string)