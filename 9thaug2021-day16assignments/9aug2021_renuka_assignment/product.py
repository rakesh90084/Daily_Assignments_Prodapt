import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
database=client['productdb']
Collection_name=database['products']

productdetails=[]

class product:

    def addproduct(self,pname,pdes,pcode,manfacno,manufacname,wprice,rprice):
        pdict={"pname":pname,"pdes":pdes,"pcode":pcode,"manfacno":manfacno,"wprice":wprice,"rprice":rprice}
        productdetails.append(pdict)  
obj=product()
while(True):
    print("1.Add product")
    print("2.view all products")
    print("3.enter product code")
    choice=int(input("enter your choice"))
    if choice==1:
        pname=input("enter product name:")
            # mfg_date=input("enter manufacturing date:")
            # exp_date=input("enter expiry date:")
        pdes=input("enter product description:")
        pcode=int(input("enter product code:"))
        manfacno=int(input("enter contact number"))
        manufacname=input("enter manufacturer name:")
        wprice=input("enter wholesale price")
        rprice=input("enter retail price")
        obj.addproduct(pname,pdes,pcode,manfacno,manufacname,wprice,rprice)
           
    if choice==2:
        print(productdetails)
        break
result=Collection_name.insert_many(productdetails)
print(result.inserted_ids)

    
        

           


       