import pymongo,logging
try:
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    mydatabase= client['Product1db']
    Collection_name =mydatabase['products1']
    productlist=[]
    class ProductDetails:
        def addproductdetails(self,productId,productName,discription,wPrice,manufacturerName,manufacturingyear,rPrice):
            dict1={"productId":productId,"productName":productName,"discription":discription,"wPrice":wPrice,"manufacturerName":manufacturerName,"manufacturingyear":manufacturingyear,"rPrice":rPrice}
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
            li=[]
            for i in result:
                li.append(i)
            print(li)
        if choice==3:
            p = int(input('enter the product name'))
            result = Collection_name.find({"productId":p})
            li= []
            for i in result:
                li.append(i)
            print(li)
        if choice==4:
            q= int(input('enter the product Id'))
            result=Collection_name.delete_one({'productId':q})
            print(result.deleted_count)

        if choice==5:
            result=Collection_name.update_one({'productid':"786"},{"$set":{"productname":"sanitizer"}})
        if choice==6:
            break
except:
    logging.error("something went wrong ")
finally:
    print("Thank you!")