''' decorator takes a function and returns a function'''
def mydecor(fun):
    def inner():
        result= fun()
        return result*2
    return inner


def num():
    return 5

result=mydecor(num)
print(result())
