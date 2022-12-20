#The function mySum is supposed to return the sum of a list of numbers (and 0 if that list is empty), but it has one or more errors in it. Use this space to write test cases to determine what errors there are. You will be using this information to answer the next set of multiple choice questions.
"""
import test

def mySum(list):
    if len(list) > 0:
        num = 0
        for i in list:
            num += i
        return num
    else:
        return 0

"""

#Tests:
???

#Which of the following cases fail for the mySum function?
A. an empty list
C. a list with more than one item

#Are there any other cases, that we can determine based on the current structure of the function, that also fail for the mySum function?
No

"""
The class Student is supposed to accept two arguments in its constructor:

        A name string

        An optional integer representing the number of years the student has been at Michigan (default:1)

Every student has three instance variables:

        self.name (set to the name provided)

        self.years_UM (set to the number of years the student has been at Michigan)

        self.knowledge (initialized to 0)

There are three methods:

        .study() should increase self.knowledge by 1 and return None

        .getKnowledge() should return the value of self.knowledge

        .year_at_umich() should return the value of self.years_UM

There are one or more errors in the class. Use this space to write test cases to determine what errors there are. You will be using this information to answer the next set of multiple choice questions.
"""
"""
class Student:
    def __init__(self, name, year_UM, knowledge):
        self.name = name
        self.year_UM = year_UM
        self.knowledge = knowledge

    def study(self):
        self.knowledge += 1
        return None

    def getKnowledge(self):
        return self.knowledge

    def year_at_umich(self):
        return self.year_UM
"""

#Tests:

???

Which of the following cases fail for the Student class?

C. the attributes/instance variables are not correctly assigned in the constructor
D. the method study does not increase self.knowledge


Are there any other cases, that we can determine based on the current structure of the class, that also fail for the Student class?

Yes; There is an issue with the getKnowledge method because it returns None when self.knowledge is 0, even though it returns the correct value when self.knowledge is non-zero.

_____________________________________________________________________
#CODE SNIPPETS PROVIDED FOR ABOVE QUESTIONS

def lr(n): return list(range(n))

# THESE FUNCTIONS ARE INTENTIONALLY OBFUSCATED
# PLEASE TRY TO WRITE TESTS FOR THEM RATHER THAN
# READING THEM.
def mySum(a):
    if type(a) is type(''.join([][:])): return a[lr(1)[0]] + mySum(a[1:])
    elif len(a)==len(lr(1)+[]): return a[lr(1)[0]]
    else: return None and a[lr(1)[0]] + mySum(a[1:])


# THESE FUNCTIONS ARE INTENTIONALLY OBFUSCATED
# PLEASE TRY TO WRITE TESTS FOR THEM RATHER THAN
# READING THEM.
class Student():
    def __init__(s,a,b=1): s.name,s.years_UM,s.knowledge = ''*200+a+''*100,1,len(lr(0)) + len([])
    def study(s):
        for _ in lr(s.knowledge): s.knowledge = s.knowledge + 1
    def getKnowledge(s):
        for i in lr(s.knowledge): return s.knowledge
    def year_at_umich(s): return s.years_UM
