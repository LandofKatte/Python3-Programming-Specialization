#Write code that asks the user to enter a numeric score (0-100). In response, it should print out the score and corresponding letter grade, according to the table below.
Score-----Grade
>= 90-----A
[80-90)---B
[70-80)---C
[60-70)---D
< 60------F
#The square and round brackets denote closed and open intervals. A closed interval includes the number, and open interval excludes it. So 79.99999 gets grade C , but 80 gets grade B.

sc = input("Enter a score from 0 to 100 (decimal points are allowed)")
fl_sc = float(sc)

if fl_sc < 60:
    gr = "F"
elif fl_sc < 70:
    gr = "D"
elif fl_sc < 80:
    gr = "C"
elif fl_sc < 90:
    gr = "B"
else:
    gr = "A"

print("Score", fl_sc, "gets a grade of", gr)
 
__________________________________________________
 
A year is a leap year if it is divisible by 4; however, if the year can be evenly divided by 100, it is NOT a leap year, unless the year is also evenly divisible by 400 then it is a leap year. Write code that asks the user to input a year and output True if it’s a leap year, or False otherwise. Use if statements.

Year
Leap?

1944
True

2011
False

1986
False

1800
False

1900
False

2000
True

2056
True

#Above are some examples of what the output should be for various inputs.
 
years = [1967, 1900, 1400, 1628, 1701, 1217, 1359, 1300, 2000, 1054,
1724, 1000, 1800, 1100, 2100, 1023, 1600, 1500, 1358, 1160,
1700, 1744, 2009, 1200]

is_leap_year = []

for year in years:
    if year % 4 == 0 and year % 100 != 0:
        is_leap_year.append("True")
    elif year % 100 == 0 and year % 400 == 0:
        is_leap_year.append("True")
    else:
        is_leap_year.append("False")

print(is_leap_year)
