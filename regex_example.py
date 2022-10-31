import re
#or
#from re import search

s = "egg000ham"

zeros = re.search('000', s)
print(zeros)

############################

if zeros:
    print('Match')
else:
    print('No Match')


############################

##### Metacharacters ########

print(re.search('[0-9][0-9][0-9]', 'egg000ham')) # OK

print(re.search('[0-9][0-9][0-9]', '000eggham')) # OK

print(re.search('[0-9][0-9][0-9]', 'eggham000')) # OK

print(re.search('[0-9][0-9][0-9]', '00eggham0')) # FAIL

#############################

s = "egg000ham"

print(re.search('0.0', s))

s = "00eggham"

print(re.search('0.', s))

################## [] Single Character Match Metacharacters ###################

print(re.search('co[dn]e', 'avecoder'))

print(re.search('co[dn]e', 'cones'))


##
print(re.search('[a-z]', 'EGGham'))

print(re.search('[A-Z]', 'EGGham'))

print(re.search('[0-9a-fA-f]', '---b0---'))

## ^

print(re.search('[0-9]', '000ave'))

print(re.search('[^0-9]', '000ave'))

print(re.search('[0-9^]', '000ave'))

## - 

print(re.search('[-ave]', '000-ave'))
print(re.search('[ave-]', '000-ave'))
print(re.search('[a\-ve]', '000-ave'))

print(re.search('[]]', 'ave :]'))
print(re.search('[\]]', 'ave :]'))



