import re
name1  = input("Enter your name: ")

def validate(name):
    re_name = re.compile(r"^(Mr\.|Mrs\.|Ms\.) ([a-z]+)( [a-z]+)*( [a-z]+)*$",name1)
    val1 = re_name.search(name)
    if val1:
        print("Verified and accepted")
    else:
        print("Name is invalid")

mob_no= input("Enter your mobile no: ")
val2=re.search("^[6-9]\d{9}$",mob_no)
if val2:
    print("Verified and accepted",mob_no)
else:
    print("Mobile Number is invalid")


pincode = input("Enter your pincode: ")
val3 = re.search("^6\d{5}$",pincode)
if val3:
    print("3.Pincode  is  acceptable: ",pincode)
else:
    print("the pin code is incorrect")


email = str(input("Enter your email id: "))
val4 = "r^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
if val3:
    print("4.valid mail address: ",email)
else:
    print("invalid email address")
