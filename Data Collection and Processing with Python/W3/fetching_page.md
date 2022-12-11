# Fetching a page

The web works with a metaphor of “pages”. When you put a URL into a browser, you see a “page” of content.

For example, if you visit https://github.com/RunestoneInteractive/RunestoneServer, you will see the home page for the open source project whose contents are used to run this online textbook.

The browser is just a computer program that fetches the contents and displays them in a nice way. If you want to see what the contents are, in plain text, right click your mouse on the page and select View source, or whatever the equivalent is in your browser.

## Fetching in python with requests.get

You don’t need to use a browser to fetch the contents of a page, though. In Python, there’s a module available, called requests. You can use the get function in the requests module to fetch the contents of a page.

### Note
For illustration purposes, try visiting https://api.datamuse.com/words?rel_rhy=funny in your browser. It returns data in JSON format, not in HTML. Your browser will display the results, information about some words that rhyme with “funny”, but it won’t look like a normal web page. Then try running the code below to fetch the same text string in a python program. Try changing “funny” to some other word, both in the browser, and in the code below. You’ll see that, either way, you are retrieving the same thing, the datamuse API’s response to your request for words that rhyme with some word that you are sending as a query parameter.

```
import requests
import json

page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
print(type(page))
print(page.text[:150]) # print the first 150 characters
print(page.url) # print the url that was fetched
print("------")
x = page.json() # turn page.text into a python object
print(type(x))
print("---first item in the list---")
print(x[0])
print("---the whole list, pretty printed---")
print(json.dumps(x, indent=2)) # pretty print the results

<class 'requests.Response'>
[{"word":"money","score":4415,"numSyllables":2},{"word":"honey","score":1206,"numSyllables":2},{"word":"sunny","score":717,"numSyllables":2},{"word":"
https://api.datamuse.com/words?rel_rhy=funny
------
<class 'list'>
---first item in the list---
{'word': 'money', 'score': 4415, 'numSyllables': 2}
---the whole list, pretty printed---
[{"word":"money","score":4415,"numSyllables":2},{"word":"honey","score":1206,"numSyllables":2},{"word":"sunny","score":717,"numSyllables":2},{"word":"bunny","score":702,"numSyllables":2},{"word":"blini","score":613,"numSyllables":2},{"word":"gunny","score":449,"numSyllables":2},{"word":"tunny","score":301,"numSyllables":2},{"word":"sonny","score":286,"numSyllables":2},{"word":"dunny","score":245,"numSyllables":2},{"word":"runny","score":225,"numSyllables":2},{"word":"thunny","score":222,"numSyllables":2},{"word":"aknee","score":179,"numSyllables":2},{"word":"squinny","score":170,"numSyllables":2},{"word":"fiat money","score":160,"numSyllables":4},{"word":"gunnie","score":156,"numSyllables":2},{"word":"blood money","score":152,"numSyllables":3},{"word":"squiny","score":151,"numSyllables":2},{"word":"tunney","score":119,"numSyllables":2},{"word":"spinny","score":117,"numSyllables":2},{"word":"pin money","score":107,"numSyllables":3},{"word":"easy money","score":66,"numSyllables":4},{"word":"smart money","score":66,"numSyllables":3},{"word":"earnest money","score":62,"numSyllables":4},{"word":"easter bunny","score":56,"numSyllables":4},{"word":"paper money","score":54,"numSyllables":4},{"word":"pocket money","score":47,"numSyllables":4},{"word":"folding money","score":46,"numSyllables":4},{"word":"conscience money","score":41,"numSyllables":4},{"word":"hush money","score":40,"numSyllables":3},{"word":"prize money","score":37,"numSyllables":3},{"word":"amount of money","score":33,"numSyllables":5},{"word":"for love or money","score":32,"numSyllables":5},{"word":"tight money","score":32,"numSyllables":3},{"word":"ship money","score":30,"numSyllables":3},{"word":"metal money","score":27,"numSyllables":4},{"word":"sum of money","score":23,"numSyllables":4},{"word":"entrance money","score":22,"numSyllables":4},{"word":"cheap money","score":21,"numSyllables":3},{"word":"spending money","score":21,"numSyllables":4},{"word":"token money","score":21,"numSyllables":4},{"word":"waste of money","score":19,"numSyllables":4},{"word":"ransom money","score":18,"numSyllables":4},{"word":"hearth money","score":14,"numSyllables":3},{"word":"munni","score":14,"numSyllables":2},{"word":"bunnie","score":2,"numSyllables":2},{"word":"euromoney","score":2,"numSyllables":4},{"word":"smartmoney","score":2,"numSyllables":3},{"word":"anyone he","numSyllables":4},{"word":"begun he","numSyllables":3},{"word":"bunney","numSyllables":2},{"word":"ca ne","numSyllables":2},{"word":"done he","numSyllables":2},{"word":"donne e","numSyllables":2},{"word":"everyone he","numSyllables":4},{"word":"fun he","numSyllables":2},{"word":"grandson he","numSyllables":3},{"word":"gun he","numSyllables":2},{"word":"handgun he","numSyllables":3},{"word":"kun hee","numSyllables":2},{"word":"le ne","numSyllables":2},{"word":"lunney","numSyllables":2},{"word":"lunny","numSyllables":2},{"word":"none e","numSyllables":2},{"word":"none he","numSyllables":2},{"word":"nun he","numSyllables":2},{"word":"one he","numSyllables":2},{"word":"one knee","numSyllables":2},{"word":"pun he","numSyllables":2},{"word":"run e","numSyllables":2},{"word":"run he","numSyllables":2},{"word":"shotgun he","numSyllables":3},{"word":"someone e","numSyllables":3},{"word":"someone he","numSyllables":3},{"word":"son e","numSyllables":2},{"word":"son he","numSyllables":2},{"word":"sun e","numSyllables":2},{"word":"sun he","numSyllables":2},{"word":"ton he","numSyllables":2},{"word":"ton ne","numSyllables":2},{"word":"un e","numSyllables":2},{"word":"un he","numSyllables":2},{"word":"un ne","numSyllables":2},{"word":"un ni","numSyllables":2},{"word":"won he","numSyllables":2}]
```

## More Details of Response objects

Once we run requests.get, a python object is returned. It’s an instance of a class called Response that is defined in the requests module. We won’t look at it’s definition. Think of it as analogous to the Turtle class. Each instance of the class has some attributes; different instances have different values for the same attribute. All instances can also invoke certain methods that are defined for the class.

In the Runestone environment, we have a very limited version of the requests module available. The Response object has only two attributes that are set, and one method that can be invoked.

    The .text attribute. It contains the contents of the file or other information available from the url (or sometimes an error message).

    The .url attribute. We will see later that requests.get takes an optional second parameter that is used to add some characters to the end of the base url that is the first parameter. The .url attribute displays the full url that was generated from the input parameters. It can be helpful for debugging purposes; you can print out the URL, paste it into a browser, and see exactly what was returned.

    The .json() method. This converts the text into a python list or dictionary, by passing the contents of the .text attribute to the jsons.loads function.

The full Requests module provides some additional attributes in the Response object. These are not implemented in the Runestone environment.

    The .status_code attribute.

        When a server thinks that it is sending back what was requested, it sends the code 200.

        When the requested page doesn’t exist, it sends back code 404, which is sometimes described as “File Not Found”.

        When the page has moved to a different location, it sends back code 301 and a different URL where the client is supposed to retrieve from. In the full implementation of the requests module, the get function is so smart that when it gets a 301, it looks at the new url and fetches it. For example, github redirects all requests using http to the corresponding page using https (the secure http protocol). Thus, when we ask for http://github.com/presnick/runestone, github sends back a 301 code and the url https://github.com/presnick/runestone. The requests.get function then fetches the other url. It reports a status of 200 and the updated url. We have to do further inquire to find out that a redirection occurred (see below).

    The .headers attribute has as its value a dictionary consisting of keys and values. To find out all the headers, you can run the code and add a statement print(p.headers.keys()). One of the headers is ‘Content-type’. Some possible values are text/html; charset-utf-8 and application/json; charset=utf-8.

    The .history attribute contains a list of previous responses, if there were redirects.

To summarize, a Response object, in the full implementation of the requests module has the following useful attributes that can be accessed in your program:

    .text

    .url

    .json()

    .status_code (not available in Runestone implementation)

    .headers (not available in Runestone implementation)

    .history (not available in Runestone implementation)

## Using requests.get to encode URL parameters

Fortunately, when you want to pass information as a URL parameter value, you don’t have to remember all the substitutions that are required to encode special characters. Instead, that capability is built into the requests module.

The get function in the requests module takes an optional parameter called params. If a value is specified for that parameter, it should be a dictionary. The keys and values in that dictionary are used to append something to the URL that is requested from the remote site.

For example, in the following, the base url is https://google.com/search. A dictionary with two parameters is passed. Thus, the whole url is that base url, plus a question mark, “?”, plus a “q=…” and a “tbm=…” separated by an “&”. In other words, the final url that is visited is https://www.google.com/search?q=%22violins+and+guitars%22&tbm=isch. Actually, because dictionary keys are unordered in python, the final url might sometimes have the encoded key-value pairs in the other order: https://www.google.com/search?tbm=isch&q=%22violins+and+guitars%22. Fortunately, most websites that accept URL parameters in this form will accept the key-value pairs in any order.
```
d = {'q': '"violins and guitars"', 'tbm': 'isch'}
results = requests.get("https://google.com/search", params=d)
print(results.url)
```

Below are more examples of urls, outlining the base part of the url - which would be the first argument when calling request.get() - and the parameters - which would be written as a dictionary and passed into the params argument when calling request.get().

![image](https://user-images.githubusercontent.com/103328611/206882880-25a94119-d3f5-4995-a129-b3c2c0282aa9.png)

Here’s an executable sample, using the optional params parameter of requests.get. It gets the same data from the datamus api that we saw previously. Here, however, the full url is built inside the call to requests.get; we can see what url was built by printing it out, on line 5.
```
import requests

# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
kval_pairs = {'rel_rhy': 'funny'}
page = requests.get("https://api.datamuse.com/words", params=kval_pairs)
print(page.text[:150]) # print the first 150 characters
print(page.url) # print the url that was fetched

[{"word":"money","score":4415,"numSyllables":2},{"word":"honey","score":1206,"numSyllables":2},{"word":"sunny","score":717,"numSyllables":2},{"word":"
https://api.datamuse.com/words?rel_rhy=funny
```


How would you request the URL http://bar.com/goodstuff?greet=hi+there&frosted=no using the requests module?
```
requests.get("http://bar.com/goodstuff", params = {'greet': 'hi there', 'frosted':'no'})
```
The ? and & are added automatically, and the space in hi there is automatically encoded as %3A.


If resp is a Response object returned by a call to requests.get(), which of the following is a way to extract the contents into a python dictionary or list?
resp.json()
json.loads(resp.text)

    .json() invokes the json method
    loads turns a json-formatted string into a list or dictionary
