# How to profile your python code

import cProfile

cProfile.run('20 * 110')

### Profiling a function that calls other functions

def create_array():
  arr=[]
  for i in range(0,500000):
    arr.append(i)

def print_statement():
  print('Array created successfully')


def main():
  create_array()
  print_statement()


if __name__ == '__main__':
    cProfile.run('main()')