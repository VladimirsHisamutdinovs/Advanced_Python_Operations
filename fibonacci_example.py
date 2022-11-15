
### iterative

def fibonacci_iter(num):
    # edge case
    if not(isinstance(num, int) and num>= 0):
        raise ValueError(f'num must be >= 0')
    # base case
    if num in {0, 1}:
        return num
    
    prev, fib_num = 0, 1

    for _ in range(2, num+1):
        prev, fib_num = fib_num, prev + fib_num
    
    return fib_num

################ recursive

def fibonacci_rec(num):
    # base case
    if num in {0, 1}:
        return num
    return fibonacci_rec(num - 1) + fibonacci_rec(num - 2)


if __name__ == '__main__':

    fibonacci_iter(5)

    print([fibonacci_iter(num) for num in range(12)])

    ### cal rec case
    print([fibonacci_rec(num) for num in range(12)])