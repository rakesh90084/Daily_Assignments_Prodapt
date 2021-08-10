import logging,re
import collections,re,pymongo
logging.basicConfig(filename='employee.log',level=logging.DEBUG)
a=collections.deque()
client=pymongo.MongoClient("mongodb://localhost:27017/EmployeeDb")  
mydatabase=client["employeeDb"]
collection_name=mydatabase["employee"]
class EmployeeDetails:
    def addEmployeeDetails(self,name,address,mblno,destination,salary,companyname):
        dict={"name":name,"address":address,"mblno":mblno,"destination":destination,"salary":salary,"companyname":companyname}
        a.append(dict)
obj=EmployeeDetails()

def validate(vname,vmblno,vsalary):
    name1=re.match("([a-z]+)([a-z]+)*([a-z]+)*$",vname)
    print(name1)
    mblno1=re.search("^91[6-9]\d{9}$",vmblno)
    print(mblno1)
    salary1=re.match("[0-9]{0,7}$",vsalary)
    print(salary1)
    if name1 and mblno1 and salary1:
        return True
    else:
        return False

if(__name__=='__main__'):
    try:
        while(1):
            print("1.Add Employee")
            print("2.Store the database")
            print("3.Search an Employee")
            print("4.Delete the Employee")
            print("5.Update the Employee")
            print("6.Exit")

            option=int(input("Enter your option:"))
            if option==1:
                vname=input("Enter the name: ")
                address=input("Enter the address : ")
                vmblno=input("Enter the mbl no : ")
                vdestination=input("Enter the Designation: ")
                vsalary=input("Enter the salary :")
                companyname=input("Enter the Company name:")
                if validate(vname,vmblno,vsalary):
                    obj.addEmployeeDetails(vname,address,vmblno,vdestination,vsalary,companyname)
                    print(a)
                else:
                    logging.error("Check your name, mblno,destination and salary")

            if option==2:
                result=collection_name.insert_many(a)
                print(result)
                logging.info("Successfully!!! Store the data")
            
            if option==3:
                a=input("Search the Employee Name: ")
                r=collection_name.find({"name":a})
                for i in r:
                    print(i)
                    logging.info("Successfully!!! Search the data")
            
            if option==4:
                b=input("Delete Employee Name:")
                r=collection_name.delete_one({"name":b})
                print(r.deleted_count)
                logging.info("Successfully!!! delete the data")
            
            if option==5:
                c=input("Enter Update Employee Name:")
                update_destination=input("Enter the Update Employee Destination:")
                update_salary=input("Enter the Update Employee Salary:")        
                r=collection_name.update_one({"name":c},{"$set":{"destination":update_destination,"salary":update_salary}})
                print(r)
                logging.info("Successfully!!! update the data")

            if option==6:
                break

    except ValueError:
        logging.error("Please Check Value int or string")

    except IndexError:
        logging.error("Please Check Your Index")

    except Exception:
        logging.error("Something Went Wrong")

    finally:
        print("Äll Block Completed Successfully")