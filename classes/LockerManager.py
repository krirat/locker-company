from classes.Locker import Locker
from classes.Reservation import Reservation

class LockerManager:
    def __init__(self, name : str):
        self.name = name
        self.lockers : list[Locker] = []
        self.reservations: list[Reservation] = []

    def add_locker(self):
        self.lockers.append(Locker(0,"Available",None,""))

    def remove_locker(self):
        self.lockers.pop()

    def get_available(self) -> list[Locker]:
        return [locker for locker in self.lockers if locker.isAvailable()]
    
    def assign_locker_to_user(self, locker: Locker, user):
        if locker.isAvailable():
            locker.assignUser(user)
        else:
            print(f"Locker {locker.number} is not available")

    def release_locker(self, locker: Locker):
        locker.free()


    def get_locker_by_number(self, number) -> Locker:
        return self.lockers[number]
    
    def add_reservation(self, reservation):
        self.reservations.append(reservation)

    def get_reservations_from_user(self, user) -> list[Reservation]:
        return [rsv for rsv in self.reservations if rsv.user == user]

    def get_reservation_from_locker(self, locker) -> Reservation:
        for rsv in self.reservations:
            if rsv.locker == locker:
                return rsv
    