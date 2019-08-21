f= open("myfile.txt","w")
s=input("Enter Text :(Type # when you are done)")

s=''
while s!="#":
    s=input()
    f.write(s+"\n")

f.close
