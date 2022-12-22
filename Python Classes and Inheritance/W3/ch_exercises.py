# Below, we have provided buggy code. Add a try/except clause so the code runs without errors. If a blog post didn’t get any likes, a ‘Likes’ key should be added to that dictionary with a value of 0.

#FIX
blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2}, {'Photos': 8, 'Comments': 1, 'Shares': 1}, {'Photos': 3, 'Likes': 19, 'Comments': 3}]

total_likes = 0

for post in blog_posts:
    total_likes = total_likes + post['Likes']


# The code below assigns the 5th letter of each word in food to the new list fifth. However, the code currently produces errors. Insert a try/except clause that will allow the code to run and produce of list of the 5th letter in each word. If the word is not long enough, it should not print anything out. Note: The pass statement is a null operation; nothing will happen when it executes.

#FIX
food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]
fifth = []

for x in food:
    fifth.append(x[4])
