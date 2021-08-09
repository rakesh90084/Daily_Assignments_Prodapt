import pymongo,logging
# try:
client = pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase= client['ProductDb']
Collection_name =mydatabase['products']
productlist=[]
class Product_Details:
    def addproductdetails(self,product_code,product_name,discription,Wprice,manufacturer_name,manufacturing_year,Retail_price):
        dict1={"product_code":product_code,"product_name":product_name,"discription":discription,"Wprice":Wprice,"manufacturer_name":manufacturer_name,"manufacturing_year":manufacturing_year,"Retail_price":Retail_price,}
        productlist.append(dict1)
obj1=Product_Details()
while(True):
    print("1.Add Products")
    print("2.insert and View all products")
    print("3.Search a product")
    print("4.Delete the data")
    print("5.Update the data")
    print("6.Break")
    choice=int(input("enter your choice:"))
    if choice==1:
        product_code=int(input('enter product code :'))
        product_name=input("enter the product name : ")
        discription=input("enter the description of product : ")
        Wprice=input("enter the Whole sale price : ")
        manufacturer_name=input("enter the manufacturer name : ")
        manufacturing_year=input("enter year :")
        Retail_price=input("enter the Retailer price : ")
        obj1.addproductdetails(product_code,product_name,discription,Wprice,manufacturer_name,manufacturing_year,Retail_price)
        result = Collection_name.insert_many(productlist)
        print(result.inserted_ids)
    if choice==2:
        result = Collection_name.find()
        l=[]
        for i in result:
            l.append(i)
        print(l)
    if choice==3:
        x = input('enter the product name :-')
        result = Collection_name.find({"product_name":x})
        l = []
        for i in result:
            l.append(i)
        print(l)
    if choice==4:
        y = input('enter the product code :-')
        result=Collection_name.delete_one({'product_name':y})
        print(result.deleted_count)
    if choice==5:
        result=Collection_name.update_one({'product_code':2601},{"$set":{"product_name":'Dettol'}})
    if choice==6:
        break
# except Exception:
#     logging.error("Wrong Input")
# finally:
#     print("Thank you!!")