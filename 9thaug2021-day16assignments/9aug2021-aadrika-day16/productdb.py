import pymongo ,logging,re
import time
client=pymongo.MongoClient("mongodb://localhost:27017/") #esttablishin connection
mydb=client['ProductDB']#database
collection_name=mydb['products']#collection

logging.basicConfig(filename='error2.log',level=logging.DEBUG)
def validation_of_Product(name,code,mob):
   
    val1=re.match("([a-z]+)([a-z]+)(\s)([a-z]+)$",name)
    val2=re.match("[0-9]{0,9}$",mob)
    val3=re.match("[0-9]{0,7}$",code)
    
    try:
        if val1 and val2 and val3:
            return True
        else:
            return False
    except:
        logging.error("Some data is not validated please try again later")
    
    finally:
        logging.info("All executed successfuly")

def getDateTime():
    time1=time.localtime()
    currenttime=time.strftime("%Y-%m-%d %H:%M:%S",time1)
    return currenttime


class Product:
    def addpro(self,name,pcode,descp,manufacturer,phone,wholep,retailp,time):
        dictionary1={"product name":name,"product code":pcode,"description":descp,"manufacturer":manufacturer,"manufacturer phone number":phone,"wholesale price":wholep,"retail price":retailp,"addedon":time}
        return dictionary1
pro=Product()

li=[]
li2=[]
while(True):
    print("1. Add product")
    print("2. view product")
    print("3. search product by code")
    print("4. delete product using code")
    print("5. updation")
    print("6. exit")
    c=int(input("enter your choice: "))
    if c==1:
        while(True):
            pname=input("Enter the product name:")
            pcode=input("Enter the product code:")
            manfp=input("Enter the manifacturer number ")
            if validation_of_Product(pname,code,manfp):
        
                des=input("Enter the product description: ")
                manf=input("Enter the manufacturer")
                
                wholesale=input("Enter the whole sale price ")
                retp=input("Enter the retail price ")
                timedate=getDateTime()
                res=pro.addpro(pname,pcode,des,manf,manfp,wholesale,retp,timedate)
                collection_name.insert_one(res)
    if c==2:
        res=collection_name.find()
        for i in res:
            li.append(i)
        print(li)    
    if c==3:
        code=input("enter product code to search :")
        res=collection_name.find({"product code":code})
        for i in res:
            li2.append(i)
        print(li2)
    if c==4:
        code=input("enter product code to delete :")
        res=collection_name.delete_one({"product code":code})
        print(res.deleted_count)
        print("productdleted")
    if c==5:
        pcode=input("enter product code whos record to change")
        prname=input("enter product name record to change")
        des=input("enter product description record to change")

        res=collection_name.update_one({"product code":pcode}, {"$set":{"product name":prname,"description":des} })
    if c==6:
        break