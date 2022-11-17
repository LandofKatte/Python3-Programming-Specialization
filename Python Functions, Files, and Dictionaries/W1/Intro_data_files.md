# Introduction: Working with Data Files

So far, the data we have used in this book have all been either coded right into the program, or have been entered by the user. In real life data reside in files. For example the images we worked with in the image processing unit ultimately live in files on your hard drive. Web pages, and word processing documents, and music are other examples of data that live in files. In this short chapter we will introduce the Python concepts necessary to use data from files in our programs.

For our purposes, we will assume that our data files are text files–that is, files filled with characters. The Python programs that you write are stored as text files. We can create these files in any of a number of ways. For example, we could use a text editor to type in and save the data. We could also download the data from a website and then save it in a file. Regardless of how the file is created, Python will allow us to manipulate the contents.

In Python, we must open files before we can use them and close them when we are done with them. As you might expect, once a file is opened it becomes a Python object just like all other data. Table 1 shows the functions and methods that can be used to open and close files.

Method Name
	
    Use
	
    Explanation



open
	
    open(filename,'r')

    Open a file called filename and use it for reading. This will return a reference to a file object.



open
	
    open(filename,'w')
	
    Open a file called filename and use it for writing. This will also return a reference to a file object.



close
	
    filevariable.close()

    File use is complete.
