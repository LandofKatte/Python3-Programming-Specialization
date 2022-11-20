# Introduction: Accumulating Multiple Results In a Dictionary

You have previously seen the accumulator pattern; it goes through the items in a sequence, updating an accumulator variable each time. Rather than accumulating a single result, it’s possible to accumulate many results. Suppose, for example, we wanted to find out which letters are used most frequently in English.

Suppose we had a reasonably long text that we thought was representative of general English usage. For our purposes in the this chapter, we will use the text of the Sherlock Holmes story, “A Study in Scarlet”, by Sir Arthur Conan Doyle. The text actually includes a few lines about the source of the transcription (Project Gutenberg), but those will not materially affect our analyses so we will just leave them in. You can access this text within this chapter with the code open('scarlet.txt', 'r').

If we want to find out how often the letter ‘t’ occurs, we can accumulate the result in a count variable.
```
f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
t_count = 0 #initialize the accumulator variable
for c in txt:
    if c == 't':
        t_count = t_count + 1   #increment the counter
print("t: " + str(t_count) + " occurrences")

t: 17584 occurrences
```

We can accumulate counts for more than one character as we traverse the text. Suppose, for example, we wanted to compare the counts of ‘t’ and ‘s’ in the text.
```
f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
t_count = 0 #initialize the accumulator variable
s_count = 0 # initialize the s counter accumulator as well
for c in txt:
    if c == 't':
        t_count = t_count + 1   #increment the t counter
    elif c == 's':
        s_count = s_count + 1
print("t: " + str(t_count) + " occurrences")
print("s: " + str(s_count) + " occurrences")

t: 17584 occurrences
s: 11830 occurrences
```

OK, but you can see this is going to get tedious if we try to accumulate counts for all the letters. We will have to initialize a lot of accumulators, and there will be a very long if..elif..elif statement. Using a dictionary, we can do a lot better.

One dictionary can hold all of the accumulator variables. Each key in the dictionary will be one letter, and the corresponding value will be the count so far of how many times that letter has occurred.

```
f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
letter_counts = {} # start with an empty dictionary
letter_counts['t'] = 0  # initialize the t counter
letter_counts['s'] = 0  # initialize the s counter
for c in txt:
    if c == 't':
        letter_counts['t'] = letter_counts['t'] + 1  # increment the t counter
    elif c == 's':
        letter_counts['s'] = letter_counts['s'] + 1  # increment the s counter

print("t: " + str(letter_counts['t']) + " occurrences")
print("s: " + str(letter_counts['s']) + " occurrences")

t: 17584 occurrences
s: 11830 occurrences
```

In the example above, we’ve created a dictionary, letter_counts, to hold the letters ‘t’ and ‘c’, with their associated counts. This hasn’t really improved things yet, but look closely at lines 8-11 in the code above. Whichever character we’re seeing, t or s, we’re incrementing the counter for that character. So lines 9 and 11 could really be the same, if we make one small change:
```
f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
letter_counts = {} # start with an empty dictionary
letter_counts['t'] = 0  # intiialize the t counter
letter_counts['s'] = 0  # initialize the s counter
for c in txt:
    if c == 't':
        letter_counts[c] = letter_counts[c] + 1   # increment the t counter
    elif c == 's':
        letter_counts[c] = letter_counts[c] + 1   # increment the s counter

print("t: " + str(letter_counts['t']) + " occurrences")
print("s: " + str(letter_counts['s']) + " occurrences")

t: 17584 occurrences
s: 11830 occurrences
```

Lines 9 and 11 above may seem a little confusing at first. Previously, our assignment statements referred directly to keys, with letter_counts['s'] and letter_counts['t']. Here we are just using a variable c whose value is ‘s’ or ‘t’, or some other character.

If that made perfect sense to you, skip the next two paragraphs. Otherwise, read on. Let’s break down that line in a little more detail.

First, note that, as with all assignment statements, the right side is evaluated first. In this case letter_counts[c] has to be evaluated. As with all expressions, we first have to substitute values for variable names. letter_counts is a variable bound to a dictionary. c is a variable bound to one letter from the string that txt is bound to (that’s what the for statement says to do: execute lines 8-11 once for each character in txt, with the variable c bound to the current character on each iteration.) So, let’s suppose that the current character is the letter s (we are on line 11). Then letter_counts[c] looks up the value associated with the key ‘s’ in the dictionary letter_counts. If all is working correctly, that value should be the number of times ‘s’ has previously occurred. For the sake of argument, suppose it’s 25. Then the right side evaluates to 25 + 1, 26. Watch this play out below.
```
f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
letter_counts = {} # start with an empty dictionary
letter_counts['t'] = 15 # initialize the t counter
letter_counts['s'] = 25 # initialize the s counter
----------------------------------------------------
for c in txt: # we have reached the 26th s now
for 's' in txt:
if c == 't':
if 's' == 't':
elif c == 's':
elif 's' == 's':
letter_counts[c] = letter_counts[c] + 1 # increment the s counter
letter_counts['s'] = letter_counts['s'] + 1 # increment the s counter
letter_counts['s'] = 25 + 1 # increment the s counter
letter_counts['s'] = 26 # increment the s counter
```

Now we have assigned the value 26 to letter_counts[c]. That is, in dictionary x, we set the value associated with the key ‘s’ (the current value of the variable c) to be 26. In other words, we have incremented the value associated with the key ‘s’ from 25 to 26.

We can do better still. One other nice thing about using a dictionary is that we don’t have to prespecify what all the letters will be. In this case, we know in advance what the alphabet for English is, but later in the chapter we will count the occurrences of words, and we do not know in advance all the of the words that may be used. Rather than pre-specifying which letters to keep accumulator counts for, we can start with an empty dictionary and add a counter to the dictionary each time we encounter a new thing that we want to start keeping count of.
```
f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
letter_counts = {} # start with an empty dictionary
for c in txt:
    if c not in letter_counts:
        # we have not seen this character before, so initialize a counter for it
        letter_counts[c] = 0

    #whether we've seen it before or not, increment its counter
    letter_counts[c] = letter_counts[c] + 1

print("t: " + str(letter_counts['t']) + " occurrences")
print("s: " + str(letter_counts['s']) + " occurrences")

t: 17584 occurrences
s: 11830 occurrences
```

Notice that in the for loop, we no longer need to explicitly ask whether the current letter is an ‘s’ or ‘t’. The increment step on line 11 works for the counter associated with whatever the current character is. Our code is now accumulating counts for all letters, not just ‘s’ and ‘t’.

As a final refinement, consider replacing lines 5-11 above with this for loop:
```
for c in txt:
   letter_counts[c] = letter_counts.get(c, 0) + 1
```
This loop uses the get method to retrieve the count for the letter in the variable c. If no such key is present, get returns 0, and letter_counts[c] is set to 1 (0 + 1 = 1). If the key is present, get retrieves its value, which is then incremented.

Consider example ac10_5_5 above. After the program runs, which of the following will print out True if there are more occurrences of e than t in the text of “A Study in Scarlet,” and False if t occurred more frequently?

    print(letter_counts['e'] > letter_counts['t'])
    
The print statements at the end of program ac10_5_5 above pick out the specific keys ‘t’ and ‘s’. Generalize that to print out the occurrence counts for all of the characters. To pass the unit tests, your output must use the same format as the original program above.
```
f = open('scarlet.txt', 'r')
txt = f.read()
letter_counts = {}
for c in txt:
    if c not in letter_counts:
        letter_counts[c] = 0

    letter_counts[c] = letter_counts[c] + 1

# Write a loop that prints the letters and their counts
for c in letter_counts.keys():
    print(c + ": " + str(letter_counts[c]) + " occurrences")
    
T: 699 occurrences
h: 12892 occurrences
e: 25410 occurrences
 : 43507 occurrences
P: 203 occurrences
r: 12054 occurrences
o: 15506 occurrences
j: 214 occurrences
c: 5121 occurrences
t: 17584 occurrences
G: 235 occurrences
u: 5665 occurrences
n: 13714 occurrences
b: 2741 occurrences
g: 4017 occurrences
E: 270 occurrences
B: 156 occurrences
k: 1480 occurrences
f: 4223 occurrences
A: 389 occurrences
S: 404 occurrences
d: 9013 occurrences
y: 3721 occurrences
I: 1358 occurrences
a: 15872 occurrences
l: 7445 occurrences
,: 3137 occurrences
C: 185 occurrences
D: 205 occurrences

: 5155 occurrences
i: 12695 occurrences
s: 11830 occurrences
w: 4745 occurrences
m: 5097 occurrences
v: 1906 occurrences
.: 2785 occurrences
Y: 201 occurrences
p: 3337 occurrences
-: 609 occurrences
L: 256 occurrences
:: 91 occurrences
J: 116 occurrences
1: 103 occurrences
2: 54 occurrences
0: 27 occurrences
8: 24 occurrences
[: 52 occurrences
#: 1 occurrences
4: 32 occurrences
]: 52 occurrences
R: 181 occurrences
9: 21 occurrences
5: 21 occurrences
F: 206 occurrences
7: 17 occurrences
3: 31 occurrences
*: 28 occurrences
O: 193 occurrences
H: 546 occurrences
U: 82 occurrences
N: 240 occurrences
K: 20 occurrences
q: 153 occurrences
': 592 occurrences
x: 330 occurrences
M: 191 occurrences
(: 23 occurrences
_: 34 occurrences
W: 286 occurrences
): 23 occurrences
z: 140 occurrences
": 1795 occurrences
?: 208 occurrences
!: 86 occurrences
;: 104 occurrences
V: 30 occurrences
6: 19 occurrences
Q: 2 occurrences
è: 1 occurrences
é: 2 occurrences
ñ: 4 occurrences
Z: 2 occurrences
&: 2 occurrences
/: 25 occurrences
%: 1 occurrences
X: 2 occurrences
@: 2 occurrences
$: 2 occurrences
```

n the solution to the problem above, note that only those letters that actually occur in the text are shown. Some punctuation marks that are possible in English, but were never used in the text, are omitted completely. The blank line partway through the output may surprise you. That’s actually saying that the newline character, \n, appears 5155 times in the text. In other words, there are 5155 lines of text in the file. Let’s test that hypothesis. Run the following example and check its output:
```
f = open('scarlet.txt', 'r')
txt_lines = f.readlines()
# now txt_lines is a list, where each item is one
# line of text from the story
print(len(txt_lines))

5155
```

Split the string sentence into a list of words, then create a dictionary named word_counts that contains each word and the number of times it occurs.
```
sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."

word_counts = {}

for word in sentence.split():
   word_counts[word] = word_counts.get(word, 0) + 1
```

Create a dictionary called char_d. The keys of the dictionary should be each character in stri, and the value for each key should be how many times the character occurs in the string.
```
stri = "what can I do"

char_d = {}
for c in stri:
   char_d[c] = char_d.get(c, 0) + 1
```

Data file: scarlet.txt
