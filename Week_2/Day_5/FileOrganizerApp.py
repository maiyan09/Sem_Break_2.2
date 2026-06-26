import os
import shutil

path = input("Enter your path: ")
# path = r"C:\Users\LENOVO\Downloads\file automate"
files = os.listdir(path)

for file in files:
    fileName, fileExtention = os.path.splitext(file)
    fileExtention = fileExtention[1:]
    
    # destination = os.path.join(path, fileExtention) join automatically add '/' 
    # if os.path.exists(destination):
    #     shutil.move(path + '/' + file, path + '/' + fileExtention)
        
    if os.path.exists(path + '/' + fileExtention):
        shutil.move(path + '/' + file, path + '/' + fileExtention)
    else:
        os.mkdir(path + '/' + fileExtention)
        shutil.move(path + '/' + file, path + '/' + fileExtention)
    
    