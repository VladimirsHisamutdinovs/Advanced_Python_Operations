import pprint
import shutil
import os
 
shutil.copytree('../shutil', './Latracal')# change
pprint.pprint(os.listdir('./Latracal'))# change

##########

print('BEFORE:')
pprint.pprint(os.listdir('.'))
 
shutil.rmtree('Latracal')
 
print('\nAFTER:')
pprint.pprint(os.listdir('.'))

#########

print(shutil.which('bsondump'))
print(shutil.which('no-such-program'))

#########

total_mem, used_mem, free_mem = shutil.disk_usage('.')
gb = 10 **9
 
print('Total: {:6.2f} GB'.format(total_mem/gb))
print('Used : {:6.2f} GB'.format(used_mem/gb))
print('Free : {:6.2f} GB'.format(free_mem/gb))

##########

shutil.move('hello.py','newdir/')

##########

root_directory='newdir'
shutil.make_archive("newdirabcd","zip",root_directory)

##########

shutil.get_archive_formats()