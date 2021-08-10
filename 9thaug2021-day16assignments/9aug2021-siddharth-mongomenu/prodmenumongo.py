import pymongo
import logging
import re
logging.basicConfig(filename="prodmongolog.log",level=logging.DEBUG)
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=client["productdb"]
prod=mydb["products"]
def validateProduct(pname,mcontact):
   
    val1=re.match(r'^([a-z]+)( [a-z]+)*( [a-z]+)*$',pname)
    val2=re.match("(0|91)?[-\s]?[6-9]\d{9}",mcontact)
    
    
    
    if val1 and val2:
        return True
    else:
        return False
class Product:
    def pdetails(self,pcode,pname,myear,wprice,rprice,pdescp,mcontact):
        
        dict1={"pcode":pcode,"pname":pname,"myear":myear,"wprice":wprice,"rprice":rprice,"pdescp":pdescp,"mcontact":mcontact}
        return dict1
obj=Product()
while(True):
    print("1. Add product")
    print("2. view all product")
    print("3. Search product using pcode")
    print("4. update product using pcode")
    print("5. delete a product using pcode")
    
    try:
        c=int(input("Enter your choice: "))
        logging.info("User enterd correct choice")
    except ValueError:
        logging.error("something went wrong")
        
        break
    if c==1:
        while(True):

            
            pname=input("Enter pname")
            mcontact=input("Enter mcontact")
            if validateProduct(pname,mcontact):
                pcode=input("Enter pcode: ")

                myear=input("Enter myear")
                wprice=input("Enter wprice")
                rprice=input("Enter rprice")
                pdescp=input("Enter pdescp")
        
                a=obj.pdetails(pcode,pname,myear,wprice,rprice,pdescp,mcontact)
                result=prod.insert_one(a)
                print(result.inserted_id)
            else:
                logging.error("Product name,id,conatct not in proper format")
                print("Enter valid details")
                continue
            break
        
        
    if c==2:
        result1=prod.find()
        for i in result1:
            print(i)
    if c==3:
        n=input("Enter pcode: ")
        r=prod.find({"pcode":n})
        for i in r:

            print(i)
    if c==4:
        pcode=input("enter product code whos record to change")
        pname=input("enter product name record to change")
        pdescp=input("enter product description record to change")

        res=prod.update_one({"pcode":pcode}, {"$set":{"pname":pname,"pdescp":pdescp} })

    if c==5:
        n2=input("Enter pcode:")
        r2=prod.delete_one({"pcode":n2})