import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
database=client['employeedb']
Collection_name=database['employees']

employeelist=[]
employeefetchlist=[]
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
        # rrint(resuesult=Collection_name.insert_many(employeelist)
        # plt.inserted_ids)
    if choice==2:
        #result=Collection_name.find({"ename":"renuka"},{"_id":0})#use find_one if we want to fetch particular data and also no need for 'forloop'
        result=Collection_name.update_one({"esalary":25000},{"$set":{"ename":"raju"}})
        # print(result)
        # for i in result:                         #_id is not in dict
        #     employeefetchlist.append(i)
        # print(employeefetchlist)
        result=Collection_name.insert_many(employeelist)
        print(result.inserted_ids)

       

        
    

