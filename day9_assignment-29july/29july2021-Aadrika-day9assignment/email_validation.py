import re   
  
regex1 = '^\w+[\._]?\w+[@]\w+[.]\w{2,3}$'  

def check(email):   
  
    if(re.search(regex1,email)):   
        print("Valid Email")   
    else:   
        print("Invalid Email")


id =input("\n enter your mail id :")
check(id)


'''below is mob validation'''


mobnum=input("enter the mobile number : ")
regex2='\+?\d[\d -]{8,12}\d' 
valid=re.search(regex2,mobnum) 
if valid:
    print("accepted")
else:
    print("not valid")




'''below is pincode validation'''

pincode=input("enter the pincode :")
regex3 = "^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$"
m = re.search(regex3, pincode)
if m:
    print("valid pincode")
else:
    print("invalid pincode")
