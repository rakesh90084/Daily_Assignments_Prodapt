def say(fn):
    def hello():
        print("hello")
        fn()
    return hello

@say
def sayhi():
    print("hi")

sayhi()