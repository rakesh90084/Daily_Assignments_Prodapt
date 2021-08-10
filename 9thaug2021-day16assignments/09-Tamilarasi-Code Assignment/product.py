import pymongo,collections,re,logging
logging.basicConfig(filename='product.log',level=logging.DEBUG)
productlist=[]
client=pymongo.MongoClient("mongodb://localhost:27017/ProductDb")  
mydatabase=client["productDb"]
collection_name=mydatabase["product"]
class ProductDetails:
    def addPro_Det(self,pro_code,name,dis_name,description,price,manufactureYear):
        dict={"pro_code":pro_code,"name":name,"dis_name":dis_name,"description":description,"price":price,"manufactureYear":manufactureYear}
        productlist.append(dict)

def validate(vname,vdescription,vprice):
    name1=re.match("([a-z]+)([a-z]+)*([a-z]+)*$",vname)
    print(name1)
    description1=re.match("([a-z]+)([a-z]+)*([a-z]+)*$",vdescription)
    print(description1)
    price1=re.match("[0-9]{0,7}$",vprice)
    print(price1)
    if name1 and description1 and price1:
        return True
    else:
        return False

obj=ProductDetails()
if(__name__=='__main__'):
    try:
        while(True):
                print("1.Add Product")
                print("2.Search the Product")
                print("3.Delete the product code")
                print("4.Update the product ")
                print("5.Exit")
                option=int(input("Enter your option :"))
                if option==1:
                    pro_code=input("Enter the product code:")
                    vname = input("Enter the name of the product:")
                    dis_name=input("Enter the Product Distributor:")
                    vdescription =  input("Enter the description of the product:")
                    vprice=input("Enter the price of the product:")
                    manufactureYear=input("Enter the manufacturing Year of the product:")
                    if validate(vname,vdescription,vprice):
                        obj.addPro_Det(pro_code,vname,dis_name,vdescription,vprice,manufactureYear)
                        print(productlist)
                        result=collection_name.insert_many(productlist)
                        print(result)
                    else:
                        logging.error("Check your name, description and price")

                if option==2:
                    a=input("Enter your product code: ")
                    r=collection_name.find({"pro_code":a})
                    for i in r:
                        print(i)
                        logging.info("Completed Searching")
                
                if option==3:
                    b=input("Delete Product name:")
                    r=collection_name.delete_one({"name":b})
                    print(r.deleted_count)
                    logging.info("Completed Deleting")

                if option==4:
                    c=input("Enter Update product code:")
                    update_name=input("Enter the Update Product Name:")
                    update_price=input("Enter the Update Product Price:")        
                    r=collection_name.update_one({"name":c},{"$set":{"name":update_name,"price":update_price}})
                    print(r)
                    logging.info("Completed Updating")

                if option==5:
                    break
    except ValueError:
        logging.error("Please Check Value int or string")

    except IndexError:
        logging.error("Please Check Your Index")

    except Exception:
        logging.error("Something Went Wrong")

    finally:
        print("Äll Block Completed Successfully")