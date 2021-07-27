#Recursive Function

def split(n):
    return n//10,n%10

def sum_digits(n):
    if n < 10:
        return n 
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last


#Facterio
def fact_iter(n):
    total,k = 1,1
    while k<=n:
        total, k = total*k, k+1
    return total

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

#Verify recurisve leap of faith
#1 verify the base case
#2 Treat fact as a functional abstraction!
#3 Assume that fact(n-1) is correct
#4 Verify that fact(n) is correct, assuming that fact(n-1) correct

def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2*last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit



 
#Recursion and Iteration

def sum_digits_iter(n):
    digit_sum = 0
    while n >0:
        n,last = split(n)
        digit_sum = digit_sum + last
    return digit_sum