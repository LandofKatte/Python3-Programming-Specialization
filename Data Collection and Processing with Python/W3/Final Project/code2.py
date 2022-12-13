import json
import requests_with_caching

def get_movies_from_tastedive(param):
    request = {"q":param,"type": "movies","limit": 5}
    response = requests_with_caching.get("https://tastedive.com/api/similar",params=request)
    data = json.loads(response.text)
    return data

def extract_movie_titles(movie_dict):
    titles_list = list()
    titles = movie_dict["Similar"]["Results"]
    for title in titles:
        titles_list.append(title["Name"])
    return titles_list

def get_related_titles(titles_list):
    if titles_list != []:
        related_list=[]
        extracted_related_list = []
        for movieName in titles_list:
            related_list = extract_movie_titles(get_movies_from_tastedive(movieName))
            for movieNameAux in related_list:
                if movieNameAux not in extracted_related_list:
                    extracted_related_list.append(movieNameAux)
        
        return extracted_related_list
    return titles_list

def get_movie_data(title):
    query_dict = {'t': title, 'r': 'json'}
    request = requests_with_caching.get('http://www.omdbapi.com/', params=query_dict)
    response = json.loads(request.text)
    return response

def get_movie_rating(title_dict):
    rating = ""
    for rating_list in title_dict["Ratings"]:
        if rating_list["Source"]== "Rotten Tomatoes":
            rating = rating_list["Value"]
    if rating != "":
        int_rating = int(rating[:2])
    else: int_rating = 0
    return int_rating

def get_sorted_recommendations(titles):
    title_list = get_related_titles(titles)
    title_list = sorted(title_list, key = lambda title: (get_movie_rating(get_movie_data(title)), title), reverse=True)
    
    return title_list


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
get_movies_from_tastedive("Bridesmaids")
get_movies_from_tastedive("Black Panther")
extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
extract_movie_titles(get_movies_from_tastedive("Black Panther"))
get_related_titles(["Black Panther", "Captain Marvel"])
get_movie_rating(get_movie_data("Deadpool 2"))
get_movie_data("Venom")
get_movie_data("Baby Mama")
@LandofKatte
