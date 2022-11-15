import os 
   
# import the shutil module  
import shutil 
   
# write the path of the file
path = '/home/User'
   
# List all the files and directories in the given path
print("Before copying file:") 
print(os.listdir(path)) 
   
   
# write the Source path 
source = "/home/User/file.txt"
   
# Print the file permission of the source given
perms = os.stat(source).st_mode 
print("File Permission mode:", perms, "\n") 
   
# Write the Destination path 
destinationfile = "/home/User/file(copy).txt"
   
# Copy the content of source file to destination file 
dests = shutil.copy(source, destinationfile) 
   
# List files and directories of the path 
print("After copying file:") 
print(os.listdir(path)) 
   
# Print again all the file permission
perms = os.stat(destinationfile).st_mode 
print("File Permission mode:", perms) 
   
# Print path of of the file which is created
print("Destination path:", dests) 
