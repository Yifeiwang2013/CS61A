# p2021
2000 + 21

# Python built in functions
abs(-2)
abs(2300 - 4321)

"Go Bears"
"Gob" + "ears"
"Go Bears! " * 1000

# You can download the file locally from http://composingprograms.com/shakespeare.txt
from urllib.request import urlopen

shakes = urlopen("http://composingprograms.com/shakespeare.txt")
# File that contains the complete text of William Shakespeare's 37 plays, all in a single text document.

text = shakes.read().decode().split()

len(text)  # number of words


text[:25]
print("hello world!")

text.count("the")
text.count("thou")  # how shakespeare said you
text.count("you")

text.count("forsooth")

text.count(",")
text.count(",") / len(text)  # 8% commas!

words = set(text)  # We care about unique words!

"forsooth" in words
"computer" in words

"draw"
"draw"[0]

{w[0] for w in words}


"draw"[::-1]

{w for w in words if w == w[::-1]}

{w for w in words if w == w[::-1] and len(w) > 4}


"draw" in words
"ward" in words

{w for w in words if w[::-1] in words and len(w) > 3}

sorted({w for w in words if w[::-1] in words and len(w) > 3})

sorted({w for w in words if w[::-1] in words and len(w) == 5})
#['asses', 'deeps', 'devil', 'keels', 'knits', 'leets', 'leper', 'level', 'lived', 'madam', 
# 'minim', 'refer', 'repel', 'rever', 'sessa', 'sleek', 'speed', 'spots', 'steel', 'stink', 'stops']

sorted({w for w in words if w[::-1] in words and len(w) == 6})

max(words, key=len)  # longest word

set("forsooth")  # gets a set with each unique letter

#Find the word with most unique letters!
max({(len(set(w)), w) for w in words})