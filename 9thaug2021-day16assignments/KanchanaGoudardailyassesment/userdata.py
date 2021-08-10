import pymongo,logging
# 1.servername-->localhost
# 2.Database-->StudentDb varies acc to project
# 3.Username-->optional
# 4.Password-->optional
try:

    client=pymongo.MongoClient("mongodb://localhost:27017/") #establishing connection
    mydatabase=client['StudentDb'] #database
    collection_name=mydatabase['students']#collection

    getName=input("Enter a name :")
    getRoll=input("Enter a roll no :")
    getAdmno=input("Enter a adm no :")
    getClg=input("Enter a college name :")

    data={"name":getName,"rollno":getRoll,"admno":getAdmno,"college":getClg}
    # print(data) 

    result=collection_name.insert_one(data)
    print(result.inserted_id)#to fetch object id
except:
    logging.error("unable to process")