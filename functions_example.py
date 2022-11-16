def adds_nums(a, b):
    return a + b

print(adds_nums(2, 3))

###################

def ave(name):
    return f'Ave {name}!'

def gladiator_greeting(name):
    return f'Ave {name} morituri te salutant, '

def ave_caesar(salve_func):
    return salve_func('Caesar')



print(ave_caesar(ave))
print(ave_caesar(gladiator_greeting))

##################
## Inner Funcs ###

def outer():
    print('Outer function')

    def inner_one():
        print('inner one function')

    def inner_two():
        print('inner two function')

    inner_one()
    inner_two()

outer()

########################################
## Returning Functions from Functions ##

def outer(func_num):

    def inner_one():
        print('inner one function')

    def inner_two():
        print('inner two function')

    if func_num == 1:
        return inner_one()
    else:
        return inner_two()


one = outer(1)
two = outer(2)

#################################
### Simple Decorators ###

def ave_decorator(func):
    def wrapper():
        print("Programming")
        func()
        print("Fun!")
    return wrapper

def say_is():
    print("is")

say_is = ave_decorator(say_is)

say_is()

#######################
### first decorator ###

def ave_decorator(func):
    def wrapper():
        print("Programming")
        func()
        print("Fun!")
    return wrapper

@ave_decorator # say_is = ave_decorator(say_is)
def say_is():
    print("is not")

say_is()
