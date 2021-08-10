import re,collections,time,csv,logging,pymongo
empdict={}
employeelist=[]
try:
    client=pymongo.MongoClient("mongodb://localhost:27017/") #establishing connection
    mydatabase=client['employeeDb'] #database
    collection_name=mydatabase['employee']
    class emp:
        def addEmployee(self):
            name=input("Enter the name: ")
            designation=input("Enter the Designation: ")
            salary=input("Enter the salary :")
            address=input("Enter the address : ")
            pincode=input("Enter the pincode : ")
            dict1={"name":name,"designation":designation,"salary":salary,"address":address,"pincode":pincode}
            return dict1
    def validate(dict1):
        valname=re.search("[A-Z]{1}[^A-Z]{0,25}$",dict1["name"])
        valsalary=re.search("[0-9]{0,7}$",dict1["salary"])
        if valname and valsalary:
            return True
        else:
            return False
    obj=emp()
    while(1):
        print("1. Add employee")
        print("2.toretrive data from db")
        print("3.Search an employee")
        print("4.delete an employee")
        print("5.update  an employee salary")
        print("6.List of employees whoes name is start with greater than A")
        print("7. exit")
        option=int(input("Enter your option :"))
        if option==1:
            n=int(input("Enter the number of employees :"))
            for i in range(0,n):
                a=obj.addEmployee()
                if len(empdict)==0:
                    empdict=collections.ChainMap(a)
                else:
                    empdict=empdict.new_child(a)
        result=collection_name.insert_one(empdict)
        print(result.inserted_id)        
        
        if option==2:
            result=collection_name.find({},{"_id":0})
            for i in result:
                employeelist.append(i)
            print(employeelist)

        if option==3:
            Ename=input("Enter the Employee name to search:")
            result=collection_name.find({"name":Ename})
            for i in result:
                print(i)
            
        if option==4:
            Ename=input("Enter the Employee name that you want to delete")
            result=collection_name.delete_many({"name":Ename})
            print(result.deleted_count)
        if option==5:
            name=input("Enter the employee name where u want to update")
            salary=input("Enter salary update")
            result=collection_name.update_one({"name":name},{"$set":{"salary":salary}})
        
        if option==6:
            result1=collection_name.find({"name":{"$gt":"A"}},{"_id":0})
            for i in result1:
                print(i)
        if option==7:
            break

except:
    logging.error("unable to process")

