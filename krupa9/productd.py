import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/") #establishing a connection
mydatabase=client['productDb']          #database
collection_name=mydatabase['products'] 

productlist=[]
pview=[]
pdv=[]

class productdetails:
    def addproducts(self,pcode,name,distribution,cono,manufyear,retail,wholesale):
        dict1={"pcode":pcode,"name":name,"distribution":distribution,"cono":cono,"manufyear":manufyear,"retail":retail,"wholesale":wholesale}
        productlist.append(dict1)

obj1=productdetails()
while(1):
    print("1. add products: ")
    print("2. view all products :")
    print("3. search a product by code: ")
    print("4. know details by entering pcode ")
    print("5. to delete the product")
    print("6. exit:")

    option=int(input("enter choice"))

    if option==1:
        pcode=input("enter code: ")
        name=input("enter name: ")
        distribution=input("enter product distribution: ")
        cono=int(input("enter the no: "))
        manufyear=input("enter manufactureyear: ")
        retail=input("enter retail: ")
        wholesale=input("enter wholesale: ")
        obj1.addproducts(pcode,name,distribution,cono,manufyear,retail,wholesale)
        result=collection_name.insert_many(productlist)
        print(result.inserted_ids)

    if option==2:
        result=collection_name.find()
        for i in result:
            pview.append(i)
        print(pview)


    if option==3:
        pc=input("enter product name: ")
        x=collection_name.find({"name":pc})
        for i in x:
            print(i)

    if option==4:
        y=collection_name.find({},{"_pcode":0}) #filter
        for i in y:
            pdv.append(i)
        print(pdv)

    if option==5:
        na=input("enter product name to delete: ")
        d=collection_name.delete_one({"name":na})
        print(d)
        d1=collection_name.delete_many({"name": {"$regex":"^d"}})
        print(d1)


    if option==6:
            break



            
