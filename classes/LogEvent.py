from classes.User import User
from classes.Locker import Locker

class LogEvent:
    def __init__(self, user : User, locker : Locker, action : str, timestamp):
        self.user = user
        self.locker = locker
        self.action = action
        self.timestamp = timestamp
