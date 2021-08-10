import pymongo
client = pymongo.MongoClient("mongodb+srv://chediv_1998:Basketball9@cluster0.8vz0p.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

mydb =client['HostelDB']
Collection_name = mydb['Hostel']

Hostel_details= []
class Hostel:
    def add_details(self,Name,Father_name,Address,Mobile_no):
        self.Name = Name
        self.Father_name = Father_name
        self.Address = Address
        self.Mobile_no = Mobile_no
        details = {"Name":Name,"Father_Name":Father_name,"Address":Address,"Mobile_no":Mobile_no}
        Hostel_details.append(details)
HD = Hostel()

while(True):
    print("1.ADD DETAILS")
    print("2.DISPLAY")
    print("3.SEARCH BY NAME")
    print("4.To DELETE")
    print("5.To UPDATE")
    choice = int(input("enter your choice: "))

    if choice == 1:
        Name = input("Enter name: ")
        Father_name = input("Enter father name: ")
        Address = input("Enter address: ")
        Mobile_no = int(input("Enter mobile no: "))
        HD.add_details(Name,Father_name,Address,Mobile_no)
    if choice == 2:
        print(Hostel_details)
        Collection_name .insert_many(Hostel_details)
    if choice == 3:
        n= input("enter name: ")
        result = Collection_name.find({"Name": n})
        for i in result:
            print(i)
    if choice == 4:
        Mobile = int(input("Enter mobile no: "))
        result = Collection_name.delete_many({"Mobile_no":Mobile})
        print(result.deleted_count)
    if choice == 5:
        Name1 = input("Enter name: ")
        Father_name1 = input("Enter father name: ")
        Address1 = input("Enter address: ")
        Mobile_no1 = int(input("Enter mobile no: "))
        result = Collection_name.update_one({"Name":'Divya'},{"$set":{"Name":Name1,"Father_Name":Father_name1,"Address":Address1,"Mobile_no":Mobile_no1}})
        break



        