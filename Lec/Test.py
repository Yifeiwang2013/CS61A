from ucb import trace


@trace
def Partition(n,m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return Partition(n-m,m) + Partition(n,m-1)