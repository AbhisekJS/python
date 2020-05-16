try:
    f = open("myfile","w")
    a, b=[int(x) for x in input("Enter two numbers: ").split()]
    c =a/b
    f.write("writing %d into file "%c)
    f.close()
except:
    print("dicvision by zero is not allowed")
    print("please enter a non zero number")

finally:
    f.close()
    print("file closed")
print("code after execution ")