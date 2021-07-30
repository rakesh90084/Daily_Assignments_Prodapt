import re
#For starting
# text =input("Enter a text: ")
# val=re.search("^The",text)   #validating the character --> 1st argument(^the)
# print(val)

# if val:
#     print("Accepted")

# else:
#     print("Rejected")

#For ending
text =input("Enter a text: ")
#val=re.search("The$",text)
#print(val)

# for both front and back together 
# val=re.search(".*The$",text)
# print(val)

# if val:
#     print("Accepted")

# else:
#     print("Rejected")

#4
val=re.search("^The.*Hello$",text)
print(val)

if val:
    print("Accepted")

else:
    print("Rejected")