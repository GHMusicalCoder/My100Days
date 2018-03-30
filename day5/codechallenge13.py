from operator import attrgetter
from day5 import get_movies_by_director


def rate_directors(directors):
    by_rating = []
    for director, movies in directors.items():
        movie_count = 0
        total_rating = 0
        for movie in movies:
            if movie.year >= 1960:
                movie_count += 1
                total_rating += movie.score

        if movie_count >= 4:
            by_rating.append((director, total_rating / movie_count))

    return sorted(by_rating, key=lambda x: x[1], reverse=True)


def print_top_20_list(the_list):
    seperator = '-'
    count = 1
    for entry in the_list:
        print('{0:02d}. {1:52} {2:0.1f}'.format(count, entry[0], entry[1]))
        print(seperator*60)
        movies = directors.get(entry[0])
        for movie in sorted(movies, key=attrgetter('score'), reverse=True):
            print('{0}] {1:50} {2:0.1f}'.format(movie.year, movie.title, movie.score))
        print('')
        count += 1


if __name__ == '__main__':
    # our movie file is already local from day 5 exercise - so i'm just going to use that
    movie_file = 'movies.csv'
    directors = get_movies_by_director(movie_file)
    rated_list = rate_directors(directors)
    print_top_20_list(rated_list[:20])