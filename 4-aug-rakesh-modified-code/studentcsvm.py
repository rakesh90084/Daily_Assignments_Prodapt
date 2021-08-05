import re,csv,logging
try:
    header=["total","name","rollno","admin","english","hindi","maths","science","social"]
    studentlist=[]
    class StudentDetails:
        def init(self,name,rollno,admin,english,hindi,maths,science,social):
           self.name=name
           self.rollno=rollno
           self.admin=admin
           self.english=english
           self.hindi=hindi
           self.maths=maths
           self.science=science
           self.social=social
        def addstudentdetail(self,name,rollno,admin,english,hindi,maths,science,social):
           totalmarks=english+hindi+maths+science+social
           dict1={"total":totalmarks,"name":name,"rollno":rollno,"admin":admin,"english":english,"hindi":hindi,"maths":maths,"science":science,"social":social} 
           studentlist.append(dict1)
    def validate(name):
        valname=re.search("[A-Z]{1}[^A-Z]{0,25}$",name)
        # valrollno=re.search("[0-9]{0,7}$",rollno)
        # valadmin=re.search("[0-9]{0,5}$",admin)
        if valname:
           return True
        else:
           return False
    obj=StudentDetails()        
    while True:
        print("1.Add student")
        print("2.Search student")
        print("3.Display")
        print("4.Ranking")
        print("5.Save") 
        print("6.Exit")
    
        choice=int(input("Enter your choice : "))
 
    # obj=StudentDetails()
        if choice==1:
     
            name=input("Enter the name : ")
            rollno=int(input("Enter the roll no : "))
       
            admin=int(input("Enter the admission no : "))
            english=int(input("Enter the marks of English : "))
            hindi=int(input("Enter the marks of Hindi : "))
            maths=int(input("Enter the marks of maths : "))
            science=int(input("Enter the marks of Science : "))
            social=int(input("Enter the marks of Social : "))
            if validate(name)==True:
                obj.addstudentdetail(name,rollno,admin,english,hindi,maths,science,social)
            else:
                logging.warning("Wrong details")
                break
        if choice==3:
            print(studentlist)
        if choice==2:
            srollno=int(input("Enter the rollno to search : "))
            print(list(filter(lambda i:i["rollno"]==srollno,studentlist)))
        if choice==4:
            print(sorted(studentlist,key=lambda i:i["total"],reverse=True))
        if choice ==5:
            with open('student.csv','w+',encoding='UTF8',newline='') as s:
                writer = csv.DictWriter(s,fieldnames=header)
                writer.writeheader()
                writer.writerows(studentlist)    
        if choice==6:
            break
except:
    logging.error("Something went wrong")      
finally:
    print("THANK YOU")          