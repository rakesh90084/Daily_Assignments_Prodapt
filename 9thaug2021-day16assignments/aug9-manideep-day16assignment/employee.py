import pymongo


client=pymongo.MongoClient("mongodb://localhost:27017/")   #establishing a connection
mydatabase=client['employeeDb']    #database
collection_name=mydatabase['employees']

employeelist=[]
employeefetchlist=[]
empid=[]
class Employee:
        
    def addemployeedetail(self,name,designation,salary,address,mobile):
        
        dict1={"name":name,"designation":designation,"salary":salary,"address":address,"mobile":mobile}
        employeelist.append(dict1)

obj1=Employee()
    
while(True):
        print("1.Add employee:")
        print("2.veiw employee:")
        print("3. search an employee by name")
        print("4. delete employee")
        print("5. by using employee id")
        print("6.exit")
        choice=int(input("enter your choice"))
        if choice==1:
            name=input("enter your name")
            designation=input("enter your designiation:")
            salary=input("enter the salary:")
            address=input("enter the address:")
            mobile=input("enter the mobile:")
            obj1.addemployeedetail(name,designation,salary,address,mobile)
            result=collection_name.insert_many(employeelist)
            print(result.inserted_ids)

        if choice==2:
            result=collection_name.find()
            for i in result:
                employeefetchlist.append(i)
            print(employeefetchlist)

        if choice==3:
            n1=input("enter name: ")
            result2=collection_name.find({"name":n1})
            for i in result2:

                print(i)

        if choice==4:
        
            de=collection_name.delete_many({"name": {"$regex":"^m"}})
            print(de)

        if choice==5:
            x=collection_name.find({},{"_name":0}) #filter
            for i in x:
               empid.append(i)
            print(empid)


        if choice==6:

           break
                
    

 
