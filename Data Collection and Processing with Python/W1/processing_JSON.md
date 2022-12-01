# Processing JSON results

JSON stands for JavaScript Object Notation. It looks a lot like the representation of nested dictionaries and lists in python when we write them out as literals in a program, but with a few small differences (e.g., the word null instead of None). When your program receives a JSON-formatted string, generally you will want to convert it into a python object, a list or a dictionary.

Again, python provides a module for doing this. The module is called json. We will be using two functions in this module, loads and dumps.

json.loads() takes a string as input and produces a python object (a dictionary or a list) as output.

Consider, for example, some data that we might get from Apple’s iTunes, in the JSON format:
```
import json
a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
print(a_string)
d = json.loads(a_string)
print("------")
print(type(d))
print(d.keys())
print(d['resultCount'])
# print(a_string['resultCount'])

{
 "resultCount":25,
 "results": [
{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}
------
<class 'dict'>
dict_keys(['resultCount', 'results'])
25
```

The other function we will use is dumps. It does the inverse of loads. It takes a python object, typically a dictionary or a list, and returns a string, in JSON format. It has a few other parameters. Two useful parameters are sort_keys and indent. When the value True is passed for the sort_keys parameter, the keys of dictionaries are output in alphabetic order with their values. The indent parameter expects an integer. When it is provided, dumps generates a string suitable for displaying to people, with newlines and indentation for nested lists or dictionaries. For example, the following function uses json.dumps to make a human-readable printout of a nested data structure.

```
import json
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

d = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2':{'b': 3, 'c': "yes"}}

print(d)
print('--------')
print(pretty(d))

{'key1': {'c': True, 'a': 90, '5': 50}, 'key2': {'b': 3, 'c': 'yes'}}
--------
{"key1":{"5":50,"a":90,"c":true},"key2":{"b":3,"c":"yes"}}
```

Because we can only write strings into a file, if we wanted to convert a dictionary d into a json-formatted string so that we could store it in a file, what would we use?

    json.dumps(d)
    dumps turns a list or dictionary into a json-formatted string
    
Say we had a JSON string in the following format. How would you convert it so that it is a python list?

    entertainment = """[{"Library Data": {"count": 3500, "rows": 10, "locations": 3}}, {"Movie Theater Data": {"count": 8, "rows": 25, "locations": 2}}]"""
    
json.loads(entertainment)
loads (load from string) turns a json-formatted string into a list or dictionary
