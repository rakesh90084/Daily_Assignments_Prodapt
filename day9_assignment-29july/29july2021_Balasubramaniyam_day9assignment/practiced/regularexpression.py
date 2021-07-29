import re
textinput=input("Enter a text: ")
#val1=re.search("^The",textinput)
#val=re.search(".Hello$",textinput)
val=re.search("^The.*Hello$",textinput)
if val:
    print("Accepted")
else:
    print("Rejected")
