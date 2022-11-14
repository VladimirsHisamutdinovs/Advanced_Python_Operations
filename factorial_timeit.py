####################
# timeit

from timeit import timeit

### recursive

stmt = '''
    def factorial(num):
        print('Recursive')
        return 1 if num <= 1 else num * factorial(num - 1)
      '''

timeit('factorial(5)', setup=stmt, number=1000000) 

### iterative

stmt = '''
    def factorial(num):
        print('Iterative')
        return_val = 1
        for i in range(2, num + 1)
            return_val *= i
        return return_val
'''

timeit('factorial(5)', setup=stmt, number=1000000) 

### reduce()

stmt = '''
    from functools import reduce

    def factorial(num):
        print('reduce()')
        return reduce(lambda a, b: a * b, range(1, num + 1) or [1])
'''


timeit('factorial(5)', setup=stmt, number=1000000) 


### math

stmt = 'from math import factorial'

timeit('factorial(5)', setup=stmt, number=1000000) 

