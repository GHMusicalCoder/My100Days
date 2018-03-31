from collections import defaultdict, namedtuple, Counter, deque
import csv
from urllib.request import urlretrieve

# tuple reference
Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director(data):
    """
    Extracts all movies from the supplied csv file and stores them in a dictionary
    where keys are the directors, and values is a list of movies (using the Movie namedtuple
    :param data: the name of the csv file we'll be traipsing through
    :return: the default dict list of directors
    """
    directors = defaultdict(list)
    with open(data) as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors


if __name__ == '__main__':
    # get the movie information local
    movie_location = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
    movie_file = '../extra_files/movies.csv'
    urlretrieve(movie_location, movie_file)

    directors = get_movies_by_director(movie_file)
    print(*directors['Christopher Nolan'], sep='\n')

    cnt = Counter()
    for director, movies in directors.items():
        cnt[director] += len(movies)

    print(*cnt.most_common(5), sep='\n')