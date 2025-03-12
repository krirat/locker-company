from User import User

class Transaction:
    def __init__(self, user : User, amount : float, transactionType : str, timestamp , transactionid : str):
        self.__user = user
        self.__amount = amount
        self.__transactionType = transactionType
        self.__timestamp = timestamp
        self.__transactionid = transactionid 
