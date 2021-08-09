import pymongo,logging
# client = pymongo.MongoClient("mongodb://localhost:27017/")
try:
    client = pymongo.MongoClient("mongodb+srv://Gulshan06:Gullu2132@cluster0.8ikox.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    mydatabase= client['EmployeeDb']
    Collection_name =mydatabase['Employee']
    list=[]
    class BookDetails:
        def addbookdetails(self,name,Address,phonenumber,designation,Company_name,Salary):
            dict1={"Empname":name,"Address":Address,"phonenumber":phonenumber,"designation":designation,"Company_name":Company_name,"Salary":Salary,}
            list.append(dict1)
    obj1=BookDetails()
    while(True): 
        print("1.Add employee")
        print('2.View emp')
        print('3.search emp by name')
        print("4.delete emp name")
        print("5.update emp")
        print("6.Break")
        choice=int(input("enter your choice:"))
        if choice==1:
            name=input("enter the name - ")
            Address=input("enter the Address - ")
            phonenumber=input("enter the phonenumber - ")
            designation=input("enter the designation - ")
            Company_name=input("enter the company name - ")
            Salary=int(input('enter Salary '))
            obj1.addbookdetails(name,Address,phonenumber,designation,Company_name,Salary)
            result = Collection_name.insert_many(list)
            print(result.inserted_ids)
        if choice==2:
            result = Collection_name.find()
            l=[]
            for i in result:
                l.append(i)
            print(l)
        if choice==3:
            a = input('enter the emp name')
            result = Collection_name.find({"Empname":a})
            l = []
            for i in result:
                l.append(i)
            print(l)
        if choice==4:
            b = input('enter the emp name')
            result=Collection_name.delete_one({'Empname':b})
            print(result.deleted_count)
        if choice==5:
            result=Collection_name.update_one({'Empname':'Gullu'},{"$set":{"company_name":'tcs'}})
        if choice==6:
            break
except Exception:
    logging.error("something went wrong")
finally:
    print("Thank You!!")
# result = Collection_name.insert_many(list)
# print(result.inserted_ids)
