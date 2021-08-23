import os                                   #we import this library to work with the OS

path = '/Program Files'                     #make sure to use '/' or you will get issues with some folders
                                            #this can be changed to the folder you wish to get the sub-folders for

directory_contents = os.listdir(path)       #create a variable that will have all the sub-folders in Program Files

print(directory_contents)                   #for this example, simply print out the contents of directory_contents

for files in directory_contents:            #decided to use a for-loop to make the contents more presentable.
    print("-->", files)                     #for first sub-folder, it will be --> and then the folder name
    word = path + "/" + files               #the sub folder will be added to the path of the original

    try:                                    #adding a try method because sometime the folder will need authorisations and will not work
        sub_directory_contents = os.listdir(word)
        for sub_files in sub_directory_contents:
            print("----->",sub_files)
    except:                                 #If access is not allowed or if it is a file, "Nothing here" will be displayed
        print("-----> nothing here")


