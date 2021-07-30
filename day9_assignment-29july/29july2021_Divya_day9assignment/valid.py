import re

name = input("enter a name: ")
num = input("enter a phone number: ")
pin_code = input("enter a pin code: ")
e_id = str(input("enter a email id: "))
#address = input("enter the address: ")

val = re.search("^D.*a",name)
val1 = re.search("^\+91?[6-9]\d{9}$",num)
val2 = re.search("^6\d{5}$",pin_code)
val3 = "r^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

if val and val1 and val2 and val3:
    print("Accepted! welcome! ")
    print("1.the name is acceptable:",name)
    print("2.Number is  acceptable: ",num)
    print("3.Pincode  is  acceptable: ",pin_code)
    print("4.valid mail address: ",e_id)
elif not val:
    print("Try again name")
elif not val1:
    print("Try again number")
elif not val2:
    print("Try again pin code")
elif not val3:
    print("ry again email id")
else:
    print("time over")


# print(val)
# print(val1)
# print(val2)
# print(val3)

# if val :
#     if val1:
#         if val2:
#             if val3:
#                 print("accepted")
#             else:
#                 print("na")
#         else:
#             print("na")
#     else:
#         print("na")
# else:
#     print("na",name)



# if val:
#     print("1.the name is acceptable:",name)
# else:
#     print("enter a correct name")
# if val1:
#     print("2.Number is  acceptable: ",num)
# else:
#     print("The number is incorrect")
# if val2:
#     print("3.Pincode  is  acceptable: ",pin_code)
# else:
#     print("the pin code is incorrect")
# if val3:
#     print("4.valid mail address: ",e_id)
# else:
#     print("invalid email address")
