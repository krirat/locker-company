class Admin:
    def __init__(self, ID : int, password : str, email : str, name : str, phone : int,) :
        self.__ID = ID
        self.__password = password
        self.__email = email 
        self.__name = name
        self.__phone = phone

    def login(self, ID, __password):
         print(f"{self.name} logged in.")

    def assign_locker(self, locker, user):
        locker.assign_user(user)

    def remove_locker_reservation(self, locker):
        locker.free()
    
    def change_locker_pin(self, pin, locker):
        locker.get_pin() = pin
        print(f"Locker {locker.lockerNumber} pin changed.")