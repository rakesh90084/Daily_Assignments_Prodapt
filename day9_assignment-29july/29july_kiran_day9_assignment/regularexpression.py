import re
txtinput=input("enter a text:")
# val=re.search("^The",txtinput)
# val=re.search("Hello$",txtinput)
val=re.search("^The .*Hello$",txtinput)
# print(val)
if val:
    print("accepted")
else:
    print("rejected")