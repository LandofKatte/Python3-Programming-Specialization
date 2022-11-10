# The Accumulator Pattern

One common programming “pattern” is to traverse a sequence, accumulating a value as we go, such as the sum-so-far or the maximum-so-far. That way, at the end of the traversal we have accumulated a single value, such as the sum total of all the items or the largest item.

The anatomy of the accumulation pattern includes:

        initializing an “accumulator” variable to an initial value (such as 0 if accumulating a sum)

        iterating (e.g., traversing the items in a sequence)

        updating the accumulator variable on each iteration (i.e., when processing each item in the sequence)

For example, consider the following code, which computes the sum of the numbers in a list.
```
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
accum = 0
for w in nums:
    accum = accum + w
print(accum)

55
```

In the program above, notice that the variable accum starts out with a value of 0. Next, the iteration is performed 10 times. Inside the for loop, the update occurs. w has the value of current item (1 the first time, then 2, then 3, etc.). accum is reassigned a new value which is the old value plus the current value of w.

This pattern of iterating the updating of a variable is commonly referred to as the accumulator pattern. We refer to the variable as the accumulator. This pattern will come up over and over again. Remember that the key to making it work successfully is to be sure to initialize the variable before you start the iteration. Once inside the iteration, it is required that you update the accumulator.

We can utilize the range function in this situation as well. Previously, you’ve seen it used when we wanted to draw in turtle. There we used it to iterate a certain number of times. We can do more than that though. The range function takes at least one input - which should be an integer - and returns a list as long as your input. While you can provide two inputs, we will focus on using range with just one input. With one input, range will start at zero and go up to - but not include - the input. Here are the examples:
```
print("range(5): ")
for i in range(5):
    print(i)

print("range(0,5): ")
for i in range(0, 5):
    print(i)

# Notice the casting of `range` to the `list`
print(list(range(5)))
print(list(range(0,5)))

# Note: `range` function is already casted as `list` in the textbook
print(range(5))

range(5): 
0
1
2
3
4
range(0,5): 
0
1
2
3
4
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
range(0, 5)
```

One important thing to know about the range function in python3 is that if we want to use it outside of iteration, we have to cast it as a list using list(). Inside the textbook you’ll notice that range works with or without casting it as a list but it is best for you to try and get into the habit of casting it as a list. Here’s how you could use the range function in the previous problem.
```
accum = 0
for w in range(11):
    accum = accum + w
print(accum)

# or, if you use two inputs for the range function

sec_accum = 0
for w in range(1,11):
    sec_accum = sec_accum + w
print(sec_accum)

55
55
```
Because the range function is exclusive of the ending number, we have to use 11 as the function input.

We can use the accumulation pattern is count the number of something or to sum up a total. The above examples only covered how to get the sum for a list, but we can also count how many items are in the list if we wanted to.
```
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for w in nums:
    count = count + 1
print(count)

10
```
In this example we don’t make use of w even though the iterator variable (loop variable) is a necessary part of constructing a for loop. Instead of adding the value of w to count we add a 1 to it, because we’re incrementing the value of count when we iterate each time through the loop. Though in this scenario we could have used the len function, there are other cases later on where len won’t be useful but we will still need to count.
