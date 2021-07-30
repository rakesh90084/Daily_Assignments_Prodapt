class Mobphone:
    def __init__(self):
        self.__price=2000 #private variable
        self.x=300
    def sellPrice(self):
        print(self.__price)
        print("x=",self.x)
    def offerPrice(self,discount):
        self.__price=self.__price-discount
ob1=Mobphone()
ob1.sellPrice()       
ob1.__price=3000
ob1.sellPrice()
ob1.offerPrice(500)
ob1.sellPrice()
ob1.x=90
ob1.sellPrice()