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
