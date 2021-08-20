import os                                   #we import this library to work with the OS

path = '\Program Files'                     #for this example we're starting with the folder Program Files. Does not need the C:\

directory_contents = os.listdir(path)       #create a variable that will have all the sub-folders in Program Files

print(directory_contents)                   #for this example, simply print out the contents of directory_contents

for files in directory_contents:            #decided to use a for-loop to make the contents more presentable.
    print(files)