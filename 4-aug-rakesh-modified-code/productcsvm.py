import datetime,time,csv,re,logging
from datetime import date
productlist=[]
try:
    header=["pname","description","price","manufacturer","mfd","ed"]
    class ProductDetails:
        def init(self,pname,description,price,manufucturer,mfd,ed):
           self.pname=pname
           self.description=description
           self.price=price
           self.manufacturer=manufacturer
           self.mfd=mfd
           self.ed=ed  
        def addproductdetail(self,pname,description,price,manufucturer,mfd,ed):
        
           dict1={"pname":pname,"description":description,"price":price,"manufacturer":manufacturer,"mfd":mfd,"ed":ed} 
           productlist.append(dict1)
    def validate(pname,description,manufacturer):
        valpname=re.search("[A-Z]{1}[^A-Z]{0,25}$",pname)
        valdescription=re.search("[A-Z]{1}[^A-Za-z]{0,100}$",description)
        valmanufacturer=re.search("[A-Z]{1}[^A-Za-z]{0,100}$",manufacturer)
        
        if valpname and valdescription and valmanufacturer:
           return True
        else:
           return False 
    obj=ProductDetails()    
    today=datetime.date.today()
    while True:
        print("1.Add Product")
        print("2.View products")
        print("3.Search a product")
        print("4.List products that expire today")
        print("5.Save") 
        print("6.Exit")
        choice=int(input("Enter your choice : "))
    
        if choice==1:
           pname=input("Enter the Product name : ")
           description=input("Enter the Description : ")
           price=int(input("Enter the Price : "))
           manufacturer=input("Enter the manufacturer name : ")
           mfd=input("Enter the manufacturing date : ")
           ed=input("Enter the expiry date   YYYY-MM-DD : ")
        if validate(pname,description,manufacturer)==True:
           obj.addproductdetail(pname,description,price,manufacturer,mfd,ed)
        else:
           logging.warning("Validation error")
           break   
        if choice==2:
           print(productlist)
        if choice==3:
           sname=input("Enter the product name to search : ")
           print(list(filter(lambda i:i["pname"]==sname,productlist)))
        if choice==4:
 
           current_time=time.localtime()
           tday=time.strftime("%Y-%m-%d",current_time)
 
        
           expirylist=(list(filter(lambda i:i["ed"]==str(tday),productlist)))    
           if len(expirylist)>0:
               print(expirylist)
           else:
               logging.warning("No Records") 
        if choice ==5:
            with open("pro.csv","w+",encoding="UTF8",newline='') as s:
               writer = csv.DictWriter(s,fieldnames=header)
               writer.writeheader()
               writer.writerows(productlist)                
        if choice==6:
            break
except:
    logging.error("Error")  
finally:
    print("Thank you")          