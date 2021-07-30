import re
name=input("Enter your name: ")
mobile_num=input("Enter your mobile number: ")
address=input("Enter your address: ")
pincode=input("Enter your pincode: ")
email_id=input("Enter your emailid: ")

def isvalid(mobile_num):
    r=re.match("(0|91)?[-\s]?[6-9]\d{9}",mobile_num)
    if (r):
        return True
    else:
        return False

    
 
def validateemail(email_id):
    r1= re.match(r"[\w-]{1,20}@\w{2,20}\.\w{2,3}$",email_id)
    if (r1):
        return True
    else:
        return False


def validatepincode(pincode):
    r2=re.match("^[5-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$",pincode)
    if (r2):
        return True
    else:
        return False

a=isvalid(mobile_num)
b=validateemail(email_id)
c=validatepincode(pincode)


if a and b and c==True:
    print("All in correct format")
    print(name)
    print(mobile_num)
    print(address)
    print(pincode)
    print(email_id)
else:
    if a != True:
        print("Enter phone number in CORRECT format")
    if b != True:
        print("enter email in CORRECT format")
    if c != True:
        print("enter pincode in CORRECT format")

