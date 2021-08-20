import os                                   #we import this library to work with the OS

path = '/Users'                   #make sure to use '/' or you will get issues with some folders

directory_contents = os.listdir(path)       #create a variable that will have all the sub-folders in Program Files

print(directory_contents)                   #for this example, simply print out the contents of directory_contents

for files in directory_contents:            #decided to use a for-loop to make the contents more presentable.
    print("-->", files)
    try:
        word = path + "/" + files
        print(os.listdir(word))
    except:
        print("nothing here")


