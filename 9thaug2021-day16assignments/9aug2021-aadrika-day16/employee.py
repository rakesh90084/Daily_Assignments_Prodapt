import pymongo

import time,re,logging
client=pymongo.MongoClient("mongodb://localhost:27017/") #esttablishin connection
mydb=client['EmployeeDB']#database
collection_name=mydb['employess']#collection
logging.basicConfig(filename='error2.log',level=logging.DEBUG)
def validation_of_Employee(name,mob):
   
    val1=re.match("([a-z]+)([a-z]+)(\s)([a-z]+)$",name)
    val2=re.match("[0-9]{0,9}$",mob)
    
    try:
        if val1 and val2 :
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


class Employee:
    def adddetails(self,name,salary,address,phone,company,time):
        dictionary1={"name":name,"salary":salary,"address":address,"phone number":phone,"company name":company,"addedon":time}
        return dictionary1
emp=Employee()

li=[]
li2=[]
while(True):
    print("1. Add employee")
    print("2. view")
    print("3. search em by name")
    print("4. delete by nam")
    print("5. updation")
    print("6. exit")
    c=int(input("enter your choice: "))
    if c==1:
        while(True):
            name=input("Enter the name:")
            phone=input("Enter the phone no ")
            if validation_of_Employee(name,phone):
                salary=input("Enter the salary:")
                addresss=input("Enter the address: ")
                
                compname=input("Enter the company name ")
                timedate=getDateTime()
                res=emp.adddetails(name,salary,addresss,phone,compname,timedate)
                collection_name.insert_one(res)
            else:
                logging.error("phone number and name are invalid")
                print("enter valid info")
                continue
            break
    if c==2:
        res=collection_name.find()
        for i in res:
            li.append(i)
        print(li)    
    if c==3:
        name=input("enter employee to search :")
        res=collection_name.find({"name":name},{'_id':0})
        for i in res:
            li2.append(i)
        print(li2)
    if c==4:
        name=input("enter employee to search :")
        res=collection_name.delete_one({"name":name})
        print(res.deleted_count)
        print("entry deleted successfully")
    if c==5:
        name=input("enter names whos record to change")
        phone=input("enter phone record to change")
        add=input("enter address record to change")

        res=collection_name.update_one({"name":name},{"$set":{"phone number":phone,"address":add}})
    if c==6:
        break
        



            
    