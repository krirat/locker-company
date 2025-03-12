class Guest :
    def __init__(self, ID, password):
        self.__ID = ID
        self.__password = password
    
    def login(self, ID, password):
         print(f"{self.name} logged in.")
