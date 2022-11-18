# Things to remember

Use relative path: easier portability

Make sure to close an open file.... OR use with a special word "with" and then there's another special word "as" After the word "as" you have a variable name "md"....
*md*.method
use "with"

First, you have to pass a string, the file's name,
as the first parameter when you call the open function.
If you have a variable name whose value is the file name,
don't put it in quotes.
If you have a literal file name,
do put it in quotes.
Second, you have to keep track of the distinction between the file name,
a string, the file object,
does the thing return by the open function,
and the file's contents which you get by doing operations on the file object. 
