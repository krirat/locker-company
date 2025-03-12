class LockerManager:
    def __init__(self, name : str):
        self.name = name
        self.lockers : list[Locker] = []

    def get_available(self):
        return [locker for locker in self.lockers if locker.is_available()]
    
    def assign_locker_to_user(self, locker, user):
        if locker.is_available():
            locker.assign_user(user)
        else:
            print(f"Locker {locker.lockerNumber} is not available")

    def release_locker(self, locker):
        locker.free

    def get_locker_by_number(self, number):
        for locker in self.lockers:
            if locker.__lockerNumber == number:
                return locker
        return None
    