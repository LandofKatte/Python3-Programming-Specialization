#It is possible to name the days 0 thru 6 where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights you would return home on a Saturday (day 6). Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the number of day of the week you will return on.

current_day_string = input("What is the current day number-days 0 thru 6 where day 0 is Sunday and day 6 is Saturday? ")
return_day_string = input("How many days until you return home? ")

current_day_int = int(current_day_string)
return_day_int = int(return_day_string)

day = current_day_int + return_day_int

return_home = day % 7

print(return_home)
