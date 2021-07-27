def keep_ints(cond,n):
    """Print out all inters 1..i..n where cond(i) is true
    
    >>> def is_even(x):
    ...     #Even numbers have remainder 0 when divided by 2
    ...     return x%2 == 0
    >>> keep_ints(is_even,5)
    2
    4
    """
    for i in range(n):
        if cond(i+1):
            print(i+1)


def make_keeper(n):
    """Returns a function which takes one parameter cond and prints out all integers 1..i..n where calling cond(i) returns True.
    
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x%2 == 0

    >>> def is_odd(x):
    ...     return x%2==1

    >>> make_keeper(5)(is_even)
    2
    4


    >>> make_keeper(10)(is_odd)
    1
    3
    5
    7
    9
    """
    def printNum(cond):
        for i in range(n):
            if cond(i+1): print(i+1)
        return
    return printNum

def print_delayed(x):
    """"Return a new function. This new function, when called,will print out x and return another function with the same behavior.
    >>> f = print_delayed(1)
    >>> f = f(2)
    1
    >>> f = f(3)
    2
    >>> f =f(4)(5)
    3
    4
    >>> f("hi")
    5
    <function print_delayed> # a function is returned'
    """
    def printNum(y):
        print(x)
        return print_delayed(y)
    return printNum
