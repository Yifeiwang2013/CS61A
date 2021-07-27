#Order of Recursive Calls
def cascade(n):
    """print #
    
    >>> cascade(123)
    123
    12
    1
    12
    123
    """
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)


def inverse_cascade(n):
    """print # inversely
    >>> inverse_cascade(123)
    1
    12
    123
    12
    1
    """
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f,g,n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow,print,n//10)
shrink = lambda n: f_then_g(print,shrink,n//10)

from ucb import trace

#Tree Recursion
#@trace
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2)+fib(n-1)


def fib_fast(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a = fib_fast(n-2)
        b = fib_fast(n-3)
        return a + a + b


"""Hanoi Problem"""
def move_disk(disk_number, from_peg, to_peg):
    print("Move disk "+str(disk_number)+" from peg "\
        +str(from_peg)+" to peg "+str(to_peg)+".")


def solve_hanoi(n, start_peg, end_peg):
    if n == 1:
        move_disk(n, start_peg, end_peg)
    else:
        spare_peg = 6 - start_peg - end_peg
        solve_hanoi(n-1,start_peg,spare_peg)
        move_disk(n,start_peg,end_peg)
        solve_hanoi(n-1,spare_peg,end_peg) 
         
#Counting Partitions
def count_partitions(n,m):
    """Return number of partitions of a positive integer n, using aprts up to size m
    
    >>> count_partitions(6,4)
    9
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m,m)
        without_m = count_partitions(n,m-1)
        return with_m + without_m


 