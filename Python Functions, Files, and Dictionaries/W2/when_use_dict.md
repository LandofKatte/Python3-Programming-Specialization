# When to use a dictionary

Now that you have experience using lists and dictionaries, you will have to decide which one is best to use in each situation. The following guidelines will help you recognize when a dictionary will be beneficial:

    When a piece of data consists of a set of properties of a single item, a dictionary is often better. You could try to keep track mentally that the zip code property is at index 2 in a list, but your code will be easier to read and you will make fewer mistakes if you can look up mydiction[‘zipcode’] than if you look up mylst[2].

    When you have a collection of data pairs, and you will often have to look up one of the pairs based on its first value, it is better to use a dictionary than a list of (key, value) tuples. With a dictionary, you can find the value for any (key, value) tuple by looking up the key. With a list of tuples you would need to iterate through the list, examining each pair to see if it had the key that you want.

    On the other hand, if you will have a collection of data pairs where multiple pairs share the same first data element, then you can’t use a dictionary, because a dictionary requires all the keys to be distinct from each other.
