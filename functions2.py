#ex1
def good(movie):
    return movie["imdb"] > 5.5

#ex2
def filter_good_movies(movies):
    good_movies = [movie for movie in movies if movie["imdb"] > 5.5]
    return good_movies

#ex3
def movies_by_category(movies, category_name):
    movies_in_category = [movie for movie in movies if movie["category"] == category_name]
    return movies_in_category

#ex4
def avg_score(movies):
    return sum([movie["imdb"] for movie in movies]) / len(movies)
print(avg_score(movies))

#ex5
def avg_imdb_categoties(movie, category_name):
    moviess=movies_by_category(movie, category_name)
    return avg_score(moviess)