class Mobilephone:
    def __init__(self):
        self.__price=2000
        self.x=500
    def Sellingprice(self):
        print(self.__price)
        print("x=",self.x)
    def Offerprice(self,discount):
        self.__price=self.__price-discount
ob=Mobilephone()
ob.Sellingprice()
# ob.__price=500
# ob.Sellingprice()
ob.Offerprice(500)
ob.Sellingprice()
ob.x=1000
ob.Sellingprice()