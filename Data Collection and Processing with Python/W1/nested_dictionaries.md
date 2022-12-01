# Nested Dictionaries

Just as lists can contain items of any type, the value associated with a key in a dictionary can also be an object of any type. In particular, it is often useful to have a list or a dictionary as a value in a dictionary. And of course, those lists or dictionaries can also contain lists and dictionaries. There can be many layers of nesting.

Only the values in dictionaries can be objects of arbitrary type. The keys in dictionaries must be one of the immutable data types (numbers, strings, tuples).


Which of the following is a legal assignment statement, after the following code executes?
```
d = {'key1': {'a': 5, 'c': 90, 5: 50}, 'key2':{'b': 3, 'c': "yes"}}
```
d[5] = {1: 2, 3: 4}
d['key1']['d'] = d['key2']

5 is a valid key; {1:2, 3:4} is a dictionary with two keys, and is a valid value to associate with key 5.
d['key2'] is {'b': 3, 'c': "yes"}, a python object. It can be bound to the key 'd' in a dictionary {'a': 5, 'c': 90, 5: 50}


Extract the value associated with the key color and assign it to the variable color. Do not hard code this.
```
info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
      }

color = info['personal_data']['physical_features']['color']
```
