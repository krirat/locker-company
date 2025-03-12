from User import User

class Admin(User):

    def login(self, id, __password):
         print(f"{self.name} logged in.")

    def assign_locker(self, locker, user):
        locker.assign_user(user)

    def remove_locker_reservation(self, locker):
        locker.free()
    
    def change_locker_pin(self, pin, locker):
        locker.get_pin() = pin
        print(f"Locker {locker.lockerNumber} pin changed.")