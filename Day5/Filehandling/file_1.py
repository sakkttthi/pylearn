# The open() function takes two parameters; filename, and mode. 
'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
'''

# Read a file 
f = open("D:\CODE\pyDocument\Day5\Filehandling\Filetxt.txt", "r")
print(f.read())
# print(f.readline())
f.close() #always best practice to close the file after use

# Write to a file 
a = open("D:\CODE\pyDocument\Day5\Filehandling\Filetxt.txt", "a") #will add data to file
a.write("New line added at the end")
a.close()

b= open("D:\CODE\pyDocument\Day5\Filehandling\Filetxt.txt", "r")
print(b.read())

# Write to a file 
t = open("D:\CODE\pyDocument\Day5\Filehandling\Filetxt.txt", "w")
t.write("Entire doc onyl has this line")
t.close()

y = open("D:\CODE\pyDocument\Day5\Filehandling\Filetxt.txt", "r")
print(y.read())

#create a new file 
z = open ("thisnewfile.txt","x")

# Delete a file 
# To delete a file, you must import the OS module, and run its os.remove() function
import os
os.remove("thisnewfile.txt")

# Check and remove 
if os.path.exists("thisnewfile.txt"):
    os.remove("thisnewfile.txt")
else:
    print("file not found")


# delete folder
# To delete an entire folder, use the os.rmdir() method
import os
os.rmdir("myfolder")