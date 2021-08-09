import pymongo
import logging
import re
logging.basicConfig(filename="prodmongolog.log",level=logging.DEBUG)
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=client["employeedb"]
employees=mydb["Employes"]
def validateemployee(name,phone):
   
    val1=re.match(r'^([a-z]+)( [a-z]+)*( [a-z]+)*$',name)
    val2=re.match("(0|91)?[-\s]?[6-9]\d{9}",phone)
    
    if val1 and val2 :
        return True
    else:
        return False
class Employee:
    def empdetails(self,name,address,phone,designation,salary,companyname):
        
        dict1={"name":name,"address":address,"phone":phone,"designation":designation,"salary":salary,"companyname":companyname}
        return dict1
obj=Employee()
while(True):
    print("1. Add employee")
    print("2. view all employee")
    print("3. Search an employee using name")
    print("4. update an employee using name")
    print("5. delete an employee using name")
    print("6. Exit")
    try:
        choice=int(input("Enter your choice: "))
        logging.info("User enterd correct choice")
    except ValueError:
        logging.error("something went wrong")
        break
    if choice==1:
        while(True):


            name=input("Enter your name: ")
            phone=input("Enter your phone: ")
            if validateemployee(name,phone):

                address=input("Enter your address: ")
            
                designation=input("Enter your designation: ")
                salary=input("Enter your salary: ")
                companyname=input("Enter your company: ")
                a=obj.empdetails(name,address,phone,designation,salary,companyname)
                result=employees.insert_one(a)
                print(result.inserted_id)
            else:
                print("Phone or name is not in correct format")
                logging.error("User entered in wrong format")
                continue
            break