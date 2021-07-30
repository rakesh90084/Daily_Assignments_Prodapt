# def add(a,b):
#     return a+b
# # print(add(3,4))
# x=add
# print(x(2,6))


# class A:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         print("decarator is working")
# obj=A
# obj(1,3)

# def sum(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def operation(op,x,y):
#     result=op(x,y)
#     return result
# print(operation(sum,5,12))
# print(operation(sub,5,12))

def sayHello(fn):
    def hello():
        print("hello")
        fn()
    return hello
@sayHello
def sayhi():
    print("hi")
sayhi()