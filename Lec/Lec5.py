#

def apply_twice(f,x):
    return f(f(x))


def square(x):
    return x*x

#using a higher order function

def repeat(f,x):
    while f(x) != x:
        x = f(x)
    return x

def g(y):
    return (y + 5) // 3


def make_adder(n):
    def adder(k):
        return k+n
    return adder



#Local Names
def f(x,y):
    def g(a):
        return a + y
    return g(x)



###
def triple(x):
    return 3*x

def compose1(f,g):
    def h(x):
        return f(g(x))
    return h

 
squiple = compose1(square,triple)

tripare = compose1(triple,square)

squadder = compose1(square,make_adder(2))

