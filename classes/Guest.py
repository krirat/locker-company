from classes.User import User

class Guest(User) : 
    def login(self, id, password):
         print(f"{self.name} logged in.")
