import pymongo,collections,logging
logging.basicConfig(filename='product.log',level=logging.DEBUG)

client=pymongo.MongoClient("mongodb://localhost:27017/")
#client=pymongo.MongoClient("mongodb+srv://Balu862:balu1234@cluster0.ug6wk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

mydata=client["Productdb"]
productcollection=mydata["product"]

productdeque=collections.deque()
print(productdeque)
class Product:
    def addproduct(self,pcode,name,distributorname,manufactureyear,wholesaleprice,retailprice,description,contactnumber):
        dict1={"pcode":pcode,"name":name,"distributor":distributorname,"manufactureyear":manufactureyear,"wholesaleprice":wholesaleprice,"retailprice":retailprice,"description":description,"contactnumber":contactnumber}
        productdeque.append(dict1)
        result=productcollection.insert_many(productdeque)
        print(result)
obj1=Product()
try:
    while(1):
        print("1) add employee")
        print("2) search ")
        print("3) Display :")
        print("4) edit: ")
        print("5) Exit")
        option=int(input("enter the option : "))
        if option==1:
            pcode=input("Enter the pcode : ")
            name=input("enter the name: ")
            distributorname=input("Enter the Distributor name : ")
            manufactureyear=input("enter the manufacture year: ")
            wholesaleprice=input("Enter the Wholesale price : ")
            retailprice=input("Enter the retail price : ")
            description=input("enter the description : ")
            contactnumber=input("enter the phone: ")
            obj1.addproduct(pcode,name,distributorname,manufactureyear,wholesaleprice,retailprice,description,contactnumber)
        if option==2:
            names=input("enter the name :")
            result=productcollection.find({"name":names})
            print(result)
            for i in result:
                print(i)
        if option==3:
            result=productcollection.find({},{"_id":0})
            print(result)
            for i in result:
                print(i)

        if option==4:
            names=input("Enter the product name you have to update")
            wholesaleprices=input("Enter the Wholesale price : ")
            retailprices=input("Enter the retail price : ")
            result=productcollection.update_one({"name":names},{"$set":{"wholesaleprice":wholesaleprices,"retailprice":retailprices}})
            print(result)
        if option==5:
            break
except:
    logging.error("some thing went wrong")
