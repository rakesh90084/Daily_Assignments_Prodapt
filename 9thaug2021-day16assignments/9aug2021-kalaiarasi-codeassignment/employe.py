import pymongo
import re
import logging
try:    
  
  
    client=pymongo.MongoClient("mongodb://localhost:27017/EmployeeDb")
    mydatabase=client['EmployeeDb']
    collection_name=mydatabase['employees']

    elist=[]
    employlist=[]  
    def validation(name):
            vname=re.search("^[A-Za-z]{2,25}$",name)
            if vname:
                return True
            else:
                return False  
    class Employee:
        def adddetail(self,name,designation,salary,address):   
            dict1={"name":name,"designation":designation,"salary":salary,"address":address}
            employlist.append(dict1)
            r=collection_name.insert_one(dict1)



    obj=Employee()
    if(__name__=='__main__'):
        while(1):
            print("1. add employee")
            print("2. view")
            print("3. search")
            print("4. delete document using name")
            print("5. update")
            print("6. exit")
            choice=int(input("Enter your choice :"))
            if choice==1:
                name=input("enter the name: ")
                designation=input("enter the Designation: ")
                salary=input("Enter the salary :")
                address=input("Enter the address : ")
                x=validation(name)
                if x:
                    obj.adddetail(name,designation,salary,address)
                    
                else:
                    logging.error("please enter data")
                   
            if choice==2:
                r=collection_name.find()
                for i in r:
                    elist.append(i)
                print(elist)

            if choice==3:
                r=collection_name.find({"name":"kalai"})
                for i in r:
                    print(i)

            if choice==4:
                d=input("enter name:")
                results=collection_name.delete_many({"name":d})
                print("deleted")

            if choice==5:
                n=input("enter the name ")
                addre=input("enter the address")
                results=collection_name.update_one({"name":n},{"$set":{"address":addre}})
                print("updated")

            if choice==6:  
                break

except:
    logging.error("something went wrong")