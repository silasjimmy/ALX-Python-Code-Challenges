def exponential(a, n):
    '''
    Implementation of the exponential algorithm
    '''
    if n == 0:
        return 1
    else:
        return a * exponential(a, n - 1)


print("Exponential:", exponential(2, 5))


def fibonacci(n):
    '''
    Implementation of the fibonacci algorithm
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print("Fibonacci:", fibonacci(7))


def cumulate(n):
    '''
    Implementation of the cumulative algorithm
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + cumulate(n - 1)


print("Cumulative:", cumulate(5))
