from User import User
from Locker import Locker

class Reservation :
    def __init__(self, startTime, reservaionTime):
        self.__user : list[User] = []
        self.__locker : list[Locker] = []
        self.__startTime = startTime
        self.__reservationTime = reservaionTime
    
    def extendedReservaion(self):
        print(f"Reservation for locker {self.locker.lockerNumber} extended.")

    def cancel(self):
        self.locker.free()
        print(f"Reservation for locker {self.locker.lockerNumber} canceled.")

