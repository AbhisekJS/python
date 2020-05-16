#\d = digit 0-9  ,\D= nondigit \s="white space" \S="nonwhite space"  \b="space arround words" \w ="alphanumeric value"
#\W= "non alpha numeric character" \A=" start of the string do a search"  \Z="end of the string"

import re
str = "Take up one idea ata time idiot"
result= re.search(r'i\w\w\w\w',str)
if result.group()=='idiot':
    print ("dont abuse please")
print(result.group())