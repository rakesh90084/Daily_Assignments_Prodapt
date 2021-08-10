import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/") #establishing a connection
mydatabase=client['EmployDb']          #database
collection_name=mydatabase['Employ']  #collecclass 

employeelist=[]
Employeefetch=[]
idv=[]


class employe:
    def addemployee(self,name,adress,phnno,designation,salary,companyname):
        dic={"name":name,"adress":adress,"phno":phnno,"designation":designation,"salary":salary,"companyname":companyname}
        employeelist.append(dic) 

obj1=employe()    
while(True): 
    print("1 Add employee :")
    print("2 view employee:")
    print("3. search an employee by name")
    print("4. delete employee")
    print("5. by using employee id")
    print("5 exit")
    choice=int(input("enter a option:"))
   
    if choice==1:
        name=input("enter employee name:")
        adress=input("enter adress:")
        phnno=int(input("enter admino no:"))
        designation=input("enter the designation :")
        salary=int(input("enter the salary:"))
        companyname=input("enter companyname:")
        obj1.addemployee(name,adress,phnno,designation,salary,companyname)
        result=collection_name.insert_many(employeelist)
        print(result.inserted_ids)

    if choice==2:
        result=collection_name.find()
        for i in result:
            Employeefetch.append(i)
        print(Employeefetch)

    if choice==3:
        n=input("enter name: ")
        result2=collection_name.find({"name":n})
        for i in result2:
            print(i)

    if choice==4:
        #na=input("enter the name")
        # d=collection_name.delete_one({"name":na})
        # print(d)
        d1=collection_name.delete_many({"name": {"$regex":"^K"}})
        print(d1)

    if choice==5:
        y=collection_name.find({},{"_name":0}) #filter
        for i in y:
            idv.append(i)
        print(idv)


    if choice==6:
        break