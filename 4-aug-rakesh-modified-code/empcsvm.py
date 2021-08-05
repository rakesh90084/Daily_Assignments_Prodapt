empdict={}
from os import name
import re,collections,time,csv,logging
try:
    headerContent=["id","name","designation","salary","address","pincode","addedOn"]
    def getdatetime():
        time1=time.localtime()
        currentime=time.strftime("%Y-%m-%d %H:%M:%S ",time1)
        return currentime
    def addEmployee():
        id=input("Enter the E-id :")
        name=input("Enter the name: ")
        designation=input("Enter the Designation: ")
        salary=input("Enter the salary :")
        address=input("Enter the address : ")
        pincode=input("Enter the pincode : ")
        timedate1=getdatetime()
        dict1={"id":id,"name":name,"designation":designation,"salary":salary,"address":address,"pincode":pincode,'addedOn':timedate1}
        return dict1
    def validate(dict1):
        valname=re.search("[A-Z]{1}[^A-Z]{0,25}$",dict1["name"])
        valsalary=re.search("[0-9]{0,7}$",dict1["salary"])
        if valname and valsalary:
            return True
        else:
            return False

    while(1):
        print("1. Add employee")
        print("2. View employee")
        print("3. Check salary")
        print("4. Save")
        print("5.Exit")
        option=int(input("Enter your option :"))
        if option==1:
           n=int(input("Enter the number of employees :"))
           for i in range(0,n):
              a=addEmployee()
              if len(empdict)==0:
                 empdict=collections.ChainMap(a)
              else:
                 empdict=empdict.new_child(a)
        if option==2:
            print(empdict.maps)
        if option==3:
            sal=int(input("Enter the Salary to check: "))
            for i in empdict.maps:
               if int(i['salary'])>=sal:
                  print(i)  
        if option==4:
            with open("emp.csv","w+",encoding="UTF8",newline='')as f:
               writer=csv.DictWriter(f,fieldnames=headerContent)
               writer.writeheader()
               writer.writerows(empdict.maps)               
        if option==5:
            break
except:
    logging.error("Something is wrong")            
finally:
    print("THANK YOU")
        