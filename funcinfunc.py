def display(name):
    def message():
        return('hello ')
    result= message()+name
    return result
print(display("Abhisek"))
