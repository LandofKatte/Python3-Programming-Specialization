Avast! Try this one swabbies. Here’s a table of English to Pirate translations

English-----Pirate

sir---------matey
hotel-------fleabag inn
student-----swabbie
boy---------matey
madam-------proud beauty
professor---foul blaggart
restaurant--galley
your--------yer
excuse------arr
students----swabbies
are---------be
lawyer------foul blaggart
the---------th’
restroom----head
my----------me
hello-------avast
is----------be
man---------matey

Write a program that asks the user for a sentence in English and then translates that sentence to Pirate.

pirate = {}
pirate['sir'] = 'matey'
pirate['hotel'] = 'fleabag inn'
pirate['student'] = 'swabbie'
pirate['boy'] = 'matey'
pirate['madam'] = 'proud beauty'
pirate['professor'] = 'foul blaggart'
pirate['restaurant'] = 'galley'
pirate['your'] = 'yer'
pirate['excuse'] = 'arr'
pirate['students'] = 'swabbies'
pirate['are'] = 'be'
pirate['lawyer'] = 'foul blaggart'
pirate['the'] = "th'"
pirate['restroom'] = 'head'
pirate['my'] = 'me'
pirate['hello'] = 'avast'
pirate['is'] = 'be'
pirate['man'] = 'matey'

sentence = input("Please enter a sentence in English")

psentence = []
words = sentence.split()
for aword in words:
    if aword in pirate:
        psentence.append(pirate[aword])
    else:
        psentence.append(aword)

print(" ".join(psentence))
_________________________________________

d = {'spring': 'autumn', 'autumn': 'fall', 'fall': 'spring'}
print d['autumn']
fall
___________________________________________

Write a program that finds the most used 7 letter word in scarlet3.txt.

f = open('scarlet3.txt', 'r')
contents = f.read()
d = {}

for w in contents.split():
    if len(w) == 7:
        if w not in d:
            d[w] = 1
        else:
            d[w] = d[w] + 1

dkeys = d.keys()
most_used = dkeys[0]
for k in dkeys:
    if d[k] > d[most_used]:
        most_used = k

print("The most used word is '"+most_used+"', which is used "+str(d[most_used])+" times")
________________________________________
d =  {'a': 2, 'b': 3, 'c': 1}
e = {}
for c in d:
    e[d[c]] = c
print e
# It creates a new dictionary which swaps the keys and values in d. d[c] gets the value from dictionary d with key c. In dictionary e, we are putting d[c] as a key and value as c.
___________________________________________


Write a program that allows the user to enter a string. It then prints a table of the letters of the alphabet in alphabetical order which occur in the string together with the number of times each letter occurs. Case should be ignored. A sample run of the program might look this this:

Please enter a sentence: ThiS is String with Upper and lower case Letters.
a  2
c  1
d  1
e  5
g  1
h  2
i  4
l  2
n  2
o  1
p  2
r  4
s  5
t  5
u  1
w  2
$

sentence = input("Enter a sentence for the letter count : ").lower()
d ={}

for c in sorted(sentence):
    if c.isalpha():
        d[c] = d.get(c, 0) + 1

v = d.keys()

print(v)
_______________________________________________________________
