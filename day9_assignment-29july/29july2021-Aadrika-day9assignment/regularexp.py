import re
text=input("enter the text here ")
# val=re.search(".*hello$",text)
val=re.search("^the.*hello$",text) #start with "the" and ends with "hello"
if val:
    print("accepted")
else:
    print("rejected")
