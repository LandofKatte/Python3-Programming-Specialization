# Filter

Now consider another common pattern: going through a list and keeping only those items that meet certain criteria. This is called a filter.
```
def keep_evens(nums):
    new_list = []
    for num in nums:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

print(keep_evens([3, 4, 6, 7, 0, 1]))

[4, 6, 0]
```

Again, this pattern of computation is so common that Python offers a more compact and general way to do it, the filter function. filter takes two arguments, a function and a sequence. The function takes one item and return True if the item should. It is automatically called for each item in the sequence. You don’t have to initialize an accumulator or iterate with a for loop.
```
def keep_evens(nums):
    new_seq = filter(lambda num: num % 2 == 0, nums)
    return list(new_seq)

print(keep_evens([3, 4, 6, 7, 0, 1]))

[4, 6, 0]
```
Exercises:

Write code to assign to the variable filter_testing all the elements in lst_check that have a w in them using filter.
```
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

filter_testing = list(filter(lambda have_w: 'w' in have_w , lst_check))
#to LIST
print(filter_testing)

['watermelon', 'kiwi', 'strawberries']
```

Using filter, filter lst so that it only contains words containing the letter “o”. Assign to variable lst2. Do not hardcode this.
```
lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]

lst2 = list(filter(lambda have_o: 'o' in have_o , lst ))
#LIST
print(lst2)

['halloween', 'wagon', 'moon']
```
