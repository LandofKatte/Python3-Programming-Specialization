#Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).

def sublist(list):
    new_list=[]
    i=0
    while i < len(list):
        if list[i] == 5:
            break
        new_list.append(list[i])
        i=i+1
    return new_list

#Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.

def check_nums(list):
    i=0
    new_list=[]
    while i < len(list):
        if list[i] == 7:
            break
        new_list.append(list[i])
        i=i+1
    return new_list
  
#Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).

def sublist(list):
    i=0
    New_list=[]
    
    while i < len(list):
        if list[i] == "STOP":
            break
        New_list.append(list[i])
        i=i+1
    return New_list
  
#Write a function called stop_at_z that iterates through a list of strings. Using a while loop, append each string to a new list until the string that appears is “z”. The function should return the new list.

def stop_at_z(list):
   i = 0
   while i < len(list):

       if (list[i] == 'z'):
           return list[0:i]
       i+=1
   return list[0:i]

#Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does the same thing, but using a while loop instead of a for loop. Assign the accumulated total in the while loop code to the variable sum2. Once complete, sum2 should equal sum1.


lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x

i = 0
sum2 = 0
while i < len(lst):
    sum2 = sum2 + lst[i]
    i = i + 1
    
#Challenge: Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’. What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.) If you want to make this even more of a challenge, do this without slicing

def beginning(lst):
    i = 0 
    new_lst = []
    while i < len(lst):
        if lst[i] != "bye" :
            new_lst.append(lst[i])
        else :
            break
        i = i + 1
    return new_lst[:10]

_____________________________________________________________________________

#Create a function called mult that has two parameters, the first is required and should be an integer, the second is an optional parameter that can either be a number or a string but whose default is 6. The function should return the first parameter multiplied by the second.

def mult(a, b=6):
    return a * b

#The following function, greeting, does not work. Please fix the code so that it runs without error. This only requires one change in the definition of the function.
def greeting(greeting="Hello ", name, excl="!"):
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))
----------------------------------
def greeting(name, greeting="Hello ", excl="!"):
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))

Hello Bob!
Hello !
Hello Bob!!!

#Below is a function, sum, that does not work. Change the function definition so the code works. The function should still have a required parameter, intx, and an optional parameter, intz with a defualt value of 5.
def sum(intz=5, intx):
    return intz + intx
-----------------------
def sum(intx, intz=5):
    return intz + intx

#Write a function, test, that takes in three parameters: a required integer, an optional boolean whose default value is True, and an optional dictionary, called dict1, whose default value is {2:3, 4:5, 6:8}. If the boolean parameter is True, the function should test to see if the integer is a key in the dictionary. The value of that key should then be returned. If the boolean parameter is False, return the boolean value “False”.

def test(x, abool = True, dict1 = {2:3, 4:5, 6:8}):
    return abool and dict1.get(x, False)

#Write a function called checkingIfIn that takes three parameters. The first is a required parameter, which should be a string. The second is an optional parameter called direction with a default value of True. The third is an optional parameter called d that has a default value of {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}. Write the function checkingIfIn so that when the second parameter is True, it checks to see if the first parameter is a key in the third parameter; if it is, return True, otherwise return False.

#But if the second paramter is False, then the function should check to see if the first parameter is not a key of the third. If it’s not, the function should return True in this case, and if it is, it should return False.

def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction:
        return bool(d.get(a, False)) and bool(d[a])
    elif not direction:
        return not bool(d.get(a, False))
    
#We have provided the function checkingIfIn such that if the first input parameter is in the third, dictionary, input parameter, then the function returns that value, and otherwise, it returns False. Follow the instructions in the active code window for specific variable assignmemts.
def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# Call the function so that it returns False and assign that function call to the variable c_false

# Call the fucntion so that it returns True and assign it to the variable c_true

# Call the function so that the value of fruit is assigned to the variable fruit_ans

# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
---------------------------------------------------------------------------------------------------------------------------
def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# Call the function so that it returns False and assign that function call to the variable c_false
c_false = checkingIfIn('peas')
# Call the fucntion so that it returns True and assign it to the variable c_true
c_true = checkingIfIn('apples', False, {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1})
# Call the function so that the value of fruit is assigned to the variable fruit_ans
fruit_ans= checkingIfIn('fruit')
# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
param_check = checkingIfIn('potatos', False, {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1})
