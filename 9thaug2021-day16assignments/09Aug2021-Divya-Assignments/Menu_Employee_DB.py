import pymongo
#client = pymongo.MongoClient("mongodb://localhost:27017")
client = pymongo.MongoClient("mongodb+srv://chediv_1998:Basketball9@cluster0.8vz0p.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

mydb =client['EmployeesDB']
Collection_name = mydb['Employees']

Emp_details= []
class Employees:
    def add_details(self,Name,Address,Phno,Designation,Salary,Company_name):
        self.Name = Name
        self.Address = Address
        self.Phno = Phno
        self.Designation = Designation
        self.Salary = Salary
        self.Company_name = Company_name
        details = {"Name":Name,"Address":Address,"Phno":Phno,"Desgination":Designation,"Salary":Salary,"Companyname":Company_name}
        Emp_details.append(details)
ED = Employees()

while(True):
    print("1.ADD DETAILS")
    print("2.DISPLAY")
    print("3.SEARCH EMPLOYEE")
    print("4.To Delete")
    choice = int(input("enter your choice: "))

    if choice == 1:
        Name = input("Enter Employee name: ")
        Address = input("Enter Employee Address: ")
        Phno = int(input("Enter Employee Phno: "))
        Designation = input("Enter designation: ")
        Salary = int(input("Enter Employee salary: "))
        Company_name = input("Enter Employee company name: ")
        ED.add_details(Name,Address,Phno,Designation,Salary,Company_name)
    if choice == 2:
        print(Emp_details)
        Collection_name .insert_many(Emp_details)
    if choice == 3:
        name= input("enter employee name: ")
        result = Collection_name.find({'Companyname': 'prodapt'},{'_id':0})
        Emp_details=[ ]
        for i in result:
            Emp_details.append(i)
            print(Emp_details)
    if choice == 4:
        result = Collection_name.delete_one({'Address':{"$gt":"x"}})
        print(result.deleted_count)
        print(result)


        