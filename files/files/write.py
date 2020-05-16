#open the file for writting
f= open("myfile.txt",'w')
print("enter text(tpy # when u r done !!)")
s= ""
while s!= '#':
    s =input()
    f.write(s+"\n")

f.close