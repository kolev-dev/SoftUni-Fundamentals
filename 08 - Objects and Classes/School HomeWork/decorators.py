def my_decorator(func):
    def wrapper():
        print("asd")
        func()
        print("asd2")

    return wrapper

@my_decorator
def say_hello():
    return "hello"

print(say_hello())

