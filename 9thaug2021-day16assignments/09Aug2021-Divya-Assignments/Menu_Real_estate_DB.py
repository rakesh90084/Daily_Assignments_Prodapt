import pymongo
client = pymongo.MongoClient("mongodb+srv://chediv_1998:Basketball9@cluster0.8vz0p.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

mydb =client['RealEstateDB']
Collection_name = mydb['RealEstate']

Real_details= []
class Real_Estate:
    def add_details(self,House_no,Flat_no,Square_feet,Model,Area):
        self.House_no = House_no
        self.Flat_no = Flat_no
        self.Square_feet = Square_feet
        self.Model = Model
        self.Area = Area
        details = {"House_no":House,"Flat_no":Flat,"Square_feet":Square,"Model":Model,"Area":Area}
        Real_details.append(details)
RD = Real_Estate()

while(True):
    print("1.ADD DETAILS")
    print("2.DISPLAY")
    print("3.SEARCH BY AREA NAME")
    print("4.To DELETE")
    print("5.To UPDATE")
    choice = int(input("enter your choice: "))

    if choice == 1:
        House = int(input("Enter house no: "))
        Flat = int(input("Enter a Flat no: "))
        Square = int(input("Enter square feet: "))
        Model = input("Enter model of house: ")
        Area = input("Enter area name: ")
        RD.add_details(House,Flat,Square,Model,Area)
    if choice == 2:
        print(Real_details)
        Collection_name .insert_many(Real_details)
    if choice == 3:
        n= input("enter area name: ")
        result = Collection_name.find({"Area": n})
        for i in result:
            print(i)
    if choice == 4:
        hn = int(input("Enter House_no: "))
        result = Collection_name.delete_many({"House_no":hn})
        print(result.deleted_count)
    if choice == 5:
        s = int(input("Enter Square feet: "))
        result = Collection_name.update_one({'Area':'Anna nagar'},{"$set":{"Square_feet":s}})
        break



        