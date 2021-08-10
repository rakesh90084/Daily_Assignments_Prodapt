import pymongo
#client = pymongo.MongoClient("mongodb://localhost:27017")
client = pymongo.MongoClient("mongodb+srv://chediv_1998:Basketball9@cluster0.8vz0p.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

mydb =client['ProductsDB']
Collection_name = mydb['Products']

Pro_details= []
class Products:
    def add_details(self,P_code,P_name,Distribution_name,Retail_price,Whole_price,P_description,Contact_number,Manufacturer_year):
        self.P_code = P_code
        self.P_name = P_name
        self.Distribuition_name = Distribution_name
        self.Retail_price = Retail_price
        self.Whole_price = Whole_price
        self.P_description = P_description
        self.Contact_number = Contact_number
        self.Manufacturer_year = Manufacturer_year
        details = {"P_code":P_code,"P_name":P_name,"P_Distributiob":Distribution_name,"retail":Retail_price,"Whole":Whole_price,"P_desc":P_description,"Contact":Contact_number,"Manuf_date":Manufacturer_year}
        Pro_details.append(details)
PD = Products()

while(True):
    print("1.ADD DETAILS")
    print("2.DISPLAY")
    print("3.SEARCH BY PRODUCTS CODE")
    print("4.To DELETE")
    print("5.To UPDATE")
    choice = int(input("enter your choice: "))

    if choice == 1:
        P_code = int(input("Enter p code: "))
        P_name = input("Enter p name: ")
        Distribution_name = input("Enter distribution name: ")
        Retail_price = int(input("Enter retail price: "))
        Whole_price = int(input("Enter whole price: "))
        P_description = input("Enter p description: ")
        Manufacturer_year = int(input("Enter manu year: "))
        Contact_number = int(input("Enter contact number: "))
        PD.add_details(P_code,P_name,Distribution_name,Retail_price,Whole_price,P_description,Contact_number,Manufacturer_year)
    if choice == 2:
        print(Pro_details)
        Collection_name .insert_many(Pro_details)
    if choice == 3:
        n= input("enter p name: ")
        result = Collection_name.find({"P_name": n})
        for i in result:
            print(i)
    if choice == 4:
        result = Collection_name.delete_many({'P_name':"biscuits"})
        print(result.deleted_count)
    if choice == 5:
        result = Collection_name.update_one({'P_name':"choco"},{"$set":{"P_name":"dairy milk"}})
        break



        