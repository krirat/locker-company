from classes.User import User
#from classes.Reservation import Reservation

class Locker :
    def __init__(self, lockerNumber : int, status : str, assignedUser : User, pin : int, startTime, remainingTime) :
        self.__lockerNumber = lockerNumber
        self.__status = status
        self.__assignedUser = assignedUser
        self.__pin = pin
        self.__startTime = startTime
        self.__remainingTime = remainingTime
    
    @property
    def number(self):
        return self.__lockerNumber

    def extendReservation(self):
        print(f"Reservation for locker {self.__lockerNumber} extended.")

    def cancel(self):
        self.free()
        print(f"Reservation for locker {self.__lockerNumber} canceled.")


    def get_pin(self):
        return self.__pin
    
    def assignUser(self, user: User):
        self.__assignedUser = user
        self.__status = "Occupied"
        print(f"Locker {self.__lockerNumber} assigned to {user.name}.")
        
    def free(self):
        self.__assignedUser = None
        self.__status = "Available"
        self.reservation = None
        print(f"Locker {self.__lockerNumber} is now free.")

    def is_available(self):
        return self.__status == "Available"
        