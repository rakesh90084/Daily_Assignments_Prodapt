import pymongo
# servername-->for establishing connection-->localhost
# database==>studentdb
# credentials-->optional

client=pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase=client['productdb']
Collection_name=mydatabase['products']
result=Collection_name.find({"pcode":{"$gt":3000}},{"_id":0})#use find_one if we want to fetch particular data and also no need for 'forloop'
#result=Collection_name.find({"pcode":{"$lt":3000}},{"_id":0})#use find_one if we want to fetch particular data and also no need for 'forloop'
#result=Collection_name.find({"pname":{"$regex":"^l"}},{"_id":0})#use find_one if we want to fetch particular data and also no need for 'forloop'
print(result)

# for i in result:
#     print(i)
#     print(result)