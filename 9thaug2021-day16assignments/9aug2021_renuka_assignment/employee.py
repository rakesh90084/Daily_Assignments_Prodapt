#CRUD-CREATE RETRIEVE UPDATE DELETE
import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
database=client['employeedb']
Collection_name=database['employees']

employeelist=[]
class employee:
    def addemployee(self,ename,eaddress,esalry,ephone,edesignation,company):
        edict={"ename":ename,"eaddress":eaddress,"esalary":esalary,"ephone":ephone,"edesignation":edesignation,"company":company}
        employeelist.append(edict)
obj=employee()
while(True):
    print("1.Add employee")
    print("2.view employee")
    choice=int(input("enter ur choice"))
    if choice==1:
        ename=input("enter the name")
        eaddress=input("enter the address")
        esalary=int(input("enter the salary"))
        ephone=int(input("enter the phone"))
        edesignation=input("enter the designation")
        company=input("enter the company")
        obj.addemployee(ename,eaddress,esalary,ephone,edesignation,company)
    if choice==2:
        print(employeelist)
        break
result=Collection_name.insert_many(employeelist)
print(result.inserted_ids)

