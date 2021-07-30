import re
mobile=input("enter a mobile number:")
val=re.search("^[6-9]\d{9}$",mobile)
if val:
    print("accepted")
else:
    print("rejected")