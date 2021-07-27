#Lamda Expression

square = lambda x: x*x

#Function Currying

def make_adder(n):
    """
    >>> make_adder(2)(3)
    5 
    
    
    """
    return lambda k : n + k

def curry2(f):
    """

    >>> curry2(add)(2)(3)
    5

    """
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g

curry3 = lambda f: lambda x: lambda y: f(x,y)


#Control
def if_(c,t,f):
    if c:
        t
    else:
        f

from math import sqrt
def real_sqrt(x):
    """Thr real part of the square root of X."""
    return if_(x>0, sqrt(x),0.0)


#Logical Operators
from math import sqrt
def has_big_sqrt(x):
    return x > 0 and sqrt(x)>10


def reasonable(n):
    return n == 0 or 1/n != 0


#Decoration
def trace1(fn):
    """Returns a version of fn that first print it is called
    
    fn - a function of 1 argument
    """
    def traced(x):
        print('Calling', fn, 'on argument', x)
        return fn(x)
    return traced


@trace1
def square(x):
    return x*x

@trace1
def sum_squares_up_to(n):
    k=1
    total = 0
    while k<=n:
        total,k=total + square(k), k+1
    return total
    





