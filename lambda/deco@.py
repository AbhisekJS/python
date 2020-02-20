def decor(num):
    def new():
        result=num()
        return result*2
    return new
    
@decor
def num():
    return 5


print(num())
