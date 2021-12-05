import os
import shutil

path = input("Enter the name of the directory to be sorted: ")
list_of_files = os.listdir(path)

for file in list_of_files:
    name, ext = os.path.splitext(file)
    #this is going to store the extension type
    ext = ext[1:]

    if ext == '':
        continue
        #this will move the file to the directory where name 'ext' already exists
    if os.path.exists(path + '/' + ext):
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)
        #this will create a new directory if the directory doesn't already exist
    else:
        os.makedirs(path + '/' + ext)
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)
