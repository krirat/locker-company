from Guest import Guest
from Admin import Admin
from Maintenance import Maintenance

class User : 
    def __init__(self, ID : int, name : str, email : str, phone : int, password : str) :
        self.__ID = ID
        self.__name = name
        self.__email = email 
        self.__phone = phone
        self.__password = password 
        self.__guest = Guest
        self.__admin = Admin
        self.__maintenance = Maintenance

    def login(self, ID, password):
        print(f"{self.name} logged in.")

    def reserve_locker(self):
        print(f"{self.name} reserved a locker")
