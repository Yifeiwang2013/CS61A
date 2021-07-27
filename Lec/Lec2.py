#Expression
#All expressions can use function call notation

#Importing Library Fuctions
from math import sqrt
sqrt(256) # 16

from operator import add, sub,mul
add(14,28) #42

sub(100, mul(7,add(8,4))) #16

#Names, Assignment, and User-Defined Functions
from math import pi
pi #3.141592653589793

from math import sin
sin(pi/2) #1

radius = 10
radius * 2 #20

area, circ = pi * radius * radius, 2 * pi * radius
area #314.1592653589793

circ #62.83185307179586

max(1,2,3) #3
f = max
f #<Built-in function max/=>

f(1,2,3) #3

####################
max = 7 #define max to value 7

f(1,2,max) #7

max = f #redefine max to max function

from operator import add,mul

add #<built-in function add>

#define square function
def square(x):  
    return mul(x,x)


square
#<function square at 0x000002148F46E1F0>

square(11) #121

square(square(3)) #81

def sum_square(x,y):
    return square(x) + square(y)

sum_square(3,4) #25

radius #20
area #314.1592653589793

#Redefine area function
def area():
    return pi * radius * radius

radius = 1

area() #3.141592653589793

# Primitive expression: 2 (number or numeral); add(Name) 'hello'(string)
#Call expressions: max (               2  ,         3)
#                  Operator      Operand     Operand
#An Operand can also be a call expression

f = min
f = max
g, h = min, max
max = g
max(f(2,g(h(1,5),3)),4)

#radius = 10 ==> assignment statement 
#'=' symbol os called assignment operator and it's simplest means of abstraction
# when binding names to value, interpreter must maintain some sort of memory that keeps track of names, values and bindings.
#this memory is called an Environment

#The Non-Pure Print Function

print(1,2,3) #1,2,3
print('Go Bears!') #Go Bears!

print(print(1),print(2)) 
#1 --> from print(1)
#2 --> from print(2)
#None None : print(1) return none, print(2) return none

#The special value None represents nothing in Python
#None is not displayed by the interpreter as the value of an expression

def does_not_square(x):
    x * x

does_not_square(4) #None, because no returen

sixteen = does_not_square(4) #sixteen -> bind None

sixteen + 4 #none + 4
#TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'#

#Pure function -> just return values 
abs(-2) #2 
pow(2,100) # 12675......

#Non-pure function -> have side effects
print(-2) #displays "-2", but return -> None


two = print(2) #display 2

print(two) #None

#Defining functions"
# Assignment is a simple means of abstraction: binds name to value
#Function definition is a more powerful means of abstraction: binds names to expressions

#def <name> (<formal parameters>) -> signature indicate how many arguments a function takes
#    Return <return expression> -> Function body defines the computational process expressed by a function
#Precesure for def statement
#1) Create a function with signature <name>(<formal parameters>)
#2) set the body of that function to be everything indented after the first line
#3) Bind <name> to that function in the current frame 











