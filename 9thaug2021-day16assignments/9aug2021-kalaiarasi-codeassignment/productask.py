import pymongo
import logging
import re
try:   
  
  
    client=pymongo.MongoClient("mongodb://localhost:27017/ProductDb")
    mydatabase=client['ProductDb']
    collection_name=mydatabase['products']

    prolist=[]
    productlist=[]  
    def validation(name,manufactdate):
                vname=re.search("^[A-Za-z]{2,25}$",name)
                vyear=re.search("^[0-9]{4}",manufacyear)
                if vname and vyear:
                    return True
                else:
                    return False   
    class Product:
        def addproduct(self,code,name,description,distributername,manufacyear,contact,wholesaleprice,retailprice):   
            
            dict1={"code":code,"name":name,"description":description,"distributername":distributername,"manufacyear":manufacyear,"contact":contact,"wholesaleprice":wholesaleprice,"retailprice":retailprice}
            productlist.append(dict1)
            r=collection_name.insert_one(dict1)



    obj=Product()
    if(__name__=='__main__'):
        while(1):
            print("1. add product")
            print("2. view ")
            print("3. search")
            print("4. find")
            print("5. update")
            print("6. delete document using code")
            print("7. exit")
            choice=int(input("Enter your choice :"))
            if choice==1:
                code=input("enter code:")
                name=input("enter the name: ")
                description=input("enter the Description: ")
                distributername=input("Enter the distributor name :")
                manufacyear=input("Enter the manufacyear : ")
                contact=input("Enter the contact : ")
                wholesaleprice=input("Enter the wholesaleprice : ")
                retailprice=input("Enter the retailprice: ")
                x=validation(name,manufacyear)
                if x:
                    obj.addproduct(code,name,description,distributername,manufacyear,contact,wholesaleprice,retailprice)
                else:
                    logging.error("please enter valid data")
  


            if choice==2:
                r=collection_name.find()
                for i in r:
                    prolist.append(i)
                print(prolist)
                
            if choice==3:
                a=input("enter code:")
                r=collection_name.find({"code":a})
                for i in r:
                    print(i)

            if choice==4:
                r=collection_name.find({"name":{"$regex":"^g"}},{"_id":0})
                for i in r:
                    print(i)

            if choice==5:
                c=input("enter the code ")
                newname=input("enter the name")
                results=collection_name.update_one({"code":c},{"$set":{"name":newname}})
                print("updated")

            if choice==6:
                d=input("enter code to delte:")
                results=collection_name.delete_many({"code":d})
                print("deleted")


            if choice==7:  
                break

except:
    logging.error("something went wrong")