def name(fn):
    def person():
        print("hello Aadrika")
        fn()
    return person

@name
def say():
    print("hi aadrika")

say()