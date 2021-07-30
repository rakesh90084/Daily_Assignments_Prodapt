import re
name=input("Enter a Name")
valname=re.search("^(Mr\.|Mrs\.|Ms\.)[A-Z]{1}[^A-Z]{0,25}$",name)
#print(valname)
number=input("Enter a Number :")
valnumber=re.search("^(\+91)[6-9]\d{9}$",number)
#print(valnumber)
#[6-9]\d{10}$"
email=input("Enter a Email: ")
valemail=re.search("[a-z0-9]{0,20}@[a-z]+\.[a-z]{2,4}$",email)
#print(valemail)
pincode=input("Enter a Pincode : ")
valpincode=re.search("(^6)[0-9]{5}$",pincode)
#print(valpincode)
if valname and valemail and valpincode and valnumber:
    print("your Details are valid")
    print(name)
    print(email)
    print(number)
    print(pincode)
else:
    if not valnumber:
        print("Enter number properly")
    if not valemail:
        print("Enter email properly")
    if not valname:
        print("Enter Name properly")
    if not valpincode:
        print("Enter Pincode properly")