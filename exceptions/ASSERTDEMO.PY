try:

    num=int(input("Enter a no : "))
    assert num%2==0," Enterd a oddno "
#    '''Assertion Error'''
except AssertionError as obj:
    print(obj)

print("After the assertion")
  