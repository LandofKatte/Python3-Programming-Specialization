# Searching for Media on iTunes

You’ve already seen an example using the iTunes API in Generating Request URLs. The iTunes API allows users to search for movies, podcasts, music, music videos, tv shows, and books that are hosted on the iTunes site. You can explore the [official iTunes API documentation.](https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/)

Earlier we showed a possible query for podcasts about Ann Arbor. Now, we’ll show you how to construct it yourself!

We will first need to write our import statements, so that we have access to the requests module and json module.

import requests
import json

At this point, we look to our documentation to find out what the base of the url will be as well as what parameters are neeed to construct the request. In the Searching section of the documentation, we can see that the url should be in the form of https://itunes.apple.com/search?parameterkeyvalue so we know the base url should be https://itunes.apple.com/search. To determine what parameters are necessary, we can look at the table in the documentation to learn what parameter keys and values will be understood by the iTuens API server.

term is a required parameter with no default value, so we’ll have to provide that.

Look at the iTunes API documentation. If we’re looking for podcasts originating in Ann Arbor, what value should be associated with the key “term”?
```
import requests
import json

params = {"term":        }
```
"Ann Arbor"

We also want to make sure that we’re searching for podcasts.

Look at the iTunes API documentation. What is the key we need to use to only search for podcasts?
```
import requests
import json

params = {      : "podcast"}
```
"entity" or "media"
(media = broader search)

Note that both entity and media are parameters we can use for this task. Entity can be more specific though, so you may need to use that in rather than media!

Now, our code can now make a request to the iTunes API. We’re using the request_with_caching module and providing a cached response to the query in the activecodes. You can try running different queries, but if the itunes webserver is inaccessible to you for one reason or another, it may not work.
```
import requests_with_caching
import json

parameters = {"term": "Ann Arbor", "entity": "podcast"}
iTunes_response = requests_with_caching.get("https://itunes.apple.com/search", params = parameters,permanent_cache_file="itunes_cache.txt")

py_data = json.loads(iTunes_response.text)
```

With that result in hand, you will have to go through the process previously described as Understand. Extract. Repeat. . For example, to print out the names of all the podcasts returned, one could run the following code.
```
import requests_with_caching
import json

parameters = {"term": "Ann Arbor", "entity": "podcast"}
iTunes_response = requests_with_caching.get("https://itunes.apple.com/search", params = parameters, permanent_cache_file="itunes_cache.txt")

py_data = json.loads(iTunes_response.text)
for r in py_data['results']:
    print(r['trackName'])
```    
