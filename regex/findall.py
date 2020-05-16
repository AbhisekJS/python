
#\d = digit 0-9  ,\D= nondigit \s="white space" \S="nonwhite space"  \b="space arround words" \w ="alphanumeric value"
#\W= "non alpha numeric character" \A=" start of the string do a search"  \Z="end of the string"

import re
str = "Idiotic Take up one idea ata time idiot date 12-12-2012"
result= re.findall(r'i\w\w\w\w',str)

print(result)


result= re.findall(r'i\w{7}',str) 
print(result)

result=re.findall(r'o\w{1,2}',str)
print(result)

result=re.findall(r'\d+',str)
print(result)

result=re.search(r'^I\w*,str)
print(result.group())