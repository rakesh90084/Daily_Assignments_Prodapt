import pymongo,logging
try:
    client = pymongo.MongoClient("mongodb+srv://Gulshan06:Gullu2132@cluster0.8ikox.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    mydatabase= client['Productdb']
    Collection_name =mydatabase['products']
    productlist=[]
    class ProductDetails:
        def addproductdetails(self,productcode,productname,discription,Hprice,manufacturername,manufacturingyear,Rprice):
            dict1={"productcode":productcode,"productname":productname,"discription":discription,"Hprice":Hprice,"manufacturername":manufacturername,"manufacturingyear":manufacturingyear,"Rprice":Rprice,}
            productlist.append(dict1)
    obj1=ProductDetails()
    while(True):
        print("1.Add Products")
        print("2.insert and View all products")
        print("3.Search a product")
        print("4.Delete the data")
        print("5.Update the data")
        print("6.Break")
        choice=int(input("enter your choice:"))
        if choice==1:
            productcode=int(input('enter product code '))
            productname=input("enter the product name - ")
            discription=input("enter the description of product - ")
            Hprice=input("enter the price - ")
            manufacturername=input("enter the manufacturer name - ")
            manufacturingyear=input("enter year -")
            Rprice=input("enter the Rprice ")
            obj1.addproductdetails(productcode,productname,discription,Hprice,manufacturername,manufacturingyear,Rprice)
            result = Collection_name.insert_many(productlist)
            print(result.inserted_ids)
        if choice==2:
            result = Collection_name.find()
            l=[]
            for i in result:
                l.append(i)
            print(l)
        if choice==3:
            a = int(input('enter the product name'))
            result = Collection_name.find({"productcode":a})
            l = []
            for i in result:
                l.append(i)
            print(l)
        if choice==4:
            b = int(input('enter the product code'))
            result=Collection_name.delete_one({'productcode':b})
            print(result.deleted_count)
        if choice==5:
            result=Collection_name.update_one({'productcode':123},{"$set":{"productname":'lifee'}})
        if choice==6:
            break
except Exception:
    logging.error("something went wrong ")
finally:
    print("Thank you!!")
