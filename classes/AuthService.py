from classes.User import User
from classes.Locker import Locker

class AuthService:
    __users: list[User] = []

    def registerUser(self, user: User):
        self.__users.append(user)

    def loginUser(self, email, password):
        for user in self.__users:
            if user.email == email and user.password == password:
                return "Access granted"

        return "Access Denied"

    def validatePin(locker: Locker, pin) -> bool:
        pass

    def verifyOTP():
        pass

    def sendOTP():
        pass

    


