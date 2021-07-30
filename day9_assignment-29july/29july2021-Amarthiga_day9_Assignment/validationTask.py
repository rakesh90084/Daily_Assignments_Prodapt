import re

def valid1(name):
    re_name = re.compile(r"^(Mr\.|Mrs\.|Ms\.) ([a-z]+)( [a-z]+)*( [a-z]+)*$", re.IGNORECASE)
    val1 = re_name.search(name)
    if val1:
        print("1. Name is verified and accepted",name)
    else:
        print("Name is invalid")

def valid2(mob_no):
    val2=re.search("^[6-9]\d{9}$",mob_no)
    if val2:
        print("2.Mobile Number is verified",mob_no)
    else:
        print("Mobile Number is invalid")

def valid3(pincode):
    val3 = re.search("^6\d{5}$",pincode)
    if val3:
        print("3.Pincode  is  acceptable: ",pincode)
    else:
        print("Pin code is invaild")

def valid4(email):
    val4 = "r^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if val4:
        print("4.valid mail address: ",email)
    else:
        print("invalid email address")

name1  = input("Enter your name: ")
mob_no1  = input("Enter your mobile number: ")
pincode1  = input("Enter your pincode: ")
email1  = str(input("Enter your email address: "))

print(valid1(name1))
print(valid2(mob_no1))
print(valid3(pincode1))
print(valid4(email1))
