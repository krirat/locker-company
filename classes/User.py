class User : 
    def __init__(self, id : int, name : str, email : str, phone : int, password : str) :
        self.__id = id
        self.__name = name
        self.__email = email 
        self.__phone = phone
        self.__password = password 
        
    @property
    def id(self):
        return self.__id 

    @property
    def password(self):
        return self.__password   

    def login(self, id, password):
        print(f"{self.name} logged in.")

    def reserve_locker(self):
        print(f"{self.name} reserved a locker")
