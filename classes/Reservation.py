from classes.User import User
from classes.Locker import Locker

class Reservation :
    def __init__(self, user, locker, startTime, reservationTime):
        self.__user = user
        self.__locker = locker
        self.__startTime = startTime
        self.__reservationTime = reservationTime

    @property
    def user(self):
        return self.__user
    
    @property
    def locker(self):
        return self.__locker
    
    def extendReservation(self):
        print(f"Reservation for locker {self.locker.lockerNumber} extended.")

    def cancel(self):
        self.locker.free()
        print(f"Reservation for locker {self.locker.lockerNumber} canceled.")

