# add some slides explanation

def func():
    num = 10
    func()

######################

# set above

from sys import setrecursionlimit
setrecursionlimit(100)

######################

def countdown(num):
    print(num)
    if num == 0:
        return
    else:
        countdown(num - 1)

### update the code above

def countdown(num):
    print(num)
    if num > 0:
        countdown(num - 1)

### non recursive approach

def countdown(num):
    while num >= 0:
        print(num)
        num -=1 