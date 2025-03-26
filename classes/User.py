class User : 
    def __init__(self, name : str, email : str, phone : str, password : str, balance : int = 0) :
        #self.__id = id
        self.__name = name
        self.__email = email 
        self.__phone = phone
        self.__password = password 
        self.__balance = balance
        
    # @property
    # def id(self):
    #     return self.__id 
    
    @property
    def email(self):
        return self.__email 

    @property
    def password(self):
        return self.__password

    @property
    def name(self):
        return self.__name  
     
    @property
    def phone(self):
        return self.__phone   
    
    @property
    def balance(self):
        return self.__balance

    def login(self, id, password):
        print(f"{self.name} logged in.")

    def reserve_locker(self):
        print(f"{self.name} reserved a locker")

    def update_balance(self, amount : float):
        self.__balance += amount
