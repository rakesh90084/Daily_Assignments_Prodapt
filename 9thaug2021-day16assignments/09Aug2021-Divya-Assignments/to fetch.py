import pymongo
#client = pymongo.MongoClient("mongodb://localhost:27017")
client = pymongo.MongoClient("mongodb+srv://chediv_1998:Basketball9@cluster0.8vz0p.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

mydb =client['EmployeesDB']
Collection_name = mydb['Employees']
# result = Collection_name.find({'Companyname': 'prodapt'},{'_id':0})
# Emp_details=[ ]
# for i in result:
#     Emp_details.append(i)
# print(Emp_details)
# result = Collection_name.find({'Companyname':{"$regex":"^p"}},{'_id':0})
# Emp_details=[ ]
# for i in result:
#     Emp_details.append(i)
# print(Emp_details)
# result = Collection_name.find({'Address':{"$gt":"y"}},{'_id':0})
# Emp_details=[ ]
# for i in result:
#     Emp_details.append(i)
# print(Emp_details)
# result = Collection_name.delete_one({'Address':{"$gt":"y"}})
# print(result)
Name1 = input("Enter Employee name: ")
Address1 = input("Enter Employee Address: ")
Phno1 = int(input("Enter Employee Phno: "))
Designation1 = input("Enter designation: ")
Salary1 = int(input("Enter Employee salary: "))
Company_name1 = input("Enter Employee company name: ")
result = Collection_name.update_one({},{"$set":{"Name":Name1,"Address":Address1,"Phno":Phno1,"Desgination":Designation1,"Salary":Salary1,"Companyname":Company_name1}})
print(result)