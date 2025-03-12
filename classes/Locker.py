from User import User

class Locker :
    def __init__(self, lockerNumber : int, status : str, assignedUser : User, pin : int, reservation) :
        self.__lockerNumber = lockerNumber
        self.__status = status
        self.__assignedUser = assignedUser
        self.__pin = pin
        self.__reservation = reservation

    def get_pin(self):
        return self.__pin
    
    def assignUser(self, user: User):
        self.assignUser = user
        self.status = "Occupied"
        print(f"Locker {self.__lockerNumber} assigned to {user.name}.")
        
    def free(self):
        self.assignUser = None
        self.status = "Available"
        self.reservation = None
        print(f"Locker {self.__lockerNumber} is now free.")

    def is_available(self):
        return self.status == "Available"
        