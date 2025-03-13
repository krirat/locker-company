from classes.Locker import Locker

class LockerManager:
    def __init__(self, name : str):
        self.name = name
        self.lockers : list[Locker] = []

    def get_available(self) -> list[Locker]:
        return [locker for locker in self.lockers if locker.isAvailable()]
    
    def assign_locker_to_user(self, locker: Locker, user):
        if locker.isAvailable():
            locker.assignUser(user)
        else:
            print(f"Locker {locker.number} is not available")

    def release_locker(self, locker):
        locker.free()

    def get_locker_by_number(self, number) -> Locker:
        return self.lockers[number]
    