from User import User

class Maintenance(User) :

        def login(self, id, password):
            print(f"{self.name} logged in.")

        def markMaintenance(self, locker):
            locker.status = "Under maintenance"
            print(f"Locker {locker.lockerNumber} marked maintenance")

        def unmarkMaintenance(self, locker):
            locker.status = "Available"
            print(f"Locker {locker.lockerNumber} is now available")
