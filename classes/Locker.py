from classes.User import User
#from classes.Reservation import Reservation

class Locker :
    def __init__(self, lockerNumber : int, status : str, assignedUser : User, pin : int) :
        self.__lockerNumber = lockerNumber
        self.__status = status
        self.__assignedUser = assignedUser
        self.__pin = pin
        
    
    @property
    def number(self):
        return self.__lockerNumber
    
    @property
    def status(self):
        return self.__status


    def get_pin(self):
        return self.__pin
    
    def set_pin(self, pin):
        self.__pin = pin
    
    def assignUser(self, user: User):
        self.__assignedUser = user
        self.__status = "Occupied"
        print(f"Locker {self.__lockerNumber} assigned to {user.name}.")
        
    def free(self):
        self.__assignedUser = None
        self.__status = "Available"
        print(f"Locker {self.__lockerNumber} is now free.")

    def is_available(self):
        return self.__status == "Available"
        