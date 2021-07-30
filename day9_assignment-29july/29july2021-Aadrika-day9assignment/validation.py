import re
mobnum=input("enter a mobile number :")
valid=re.search("^[6-9]\d{9}$",mobnum) #starts either with 6 7 8 9 or use dictionary
if valid:
    print("accepted")
else:
    print("not valid")