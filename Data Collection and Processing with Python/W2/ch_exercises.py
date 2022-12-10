#Write equivalent code using map instead of the manual accumulation below and assign it to the variable test.
things = [3, 5, -4, 7]

accum = []
for thing in things:
    accum.append(thing+1)
print(accum)




#Use manual accumulation to define the lengths function below.
def lengths(strings):
    """lengths takes a list of strings as input and returns a list of numbers that are the lengths
    of strings in the input list. Use manual accumulation!"""
    # fill in this function's definition to make the test pass.



#Now define lengths using map instead.
def lengths(strings):
    """lengths takes a list of strings as input and returns a list of numbers that are the lengths
     of strings in the input list. Use map!"""
     # fill in this function's definition to make the test pass.

      
      
      
#Now define lengths using a list comprehension instead.
def lengths(strings):
    """lengths takes a list of strings as input and returns a list of numbers that are the lengths
    of strings in the input list. Use a list comprehension!"""
    # fill in this function's definition to make the test pass.




#Write a function called positives_Acc that receives list of numbers as the input (like [3, -1, 5, 7]) and returns a list of only the positive numbers, [3, 5, 7], via manual accumulation.
things = [3, 5, -4, 7]





#Write a function called positives_Fil that receives list of things as the input and returns a list of only the positive things, [3, 5, 7], using the filter function.
things = [3, 5, -4, 7]






#Write a function called positives_Li_Com that receives list of things as the input and returns a list of only the positive things, [3, 5, 7], using the list comprehension.
things = [3, 5, -4, 7]






#Define longwords using manual accumulation.
def longwords(strings):
    """Return a shorter list of strings containing only the strings with more than four characters. Use manual accumulation."""
    # write your code here
    
    
    
    
    
    
#Define longwords using filter.
def longwords_Fil(strings):
    """Return a shorter list of strings containing only the strings with more than four characters. Use the filter function."""
    # write your code here



#Define longwords using a list comprehension.
def longwords_Li_Comp(strings):
    """Return a shorter list of strings containing only the strings with more than four characters. Use a list comprehension."""
    # write your code here





#11. Write a function called longlengths that returns the lengths of those strings that have at least 4 characters. Try it with a list comprehension.
#list comprehension--best to use

def longlengths(strings):
    return [len(s) for s in strings if len(s)>=4]

print(longlengths(['a', 'bc', 'def', 'ghij', 'klmno']))

[4, 5]

#or manual accum

def longlengths(strings):
  accum = []
  for s in strings:
    if len(s) >= 4:
      accum.append(len(s))
  return accum

#or map & filter

def longlengths(strings):
    filter_strings = filter(lambda s: len(s) >= 4, strings)
    return map(lambda s: len(s), filtered_strings)

#list?....
# ex return list(map(lambda s: len(s), filtered_strings))
 
  
  
#Write a function called longlengths that returns the lengths of those strings that have at least 4 characters. Try it using map and filter.
def longlengths(strings):
    return None




#Write a function that takes a list of numbers and returns the sum of the squares of all the numbers. Try it using an accumulator pattern.
def sumSquares(L):
    return None

nums = [3, 2, 2, -1, 1]



#Write a function that takes a list of numbers and returns the sum of the squares of all the numbers. Try it using map and sum.
def sumSquares(L):
    return None

nums = [3, 2, 2, -1, 1]




#Use the zip function to take the lists below and turn them into a list of tuples, with all the first items in the first tuple, etc.
L1 = [1, 2, 3, 4]
L2 = [4, 3, 2, 3]
L3 = [0, 5, 0, 5]

tups = []




#Use zip and map or a list comprehension to make a list consisting the maximum value for each position. For L1, L2, and L3, you would end up with a list [4, 5, 3, 5].
L1 = [1, 2, 3, 4]
L2 = [4, 3, 2, 3]
L3 = [0, 5, 0, 5]

maxs = []




#Write code to assign to the variable compri_sample all the values of the key name in the dictionary tester if they are Juniors. Do this using list comprehension.
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}




#Challenge The nested for loop given takes in a list of lists and combines the elements into a single list. Do the same thing using a list comprehension for the list L. Assign it to the variable result2.
def onelist(lst):
    result = []
    for each_list in lst:
        for item in each_list:
            result.append(item)
    return result

L = [["hi", "bye"], ["hello", "goodbye"], ["hola", "adios", "bonjour", "au revoir"]]





#Challenge: Write code to assign to the variable class_sched all the values of the key important classes. Do this using list comprehension.
tester = {'info': [
         {"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science", 'important classes': ['SI 106', 'ENGLISH 125', 'SI 110', 'AMCULT 202']},
         {'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science', "important classes": ['SI 106', 'SI 410', 'PSYCH 111']},
         {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology', 'important classes': ['WOMENSTD 220', 'SOC 101', 'ENS 384']},
         {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science', "important classes": ['SOC 101', 'AMCULT 334', 'EECS 281']},
         {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History', 'important classes': ['ENGLISH 125', 'HIST 259', 'ENGLISH 130']},
         {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior', 'important classes': ['PIANO 101', 'STUDIO 300', 'THEORY 229', 'MUSC 356']}]}





#Challenge: Below, we have provided a list of lists that contain numbers. Using list comprehension, create a new list threes that contains all the numbers from the original list that are divisible by 3. This can be accomplished in one line of code.
nums = [[4, 3, 12, 10], [8, 7, 6], [5, 18, 15, 7, 11], [9, 4], [24, 20, 17], [3, 5]]
