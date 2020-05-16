import pickle,sys,os

if os.path.isfile('F:\sample data\Python\student.dat'):

    f=open("student.dat","rb")
    obj= pickle.load(f)
    obj.display()
    f.close()
