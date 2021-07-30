import re
name=input("enter the name:")
mobile=input("enter the mobileno:")
pincode=input("enter the pincode:")
email=input("enter the email address:")
val1=re.search("^[6-9]\d{9}$",mobile)
if val1:
      print("number accepted")
      print(mobile)
else:
    print("mobile number rejected")

val2=re.search("^5\d{5}$",pincode) 
if val2:
     print("pincode accepted")
     print(pincode)
else:
   print(" pincode rejected")

val3=re.search("^[a-zA-Z][a-zA-Z0-9.]*@gmail.com",email)
if val3:
      print("emailaccepted")
      print(email)
else:
    print(" email rejected")