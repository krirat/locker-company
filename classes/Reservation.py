from classes.User import User
from classes.Locker import Locker

from classes.NotificationService import NotificationService

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
    
    def extendReservation(self, user, period):
        self.__reservationTime += period
        NotificationService.send_notification(user,f"Your reservation for locker {self.locker.number} has been extended.")
        print(f"Reservation for locker {self.locker.lockerNumber} extended.")

    def cancel(self):
        self.locker.free()
        print(f"Reservation for locker {self.locker.lockerNumber} canceled.")

