def decorfun(fun):
    def inner(n):
        result = fun(n)
        result+= "how are you"
        return result
    return inner






@decorfun
def hello(name):
    return "hello "+ name

print(hello("suk"))
