import logging

logging.basicConfig(filename="mylog.log",level=logging.DEBUG)

try:
    f = open("myfile","w")
    a, b=[int(x) for x in input("Enter two numbers: ").split()]
    logging.info("Division in progress")
    c =a/b
    f.write("writing %d into file "%c)
    f.close()
except:
    print("dicvision by zero is not allowed")
    print("please enter a non zero number")
    logging.error("Division by Error")
else:
    print("you have entered a non zero number")

finally:
    f.close()
    print("file closed")
print("code after execution ")