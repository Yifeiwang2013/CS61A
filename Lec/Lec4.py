#Fibonacci Sequence
def fib(n):
    """Compute the nth Fabonacci number, for N>=1.
    
    
    >>> fib(5)
    5
    
    >>> fib(10)
    55
    
    """
    pred, curr = 0,1
    k = 1
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr

# Higher order functions
 
"""Generalization"""
from math import pi, sqrt

def area(r, shape_constant):
    assert r > 0, 'A lenth must be positive'
    return r*r*shape_constant
     

def  area_square(r):
    assert r > 0, 'A length must be positive'
    return area(r,1)

def area_circle(r):
    return area(r,pi)

def area_hexagon(r):
    return area(r,3*sqrt(3)/2)


"""Generalization"""

def identity(k):
    return k

def cube(k):
    return pow(k,3)

def  summation(n, term):
    """Sum the first N terms of a sequence
    
    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total


def sum_naturals(n):
    """Sum the first N natural number
    
    >>> sum_naturals(5)
    15
    """
    return summation(n, identity)



def sum_cubes(n):
    """Sum the first N cubes of natural bubers.
    
    >>> sum_cubes(5)
    225
    """
    return summation(n, cube)


from operator import mul
def pi_term(k):
    return 8 / mul(4*k-3, 4*k-1)


#Functions as return value
"""Generalization"""
def make_adder(n):
    """Return a function that takes one argument
    K and return K+N
    
    >>> add_three = make_adder(3)

    >>> add_three(4)
    7
    """
    def adder(k):
        return k+ n
    return adder


##









