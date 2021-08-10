import collections
import re
import pymongo
# 1)Srevername : Localhost
# 2)Database
# 3) Username
# 4)Password
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydata=client["StudentsDb"]
collection_name=mydata["students"]
name="balu"
roll=1
adminno=2
clge="CSE"
dict1={"name":name,"roll":roll,"admino":adminno,"clge":clge}
print(dict1)
collection_name.insert_one(dict1) #insert data into database

"menu driven employee application class ,pythoncollection deque,collection name employee"
#1)add emloyee name,address,phone,designation,company name
#2)store to database
result=collection_name.find() #used retrive all the data
for i in result:
    print(i)
result=collection_name.find_one() #used to retrive only one data
print(result)
result=collection_name.find({"name":{"$regex":"^B"}}) #used retrive all the data with regex with starting B
result=collection_name.find({"name":{"$regex":"u$"}})#used retrive all the data with regex with Ending  u
result=collection_name.find({"name":{"$gt":"A"}})#used retrive all the data greater than A  u
for i in result:
    print(i)