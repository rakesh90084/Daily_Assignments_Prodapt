import pymongo
try:
    studentlist=[]
    client=pymongo.MongoClient("mongodb://localhost:27017")
    mydatabase=client["StudentDb"]
    collection_name=mydatabase['students']
    result=collection_name.find({},{"_id":0})
    # result=collection_name.update_one({"getusn=":"4su17cs028"},{"$set":{"name":"Kavya"}})
    # print(result.updated_count)
    print(result)
    for i in result:
        studentlist.append(i)
    print(studentlist)
except:
    logging.error("unable to process")