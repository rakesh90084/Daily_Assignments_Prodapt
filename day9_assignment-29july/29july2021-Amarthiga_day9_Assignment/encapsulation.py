class headphone:
    def __init__(self):
        self.__price=500
        self.x=150
    def sellingprice(self):
        print(self.__price)
        print("x= ",self.x)
    def offerprice(self,discount):
        self.__price = self.__price-discount

objectHp=headphone()
objectHp.sellingprice()
objectHp.__price = 250
objectHp.sellingprice()
objectHp.offerprice(200)
objectHp.x = 600
objectHp.sellingprice()


