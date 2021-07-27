2000+15
#>>>2015

1*2*((3*4*5//6)**3)+7+8
#**3 -> Power
#>>>2015

max(2,4)
#>>>4

min(-2,50000)
#-2

from operator import add,mul
add(2,3)
#>>>5

mul(2,3)
#>>>6

max(1,2,3,4,5)
#>>>5

mul(add(2,mul(4,6)),add(3,5))
#>>>208

#add       (2    ,           3)
#   Operator   Operand   Operand
#  Function   argument   argument

#Operator and operands are also expressions
#so they evaluate to values


#1)Evaluate the operator and then the operand subexpressions
#2)Apply the function that is the value of the operator subexpression to arguments that are the values of the operand subexpression"""

#Demo Function, Objects, and Interpreters

# p2021
2000 + 21

# Python built in functions
abs(-2)
abs(2300 - 4321)

"Go Bears"
"Gob" + "ears"
"Go Bears! " * 1000

shakes = open('shakespeare.txt') #Open text
text = shakes.read().split() #read and split text
text[:25] #first 25 words
#['A', "MIDSUMMER-NIGHT'S", 'DREAM', 'Now', ',', 'fair', 'Hippolyta', ',', 'our', 'nuptial', 'hour', 'Draws', 'on', 'apace', ':', 'four', 'happy', 'days', 'bring', 'in', 'Another', 'moon', ';', 'but', 'O']
len(text) #number of world
#980637
text.count('the') #number of 'the'
#23272
text.count('thou')#number of 'thou'
#4501
text.count('you') #number of 'you'
#12361
text.count('forsooth')#number of 'forsooth'
#40

text.count(',') #number of ','
#81827
text.count(',')/len(text) # % of ',' of all words
#0.0834427010198473
words = set(text) # creat word set
'forsooth' in words # if 'forsooth' in words
#True
'the' in words # if 'the' in words
#True
len(words) #number of nuique words
#33505

'draw' #string
#'draw'

#'draw' [::-1] #reverse word
#'ward'

{w for w in words if w == w[::-1] and len(w) >4} # word which same as its reverse word and lenth >4
#{'rever', 'refer', 'level', 'redder', 'madam', 'minim'}

{w for w in words if w[::-1] in words and len(w) ==4} #words which reverse in set and lenth =4
#{'pins', 'sees', 'smug', 'door', 'meed', 'teem', 'doom', 'hoop', 'rood', 
# 'wort', 'laid', 'draw', 'ward', 'liar', 'bard', 'noon', 'stab', 'gums', 'poop', 
# 'spot', 'deem', 'pooh', 'leek', 'garb', 'port', 'evil', 'tops', 'tips', 'trop', 'wolf', 
# 'maws', 'esse', 'spit', 'meet', 'leer', 'reed', 'pots', 'dial', 'lees', 'deed', 'spin', 'star', 'seel', 
# 'drab', 'brag', 'peep', 'keel', 'trow', 'nips', 'room', 'moor', 'stop', 'part', 'bats', 'flow', 'ecce', 'rats', 
# 'pool', 'elle', 'tang', 'rail', 'deer', 'gnat', 'mood', 'reel', 'swam', 'snip', 'live', 'loop', 'trap'}

{w for w in words if w[::-1] in words and len(w) ==6} #words which reverse in set and lenth =6
#{'reward', 'redder', 'diaper', 'repaid', 'drawer'}










