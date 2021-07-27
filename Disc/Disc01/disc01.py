"""
Q1 Boolean Operator

Alfonso will only wear a jacket outside if it is below 60 degrees or it is raining.
Write a function that takes in the current temperature and a boolean value telling
if it is raining and returns True if Alfonso will wear a jacket and False otherwise.
First, try solving this problem using an if statement.
"""

def wears_jacket_with_if(temp, raining):
    """
    Return True if temperature under 60 degrees or the weather is rainning

    >>> wears_jacket_with_if(90,False)
    False
    >>> wears_jacket_with_if(40,False)
    True
    >>> wears_jacket_with_if(100,True)
    True
    """
    return True if temp < 60 or raining else False


"""
Q2 What is the result of evaluating the following code?
"""

def square(x):
    print('Here!')
    return x*x

def so_slow(num):
    x = num
    while x>0:
        x = x + 1 #Infinity Loop
    return x/0


"""Tutorial: Write a function that returns True if a positive integer n is a prime
number and False otherwise.
A prime number n is a number that is not divisible by any numbers other than 1
and n itself. For example, 13 is prime, since it is only divisible by 1 and 13, but 14
is not, since it is divisible by 1, 2, 7, and 14.
Hint: use the % operator: x % y returns the remainder of x when divided by y"""

def is_prime(n):
    """
    return True is a positive integer n is a prime number
    
    >>> is_prime(10)
    Flase
    >>> is_prime(7)
    True
    """
    k = n-1
    while k > 1:
        if n%k == 0: return False
        k = k - 1
    return True  


