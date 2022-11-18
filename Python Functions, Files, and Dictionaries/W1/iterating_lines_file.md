# Iterating over lines in a file

We will now use this file as input in a program that will do some data processing. In the program, we will examine each line of the file and print it with some additional text. Because readlines() returns a list of lines of text, we can use the for loop to iterate through each line of the file.

A line of a file is defined to be a sequence of characters up to and including a special character called the newline character. If you evaluate a string that contains a newline character you will see the character represented as \n. If you print a string that contains a newline you will not see the \n, you will just see its effects (a carriage return).

As the for loop iterates through each line of the file the loop variable will contain the current line of the file as a string of characters. The general pattern for processing each line of a text file is as follows:

for line in myFile.readlines():
    statement1
    statement2
    ...

To process all of our olypmics data, we will use a for loop to iterate over the lines of the file. Using the split method, we can break each line into a list containing all the fields of interest about the athlete. We can then take the values corresponding to name, team and event to construct a simple sentence.

```
olypmicsfile = open("olypmics.txt", "r")

for aline in olypmicsfile.readlines():
    values = aline.split(",")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])

olypmicsfile.close()
```
To make the code a little simpler, and to allow for more efficient processing, Python provides a built-in way to iterate through the contents of a file one line at a time, without first reading them all into a list. Some students find this confusing initially, so we don’t recommend doing it this way, until you get a little more comfortable with Python. But this idiom is preferred by Python programmers, so you should be prepared to read it. And when you start dealing with big files, you may notice the efficiency gains of using it.
```
olypmicsfile = open("olypmics.txt", "r")

for aline in olypmicsfile:
    values = aline.split(",")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])

olypmicsfile.close()
```

### Examples:

```
Sad upset blue down melancholy somber bitter troubled
Angry mad enraged irate irritable wrathful outraged infuriated
Happy cheerful content elated joyous delighted lively glad
Confused disoriented puzzled perplexed dazed befuddled
Excited eager thrilled delighted
Scared afraid fearful panicked terrified petrified startled
Nervous anxious jittery jumpy tense uneasy apprehensive
```
Write code to find out how many lines are in the file emotion_words.txt as shown above. Save this value to the variable num_lines. Do not use the len method.
```
file = open("emotion_words.txt","r")
num_lines = 0

for aline in file.readlines():
    num_lines += 1
print(num_lines)
file.close()

7
```
