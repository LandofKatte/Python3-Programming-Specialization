# Requests Cookbook

The basic process involves three steps:

    Make the appropriate call to requests.get(). If you have trouble, print out the URL that’s generated and work with it in the browser.

    Extract content from response object, by accessing the .text attribute and calling json.loads if the string is in json format.

    Process the data you’ve extracted. Often, when you get back data in json format, it will be a highly nested data structure. You may only need a little of that data. You may want to review the chapter on nested data and nested iteration, especially the section on the cycle of Understand. Extract. Repeat.

The key to success is to make sure that you debug each of those steps before going on to the next one. This is just a particular case of the general advice we gave early in the course: start small and keep it working at every stage, growing the amount that your program does over time.
