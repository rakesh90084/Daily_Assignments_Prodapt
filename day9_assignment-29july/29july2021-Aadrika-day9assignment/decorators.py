# def simpleadd(a,b):
#     return a+b
# # print(simpleadd(2,3))
# x=simpleadd
# print(x(1,2))

# class decorator:
#     def __init__(self):
#         print("hello decorators are working")
# ob=decorator
# ob()


def sum(a,b):
    return a+b


def sub(a,b):
    return a-b
def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def oper(op,x,y):
    res=op(x,y)
    return res

print(oper(sum,10,5))
print(oper(sub,10,5))
print(oper(mul,10,5))
print(oper(div,10,5))
