import os

# path = r"C:\Users\LENOVO\Downloads\pdf rename automate"
path = input("Enter you path:")
os.chdir(path) 
# this line in IMP because if we dont use this line (os.chdir())
# python will focus current directory where the code is not
#our given path

contents = os.listdir() # eturns a list of all files and folders in the current directory.
counter = 0

for file in contents:
    name, extension = os.path.splitext(file) 
    new_name = f"PDF - {counter}{extension}"
    os.rename(file, new_name)
    counter += 1
    
print("Succesfully rename the file with fomate (number+name)")