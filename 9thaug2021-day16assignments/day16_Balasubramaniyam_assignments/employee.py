import pymongo,collections,re,logging
logging.basicConfig(filename='employee.log',level=logging.DEBUG)

client=pymongo.MongoClient("mongodb://localhost:27017/")
#client=pymongo.MongoClient("mongodb+srv://Balu862:balu1234@cluster0.ug6wk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

mydata=client["Employeedb"]
employeecollection=mydata["Employee"]


employeedeques=collections.deque()
def validation(name,address,phone):
    valname=re.search("^[A-Z]{1}[a-z]{0,25}$",name)
    valaddress=re.search("^[A-Za-z]{0,25}$",address)
    valnumber=re.search("^(\+91)[6-9]\d{9}$",phone)
    if valname and valaddress and valnumber:
        return True
print(employeedeques)
class Employee:
    def addEmployee(self,name,address,phone,designation,company_name):
        if validation(name,address,phone)==True:
            dict1={"name":name,"address":address,"phone":phone,"designation":designation,"company_name":company_name}
            employeedeques.append(dict1)
            result=employeecollection.insert_many(employeedeques)
            print(result)
obj1=Employee()
try:
    while(1):
        print("1) add employee")
        print("2) display")
        print("3) seach by name :")
        print("4) edit : ")
        print("5) exit : ")
        option=int(input("enter the option : "))
        if option==1:
            name=input("enter the name: ")
            address=input("enter the address: ")
            phone=input("enter the phone: ")
            designation=input("enter the designation: ")
            company_name=input("enter the company_name: ")
            obj1.addEmployee(name,address,phone,designation,company_name)
        if option==2:
            result=employeecollection.find()
            print(result)
            for i in result:
                print(i)
        if option==3:
            employeelist=[]
            names=input("enter the name :")
            result=employeecollection.find({"name":names})
            print(result)
            for i in result:
                print(i)
                employeelist.append(i)
            print(employeelist)
        if option==4:
            names=input("Enter the Employee name you have to update")
            addresses=input("Enter address : ")
            designations=input("Enter Designation : ")
            result=employeecollection.update_one({"name":names},{"$set":{"address":addresses,"designation":designations}})
            print(result)
        if option==5:
            break
except:
    logging.error("something went wrong")

