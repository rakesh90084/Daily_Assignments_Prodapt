#validating indian mobile number
import re
phnNo=(input("Enter your mobile number:"))
validation=re.search("^[6-9]\d{9}$",phnNo)        #either of the value [6-9] or [6,,7,8,9] #\ - backslash for adding condition
if validation:
    print("validated and accepted")
else:
    print("Rejected")
    