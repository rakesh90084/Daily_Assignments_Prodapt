#Normal method:
def add(a,b):
    return a+b
#print(add(2,3))

#decorators:
x=add 
#print(x(4,6))

#decorator class
class decorator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("decorator is working")

# obj=decorator
# obj(1,2)


#pass a function as a argument
def sum(x,y):     
    return x+y
def difference(a,b):
    return a-b
def operation(op,x,y):
    result=op(x,y)
    return result
# print(operation(sum,10,5))
# print(operation(difference,12,4))

#practice
def multi(a,b):
    return a*b
def div(rt,b,c):
    result=rt(b,c)
    return result
def operation(op,x,y):
    result1=op(x,y)
    return result1
#print(div(sum,10,5))
#print(operation(div(multi,5,15)))

# wrap a function inside a function
def hi(sn):
    def sayhello():
        print("Hello,world")
        sn()
    return sayhello

@hi               #  @ decorator -->we define a function with decorator
def sayhi():
    print("Hi")

sayhi()







