import re   
name=input("enter your name :")
email_id =input("\n enter your mail id :") 
mobnum=input("enter the mobile number : ")
pincode=input("enter the pincode :")


def isvalid_email(email):
    regex1 = '^\w+[\._]?\w+[@]\w+[.]\w{2,3}$'
    valid1=re.search(regex1,email_id)
    if (valid1):
        return True
    else:
        return False

def isvalid_mob(mob):
    regex2='\+?\d[\d -]{8,12}\d'
    valid2=re.search(regex2,mobnum)
    if (valid2):
        return True
    else:
        return False

def isvalid_pin(pin):
    regex3 = "^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$"
    valid3 = re.search(regex3, pincode)
    if (valid3):
        return True
    else:
        return False

em=isvalid_email(email_id)
mb=isvalid_mob(mobnum)
pin=isvalid_pin(pincode)


if em and mb and pin==True:
    print("All information is in correct format")
    print(name)
    print(mobnum)
    print(pincode)
    print(email_id)
else:
    if em != True:
        print("Enter correct phone number")
    if mb != True:
        print("enter correct email")
    if pin != True:
        print("enter correct pincode")