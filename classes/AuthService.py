from classes.User import User
from classes.Locker import Locker
from classes.NotificationService import NotificationService


import random

class AuthService:
    __users: list[User] = []
    
    __OTPrepo: dict[User] = {} #dictionaries to store all of the users, and their respective OTP strings.

    def registerUser(self, user: User):
        self.__users.append(user)

    def loginUser(self, email, password):
        for user in self.__users:
            if user.email == email and user.password == password:
                return user

        return False

    def validatePin(locker: Locker, pin) -> bool:
        pass

    def verifyOTP(self, user: User, otp: str):
        if user in self.__OTPrepo.keys():
            if self.__OTPrepo[user] == otp:
                self.__OTPrepo.pop(user) # deletes item from OTP repo.
                return True

    def sendOTP(self, user: User): # generates 6-digit code, random numbers.
        combinedPIN = ""
        for i in range(6):
            combinedPIN += str(random.randint(0,9))
        if user in self.__OTPrepo.keys(): # deletes existing OTP incase user already made one beforehand.
            self.__OTPrepo.pop(user)
        NotificationService.send_notification(user,f"Your OTP number is {combinedPIN}")
        self.__OTPrepo[user] = combinedPIN # holds OTP along with the user its linked to in __OTPrepo



    


