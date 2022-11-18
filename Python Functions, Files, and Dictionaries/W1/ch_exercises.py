Exercises

Below are the datafiles that you have been using so far, and will continue to use for the rest of the chapter.

The file below is travel_plans.txt.

This summer I will be travelling.
I will go to...
Italy: Rome
Greece: Athens
England: London, Manchester
France: Paris, Nice, Lyon
Spain: Madrid, Barcelona, Granada
Austria: Vienna
I will probably not even want to come back!
However, I wonder how I will get by with all the different languages.
I only know English!

The file below is school_prompt.txt.

Writing essays for school can be difficult but
many students find that by researching their topic that they
have more to say and are better informed. Here are the university
we require many undergraduate students to take a first year writing requirement
so that they can
have a solid foundation for their writing skills. This comes
in handy for many students.
Different schools have different requirements, but everyone uses
writing at some point in their academic career, be it essays, research papers,
technical write ups, or scripts.

The file below is emotion_words.txt.

Sad upset blue down melancholy somber bitter troubled
Angry mad enraged irate irritable wrathful outraged infuriated
Happy cheerful content elated joyous delighted lively glad
Confused disoriented puzzled perplexed dazed befuddled
Excited eager thrilled delighted
Scared afraid fearful panicked terrified petrified startled
Nervous anxious jittery jumpy tense uneasy apprehensive
____________________________________________________________



The following sample file called studentdata.txt contains one line for each student in an imaginary class. The students name is the first thing on each line, followed by some exam scores. The number of scores might be different for each student.

joe 10 15 20 30 40
bill 23 16 19 22
sue 8 22 17 14 32 17 24 21 2 9 11 17
grace 12 28 21 45 26 10
john 14 32 25 16 89

Using the text file studentdata.txt write a program that prints out the names of students that have more than six quiz scores.

# Hint: first see if you can write a program that just prints out the number of scores on each line
# Then, make it print the number only if the number is at least six
# Then, switch it to printing the name instead of the number

f = open("studentdata.txt", "r")

for aline in f:
    items = aline.split()
    if len(items[1:]) > 6:
        print(items[0])

f.close()

#Sue
_________________________________________________________________________________________________

#Create a list called destination using the data stored in travel_plans.txt. Each element of the list should contain a line from the file that lists a country and cities inside that country. Hint: each line that has this information also has a colon : in it.
    
f = open("travel_plans.txt", "r")
line = f.readlines()
destination = []

for words in line:
    if ":" in words:
        destination.append(words)
f.close()
print (destination)

#['Italy: Rome\n', 'Greece: Athens\n', 'England: London, Manchester\n', 'France: Paris, Nice, Lyon\n', 'Spain: Madrid, Barcelona, Granada\n', 'Austria: Vienna\n']
_________________________________________________________________________________________________

#Create a list called j_emotions that contains every word in emotion_words.txt that begins with the letter “j”.

file = open("emotion_words.txt", "r")
f = file.read()
j_emotions = []
words = f.split()
for line in words:
    if "j" in line:
        j_emotions.append(line)
        print(j_emotions)

file.close()

#['joyous', 'jittery', 'jumpy']
_________________________________________________________________________________________________
