#Write code to assign the string "You can apply to SI!" to output if the string "SI 106" is in the list courses. If it is not in courses, assign the value "Take SI 106!" to the variable output.

courses = ["ENGR 101", "SI 110", "ENG 125", "SI 106", "CHEM 130"]

if "SI 106" in courses:
    output = "You can apply to SI!"
else:
    output = "Take SI 106!"
    
___________________________________

#Create a variable, b, and assign it the value of 15. Then, write code to see if the value b is greater than that of a. If it is, a’s value should be multiplied by 2. If the value of b is less than or equal to a, nothing should happen. Finally, create variable c and assign it the value of the sum of a and b.

a = 20
b = 15

if b > a:
    a * 2
print(a)

c = a + b 
________________________________________

Chained Conditionals

#Create one conditional to find whether “false” is in string str1. If so, assign variable output the string “False. You aren’t you?”. Check to see if “true” is in string str1 and if it is then assign “True! You are you!” to the variable output. If neither are in str1, assign “Neither true nor false!” to output.

str1 = "Today you are you! That is truer than true! There is no one alive who is you-er than you!"

if "false" in str1:
    output = "False. You aren’t you?"   
elif "true" in str1:
    output = "True! You are you!"
else:
    output = "Neither true nor false!"    
______________________________________________
#Create an empty list called resps. Using the list percent_rain, for each percent, if it is above 90, add the string ‘Bring an umbrella.’ to resps, otherwise if it is above 80, add the string ‘Good for the flowers?’ to resps, otherwise if it is above 50, add the string ‘Watch out for clouds!’ to resps, otherwise, add the string ‘Nice day!’ to resps. Note: if you’re sure you’ve got the problem right but it doesn’t pass, then check that you’ve matched up the strings exactly.

percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
resps = []

for i in percent_rain:
    if i > 90:
        resps.append("Bring an umbrella.")
    elif i > 80:
        resps.append("Good for the flowers?")                   
    elif i > 50:
        resps.append("Watch out for clouds!")
    else:
        resps.append("Nice day!")  
____________________________________________________
#We have created conditionals for you to use. Do not change the provided conditional statements. Find an integer value for x that will cause output to hold the values True and None. (Drawing diagrams or flow charts for yourself may help!)

x = 65
output = []

if x > 63:
    output.append(True)
elif x > 55:
    output.append(False)
else:
    output.append("Neither")

if x > 67:
    output.append(True)
else:
    output.append(None)
