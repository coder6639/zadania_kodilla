import datetime
import random
from csv import reader

from faker import Faker

fake = Faker()


class Film:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self._views = 0

    def __str__(self):
        return f"{self.title} ({self.year})"

    def __gt__(self, other):
        return self.views_number > other.views_number

    def __lt__(self, other):
        return self.views_number < other.views_number

    @property
    def views_number(self):
        return self._views

    @views_number.setter
    def views_number(self, value: int):
        self._views = value

    def play(self):
        self._views += 1


class Series(Film):
    def __init__(self, season_number, episode_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season_number = season_number
        self.episode_number = episode_number

    def __str__(self):
        return f"{self.title} S{str(self.season_number).zfill(2)}E{str(self.episode_number).zfill(2)}"

    @property
    def episode_count(self):
        episode_counter = 0
        title = self.title
        for item in film_list:
            if isinstance(item, Series) and item.title == title:
                episode_counter += 1
        return episode_counter


def get_movies():
    movies_list = []
    for item in film_list:
        if not isinstance(item, Series):
            movies_list.append(str(item))
    return sorted(movies_list)


def get_series():
    series = []
    for item in film_list:
        if isinstance(item, Series):
            series.append(str(item))
    return sorted(series)


def search(expression):
    search_results = []
    for item in film_list:
        if expression.casefold() in item.title.casefold():
            search_results.append(item)

    print(f"Wyniki wyszukiwania '{expression}': ")
    for result in search_results:
        print(result)


def generate_views():
    lucky_number = random.randint(0, len(film_list) - 1)
    lucky_item = film_list[lucky_number]
    lucky_item.views_number += random.randint(0, 100)


def generate_times_10():
    for i in range(10):
        generate_views()


def top_titles(content_type, number=3):
    relevant_list = []
    if content_type == Series:
        for item in film_list:
            if isinstance(item, Series):
                relevant_list.append(item)
    elif content_type == Film:
        for item in film_list:
            if not isinstance(item, Series):
                relevant_list.append(item)
    else:
        print("Choose 'Film' or 'Series' as content type")
    by_views = sorted(relevant_list, key=lambda film: film.views_number)
    if content_type == Series:
        print(f"Najpopularniejsze seriale dnia {datetime.date.today()}:")
    elif content_type == Film:
        print(f"Najpopularniejsze filmy dnia {datetime.date.today()}: ")

    for i in range(number):
        print(str(by_views[-(i+1)]) + " - wyświetleń: " + str(by_views[-(i+1)].views_number))


def load_movies():
    with open("movies.csv", "r") as movies:
        csv_reader = reader(movies)
        list_of_movies = list(csv_reader)
        for item in list_of_movies:
            item = Film(title=item[0], year=item[1], genre=item[2])
            film_list.append(item)


def load_series():
    with open("series.csv", "r") as series:
        csv_reader = reader(series)
        list_of_series = list(csv_reader)
        for item in list_of_series:
            item = Series(title=item[0], year=item[1], genre=item[2], season_number=item[3], episode_number=item[4])
            film_list.append(item)


def load_data():
    load_movies()
    load_series()


def add_series(title: str, year: int, genre: str, season_number: int, episodes: int):
    for i in range(episodes):
        item = Series(title=title, year=year, genre=genre, season_number=season_number, episode_number=i+1)
        film_list.append(item)


film_list = []

print("Biblioteka filmów")

load_data()

for i in range(10):
    generate_times_10()

top_titles(Series)
top_titles(Film)



