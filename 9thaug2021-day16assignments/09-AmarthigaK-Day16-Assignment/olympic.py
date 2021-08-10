import pymongo

customer =pymongo.MongoClient("mongodb+srv://Amar_24:Amar2421@cluster0.g6gs1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

DataBase = customer["MyFirstDB"]
collection = DataBase["First"]


OlympicsDB=[]

class Olympics:
    def add_games(self, game_name, olympic_year, Organizing_country, gold, gold_country, silver, silver_country, bronze, bronze_country):
        self.game_name = game_name
        self.olympic_year = olympic_year
        self.Organizing_country = Organizing_country
        self.gold = gold
        self.gold_country = gold_country
        self.silver =silver
        self.silver_country = silver_country
        self.bronze = bronze
        self.bronze_country = bronze_country

        details = {"Sport_Name": game_name,
                   "Olympic_Year":olympic_year,
                   "Organized_Country": Organizing_country,
                   "GoldWinner_Name":gold,
                   "GoldWinner_Country":gold_country,
                   "SilverWinner_Name":silver,
                   "SilverWinner_Country":silver_country,
                   "BronzeWinner_Name":bronze,
                   "BronzeWinner_Country":bronze_country}
        OlympicsDB.append(details)    

O = Olympics()


while(True):

    print(" 1.Add details: ")
    print(" 2.Display: ")
    print(" 3.Search by Game Name: ")
    print(" 4.To Delete: ")
    print(" 5.To update: ")

    choice = int(input("Type your choice: "))

    if choice==1:
        game_name = input("Enter Any Olympic Sport Name: ")
        olympic_year = input("Enter the olympic year: ")
        Organizing_country = input("Enter the Olympic organised country in that particular year: ")
        gold = input("Enter name of the Gold winner: ")
        gold_country = input("Enter Country name of the Gold winner: ")
        silver = input("Enter name of the Silver winner: ")
        silver_country = input("Enter Country name of the Silver winner: ")
        bronze = input("Enter name of the Bronze winner: ")
        bronze_country = input("Enter Country name of the Bronze winner: ")

        O.add_games(game_name, olympic_year, Organizing_country, gold, gold_country,silver, silver_country, bronze, bronze_country)
       
    if choice==2:
        print(OlympicsDB)
        collection.insert_many(OlympicsDB)

    if choice ==3:
        x = input("Enter Olympic Sport Name: ")
        findSport = collection.find({"Sport_Name":x})
        for s in findSport:
            print(s)

    if choice ==4:
        findSport = collection.delete_one({"Olympic_Year":"2020"})
        print(findSport.deleted_count)

    if choice ==5:
        findSport = collection.update_one({"Olympic_Year":"2021"}, {"$set":{"Olympic_Year":"2020"}})
        
        break





