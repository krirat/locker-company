from User import User
from Locker import Locker

class Reservation :
    def __init__(self, user, locker, startTime, reservationTime):
        self.__user = user
        self.__locker = locker
        self.__startTime = startTime
        self.__reservationTime = reservationTime
    
    def extendReservation(self):
        print(f"Reservation for locker {self.locker.lockerNumber} extended.")

    def cancel(self):
        self.locker.free()
        print(f"Reservation for locker {self.locker.lockerNumber} canceled.")

