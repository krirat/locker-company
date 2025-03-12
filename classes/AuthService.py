from User import User
from Locker import Locker

class AuthService:
    __users: list[User] = []

    def registerUser(self, user: User):
        self.__users.append(user)

    def loginUser(self, id, password):
        for user in self.__users:
            if user.id == id and user.password == password:
                return print("Access granted")

        print("Access Denied")

    def validatePin(locker: Locker, pin) -> bool:
        pass

    def verifyOTP():
        pass
    
    def sendOTP():
        pass

    


