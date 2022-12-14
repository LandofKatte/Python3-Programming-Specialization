#rainfall_mi is a string that contains the average number of inches of rainfall in Michigan for every month (in inches) with every month separated by a comma. Write code to compute the number of months that have more than 3 inches of rainfall. Store the result in the variable num_rainy_months. In other words, count the number of items with values > 3.0.

rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
rainfall = rainfall_mi.split(",")
num_rainy_months = 0

for rain in rainfall:
    rain = float(rain)
    if rain > 3.0:
        num_rainy_months += 1
        
print(num_rainy_months)

#5
____________________________________________________

#The variable sentence stores a string. Write code to determine how many words in sentence start and end with the same letter, including one-letter words. Store the result in the variable same_letter_count.

sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

# Write your code here.
same_letter_count = 0
sentence=sentence.split()

for word in sentence:
    if word[0]== word[-1]:
        same_letter_count+=1
print(same_letter_count)

#2
________________________________________________

#Write code to count the number of strings in list items that have the character w in it. Assign that number to the variable acc_num.

#HINT 1: Use the accumulation pattern!
#HINT 2: the in operator checks whether a substring is present in a string.

items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
count = 0

for i in items:
    if 'w' in i:
        count += 1
acc_num = count
___________________________________________________

#Write code that counts the number of words in sentence that contain either an āaā or an āeā. Store the result in the variable num_a_or_e.

#Note 1: be sure to not double-count words that contain both an a and an e.
#HINT 1: Use the in operator.
#HINT 2: You can either use or or elif.

sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
num_a_or_e = 0

for word in sentence.split():
    if ('a' in word) or ('e' in word):
        num_a_or_e += 1

print(num_a_or_e)

#14
_______________________________________________

#Write code that will count the number of vowels in the sentence s and assign the result to the variable num_vowels. For this problem, vowels are only a, e, i, o, and u. Hint: use the in operator with vowels.

s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']

# Write your code here.
num_vowels = 0

for i in s:
    if i in vowels:
        num_vowels+=1
    
print(num_vowels)

#32
___________________________________

#Create one conditional so that if āFriendlyā is in w, then āFriendly is here!ā should be assigned to the variable wrd. If itās not, check if āFriendā is in w. If so, the string āFriend is here!ā should be assigned to the variable wrd, otherwise āNo variation of friend is in here.ā should be assigned to the variable wrd. (Also consider: does the order of your conditional statements matter for this problem? Why?)

w = "Friendship is a wonderful human experience!"

for i in w:
    if "Friendly" in w:
        wrd = str("Friendly is here!")
    elif "Friend" in w:
        wrd = str("Friend is here!")
    else:
        wrd = str("No variation of friend is in here.")
print(wrd)

#Friend is here!
____________________________________________________________

#We have written conditionals for you to use. Create the variable x and assign it some integer so that at the end of the code, output will be assigned the string "Consistently working".

x = 8

if x >= 10:
    output = "working"
else:
    output = "Still working"
if x > 12:
    output = "Always working"
elif x < 7:
    output = "Forever working"
else:
    output = "Consistently working"    
___________________________________________

#Write code so that if "STATS 250" is in the list schedule, then the string "You could be in Information Science!" is assigned to the variable resp. Otherwise, the string "That's too bad." should be assigned to the variable resp.

schedule = ["SI 106", "STATS 250", "SI 110", "ENGLISH 124/125"]

if "STATS 250" in schedule:
        resp = "You could be in Information Science!"
else:
        resp = "That's too bad."
print(resp)

#You could be in Information Science!
_____________________________________________________________________

#Create the variable z whose value is 30. Write code to see if z is greater than y. If so, add 5 to yās value, otherwise do nothing. Then, multiply z and y, and assign the resulting value to the variable x.

y = 22
z = 30

if z > y:
    y += 5
x = z * y
print(x)

#810
_____________________________________

#For each string in wrd_lst, find the number of characters in the string. If the number of characters is less than 6, add 1 to accum so that in the end, accum will contain an integer representing the total number of words in the list that have fewer than 6 characters.

wrd_lst = ["Hello", "activecode", "Java", "C#", "Python", "HTML and CSS", "Javascript", "Swift", "php"]

accum = 0
for x in wrd_lst:
    if len(x)<6:
        accum = accum +1
print(accum)

#5
