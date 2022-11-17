#For each word in the list verbs, add an -ing ending. Overwrite the old list so that verbs has the same words with ing at the end of each one.
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]

verbs=[i+"ing" for i in verbs]
print(verbs)

['kayaking', 'crying', 'walking', 'eating', 'drinking', 'flying']
_________________________________________________________
#In XYZ University, upper level math classes are numbered 300 and up. Upper level English classes are numbered 200 and up. Upper level Psychology classes are 400 and up. Create two lists, upper and lower. Assign each course in classes to the correct list, upper or lower. HINT: remember, you can convert some strings to different types!

classes = ["MATH 150", "PSYCH 111", "PSYCH 313", "PSYCH 412", "MATH 300", "MATH 404", "MATH 206", "ENG 100", "ENG 103", "ENG 201", "PSYCH 508", "ENG 220", "ENG 125", "ENG 124"]
upper=[]
lower=[]

for i in classes:
    new=i.split()
    if (new[0]=='MATH') and (int(new[1])>=300):
        upper.append(i)
    elif (new[0]=='ENG') and (int(new[1])>=200): 
        upper.append(i)
    elif (new[0]=='PSYCH') and (int(new[1])>=400): 
        upper.append(i) 
    else:
        lower.append(i)
        
print("upper=",upper)  
print("lower=",lower)   
_________________________________________________________


Starting with the list myList = [76, 92.3, ‘hello’, True, 4, 76], write Python statements to do the following:

    Append “apple” and 76 to the list.

    Insert the value “cat” at position 3.

    Insert the value 99 at the start of the list.

    Find the index of “hello”.

    Count the number of 76s in the list.

    Remove the first occurrence of 76 from the list.

    Remove True from the list using pop and index.


myList = [76, 92.3, 'hello', True, 4, 76]

myList.append("apple")         # a
myList.append(76)              # a
myList.insert(3, "cat")        # b
myList.insert(0, 99)           # c

print(myList.index("hello"))   # d
print(myList.count(76))        # e
myList.remove(76)              # f
myList.pop(myList.index(True)) # g

print (myList)

[99, 92.3, 'hello', 'cat', 4, 76, 'apple', 76]
_____________________________________________________________________________
#The module keyword determines if a string is a keyword. e.g. keyword.iskeyword(s) where s is a string will return either True or False, depending on whether or not the string is a Python keyword. Import the keyword module and test to see whether each of the words in list test are keywords. Save the respective answers in a list, keyword_test.

import keyword

test = ["else", "integer", "except", "elif"]
keyword_test = []

for word in test:
        keyword_test.append(keyword.iskeyword(word))
print(keyword_test)

[True, False, True, True]
_____________________________________________________________________________
The string module provides sequences of various types of Python characters. It has an attribute called digits that produces the string ‘0123456789’. Import the module and assign this string to the variable nums. Below, we have provided a list of characters called chars. Using nums and chars, produce a list called is_num that consists of tuples. The first element of each tuple should be the character from chars, and the second element should be a Boolean that reflects whether or not it is a Python digit.

chars = ['h', '1', 'C', 'i', '9', 'True', '3.1', '8', 'F', '4', 'j']

.........EDIT.............


______________________________________________________________________________

#For each character in the string saved in ael, append that character to a list that should be saved in a variable app.

ael = "python!"
app = []

for i in ael:
    app.append(i)
print(app)

['p', 'y', 't', 'h', 'o', 'n', '!']
__________________________________________________________________________________

#For each string in wrds, add ‘ed’ to the end of the word (to make the word past tense). Save these past tense words to a list called past_wrds.

wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds = []

for pst in range(len(wrds)):
    past_wrds.append(wrds[pst]+"ed")
print(past_wrds)

['ended', 'worked', 'played', 'started', 'walked', 'looked', 'opened', 'rained', 'learned', 'cleaned']
__________________________________________________________________________________________________________
#Below are a set of scores that students have received in the past semester. Write code to determine how many are 90 or above and assign that result to the value a_scores.

scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
new_scores = scores.split(" ")
a_scores = 0

for score in new_scores :
    if int(score) >= 90:
        a_scores +=1
print(a_scores)

10
_________________________________________________
#Write code that uses the string stored in org and creates an acronym which is assigned to the variable acro. Only the first letter of each word should be used, each letter in the acronym should be a capital letter, and there should be nothing to separate the letters of the acronym. Words that should not be included in the acronym are stored in the list stopwords. For example, if org was assigned the string “hello to world” then the resulting acronym should be “HW”.

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"

words = org.split()
acro = ''

for word in words:
    if word in stopwords:
        continue
    acro += word[0].upper()

print(acro)

OHSE
__________________________________________________________
#Write code that uses the string stored in sent and creates an acronym which is assigned to the variable acro. The first two letters of each word should be used, each letter in the acronym should be a capital letter, and each element of the acronym should be separated by a “. ” (dot and space). Words that should not be included in the acronym are stored in the list stopwords. For example, if sent was assigned the string “height and ewok wonder” then the resulting acronym should be “HE. EW. WO”.

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
acro = ""
lst = sent.split()

for i in lst:
    if i in stopwords:
        lst.remove(i)

for j in lst:
    acro = acro + j[0] + j[1]
    if j != lst[-1]:
        acro += ". "

acro = acro.upper()
print(acro)

WA. EA. AI. AR. VI
___________________________________________
#A palindrome is a phrase that, if reversed, would read the exact same. Write code that checks if p_phrase is a palindrome by reversing it and then checking if the reversed version is equal to the original. Assign the reversed version of p_phrase to the variable r_phrase so that we can check your work.

p_phrase = "was it a car or a cat I saw"

r_phrase = p_phrase[::-1]
print(r_phrase)

was I tac a ro rac a ti saw
___________________________________________________
#Provided is a list of data about a store’s inventory where each item in the list represents the name of an item, how much is in stock, and how much it costs. Print out each item in the list with the same formatting, using the .format method (not string concatenation). For example, the first print statment should read The store has 12 shoes, each for 29.99 USD.

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

for temp in inventory:
    temp = temp.split(',')
    str1="The store has{} {}, each for{} USD."
    str1=str1.format(temp[1],temp[0],temp[2])
    print(str1)
    
The store has 12 shoes, each for 29.99 USD.
The store has 20 shirts, each for 9.99 USD.
The store has 25 sweatpants, each for 15.00 USD.
The store has 13 scarves, each for 7.75 USD.
