
import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017")
mydatabase=client["productDb"]
collection=mydatabase["Products"]
productlist=[]
view=[]
delete=[]
class product:
    def productdetails(self,productId,productName,distributorName,manufacturingyYear,wholesalePrice,retailPrice,pDes,mContact):
         dict1={"productId":productId,"productName":productName,"distributorName":distributorName,"manufacturingYear":manufacturingYear,"wPrice":wPrice,"rPrice":rPrice,"pDes":pDes,"mContact":mContact}
         productlist.append(dict1)
obj=product()
while(True):
    print("1. Add Product")
    print("2. View product")
    print("3.search product using name")
    print("4.know details by entering pcode")
    print("5.to delete the product")
    print("6.exit")

    option=int(input("Enter option: "))
    if option==1:

        productId=input("Enter productid:: ")
        productName=input("Enter product name: ")
        distributorName=input("Enter distributor name: ")
        manufacturingYear=input("Enter manufacturing year: ")
        wholesalePrice=input("Enter wholesale price: ")
        retailPrice=input("Enter retailer price: ")
        pDes=input("enter the product description:")
        mContact=input("enter the contact no:")
        a=obj.productdetails(productId,productName,distributorName,manufacturingYear,wholesalePrice,retailPrice,pDes,mContact)
        result=collection.insert_many(productlist)
        print(result.inserted_ids)
        
        
    if option==2:
        result=collection.find()
        for i in result:
           print(i)
    if option==3:
        pc=input("enter product name: ")
        x=collection.find({"productName":pc})
        for i in x:
            print(i)

    if option==4:
        y=collection.find({},{"productId":0}) 
        for i in y:
            delete.append(i)
        print(delete)

    if option==5:
        pname=input("enter product name to delete: ")
        de=collection.delete_one({"productName":pname})
        print(de)
        de1=collection.delete_many({"productName": {"$regex":"^p"}})
        print(de1)


    if option==6:
            break
