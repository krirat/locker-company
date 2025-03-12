class Maintanance :
        def __init__(self, ID, password) :
            self.__ID = ID
            self.__password = password

        def login(self, ID, password):
            print(f"{self.name} logged in.")

        def markMaintanance(self, locker,):
            locker.status = "Under maintenance"
            print(f"Locker {locker.lockerNumber} marked maintenance")

        def unmarkMaintenance(self, locker):
            locker.status = "Available"
            print(f"Locker {locker.lockerNumber} is now available")
