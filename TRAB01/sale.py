class Sale:
    __idClient = None
    __idProduct = None
    __amount = None
    __price = None
    __total = None

    def __init__(self, idClient, idProduct, amount, price, total):
        self.__idClient = idClient
        self.__idProduct = idProduct
        self.__amount = amount
        self.__price = price
        self.__total = total

    def getClientId(self):
        return self.__idClient

    def getProductId(self):
        return self.__idProduct

    
    def getSaleAmount(self):
        return self.__amount    

    
    def getSaleTotal(self):
        return self.__total