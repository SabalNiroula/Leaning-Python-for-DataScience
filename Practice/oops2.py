from abc import *

class Myclass(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass

class Oracle(Myclass):

    def connect(self):
        print("connecting to the oracle database")
    
    def disconnect(self):
        print("disconnecting frmo the server....")


class Sybase(Myclass):

    def connect(self):
        print("connecting to the oracle database")

    def disconnect(self):
        print("disconnecting frmo the server....")

class Database:
    str = input("Enter database name: ")
    classname = globals()[str]
    x = classname()
    x.connect()
    x.disconnect()