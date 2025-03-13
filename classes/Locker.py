from classes.User import User

class Locker :
    def __init__(self, lockerNumber : int, status : str, assignedUser : User, pin : str) :
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
    
    @property
    def assignedUser(self) -> User:
        return self.__assignedUser


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

    def isAvailable(self):
        return self.__status == "Available"
        