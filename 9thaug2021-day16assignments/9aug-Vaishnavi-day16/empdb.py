import pymongo,logging

# try:
client = pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase= client['EmployeeDb']
Collection_name =mydatabase['Employee']
list=[]
class BookDetails:
    def addbookdetails(self,name,Address,phone_number,designation,Company_name,Salary):
        dict1={"Employee_name":name,"Address":Address,"phone_number":phone_number,"designation":designation,"Company_name":Company_name,"Salary":Salary,}
        list.append(dict1)
obj1=BookDetails()
while(True): 
    print("1.Add employee")
    print('2.View employee')
    print('3.Search employee')
    print('4.Delete employee')
    print('5.Update employee')
    print('6.Exit')
    choice=int(input("enter your choice:"))
    if choice==1:
        name=input("enter the name - ")
        Address=input("enter the Address - ")
        phone_number=input("enter the phone number - ")
        designation=input("enter the designation - ")
        Company_name=input("enter the company name - ")
        Salary=int(input('enter Salary '))
        obj1.addbookdetails(name,Address,phone_number,designation,Company_name,Salary)
        result = Collection_name.insert_many(list)
        print(result.inserted_ids)
    if choice==2:
        result = Collection_name.find()
        l=[]
        for i in result:
            l.append(i)
        print(l)
    if choice==3:
        a = input('enter the employee name')
        result = Collection_name.find({"Employee_name":a})
        l = []
        for i in result:
            l.append(i)
        print(l)
    if choice==4:
        b = input('enter the employee name')
        result=Collection_name.delete_one({'Employee_name':b})
        print(result.deleted_count)
    if choice==5:
        result=Collection_name.update_one({'Employee_name':'Vaishnavi'},{"$set":{"company_name":'Google'}})
    if choice==6:
        break
# except Exception:
#     logging.error("Something went wrong")
# else:
#     print("Your program completed Successfully")
# finally:
#     print("Thank You!!")
