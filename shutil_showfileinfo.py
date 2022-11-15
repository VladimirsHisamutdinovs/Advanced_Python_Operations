from shutil import *
import os
import time
import sys
 
def show_file_info(filename):
    stat_info = os.stat(filename)
    print ('\tMode    :', stat_info.st_mode)
    print ('\tCreated :', time.ctime(stat_info.st_ctime))
    print ('\tAccessed:', time.ctime(stat_info.st_atime))
    print ('\tModified:', time.ctime(stat_info.st_mtime))
 
os.mkdir('example')
print ('SOURCE time: ')
show_file_info('shutil_copy2.py') # change
copy2('shutil_copy2.py', 'example') # change
print ('DESTINATION time:')
show_file_info('example/shutil_copy2.py') # change