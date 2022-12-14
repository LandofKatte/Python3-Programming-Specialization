# Accumulating Results From a Dictionary

Just as we have iterated through the elements of a list to accumulate a result, we can also iterate through the keys in a dictionary, accumulating a result that may depend on the values associated with each of the keys.

For example, suppose that we wanted to compute a Scrabble score for the Study in Scarlet text. Each occurrence of the letter āeā earns one point, but āqā earns 10. We have a second dictionary, stored in the variable letter_values. Now, to compute the total score, we start an accumulator at 0 and go through each of the letters in the counts dictionary. For each of those letters that has a letter value (no points for spaces, punctuation, capital letters, etc.), we add to the total score.
```
f = open('scarlet2.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
letter_counts = {} # start with an empty dictionary
for c in txt:
    if c not in letter_counts:
        # we have not seen this character before, so initialize a counter for it
        letter_counts[c] = 0

    #whether we've seen it before or not, increment its counter
    letter_counts[c] = letter_counts[c] + 1

letter_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f':4, 'g': 2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}

tot = 0
for letter in letter_counts:
    if letter in letter_values:
        tot = tot + letter_values[letter] * letter_counts[letter]

print(tot)

337353
```
Line 18 is the tricky one. We are updating the variable tot to have its old number plus the score for the current letter times the number of occurrences of that letter. 

The dictionary travel contains the number of countries within each continent that Jackie has traveled to. Find the total number of countries that Jackie has been to, and save this number to the variable name total. Do not hard code this!
```
travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}

total = 0
for i in travel:
    total = total + travel[i]
print(total)

19
```

schedule is a dictionary where a class name is a key and its value is how many credits it was worth. Go through and accumulate the total number of credits that have been earned so far and assign that to the variable total_credits. Do not hardcode.
```
schedule = {"UARTS 150": 3, "SPANISH 103": 4, "ENGLISH 125": 4, "SI 110": 4, "ENS 356": 2, "WOMENSTD 240": 4, "SI 106": 4, "BIO 118": 3, "SPANISH 231": 4, "PSYCH 111": 4, "LING 111": 3, "SPANISH 232": 4, "STATS 250": 4, "SI 206": 4, "COGSCI 200": 4, "AMCULT 202": 4, "ANTHRO 101": 4}

total_credits = 0

for i in schedule:
    total_credits = total_credits + schedule[i]
print(total_credits)

63
```
