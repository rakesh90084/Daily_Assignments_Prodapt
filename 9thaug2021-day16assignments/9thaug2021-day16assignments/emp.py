import pymongo,logging
try:
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    mydatabase= client['Employee1Db']
    Collection_name =mydatabase['Employee1']
    elist=[]
    class EmpDetails:
        def addempdetails(self,name,Address,phonenumber,designation,Company_name,Salary):
            dict1={"Empname":name,"Address":Address,"phonenumber":phonenumber,"designation":designation,"Company_name":Company_name,"Salary":Salary,}
            elist.append(dict1)
    obj1=EmpDetails()
    while(True): 
        print("1.Add employee")
        print("2.View emp")
        print("3.search emp by name")
        print("4.delete emp name")
        print("5.update emp")
        choice=int(input("enter your choice:"))
        if choice==1:
            name=input("enter the name - ")
            Address=input("enter the Address - ")
            phonenumber=input("enter the phonenumber - ")
            designation=input("enter the designation - ")
            Company_name=input("enter the company name - ")
            Salary=int(input('enter Salary '))
            obj1.addempdetails(name,Address,phonenumber,designation,Company_name,Salary)
            result = Collection_name.insert_many(elist)
            print(result.inserted_ids)
        if choice==2:
            result = Collection_name.find()
            li=[]
            for i in result:
                li.append(i)
            print(li)
        if choice==3:
            p = input('enter the emp name')
            result = Collection_name.find({"Empname":p})
            li = []
            for i in result:
                li.append(i)
            print(li)
        if choice==4:
            q= input('enter the emp name')
            result=Collection_name.delete_one({'Empname':q})
            print(result.deleted_count)
        if choice==5:
            result=Collection_name.update_one({'Empname':'Arif'},{"$set":{"company_name":'google'}})
            print(result)
        if choice==6:
            break
except:
    logging.error("something went wrong")