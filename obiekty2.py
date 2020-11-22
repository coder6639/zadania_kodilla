import datetime
import random
from csv import reader


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


class DataBase:

    def __init__(self, file_name="movies.csv"):
        self.film_list = []
        self.file_name = file_name
        self.load_movies(file_name)
        print("Pomyślnie załadowano filmy z pliku")

    def append(self, item):
        self.film_list.append(item)

    def load_movies(self, file):
        with open(file, "r") as movies:
            csv_reader = reader(movies)
            list_of_movies = list(csv_reader)
            for item in list_of_movies:
                if len(item) == 5:
                    item = Series(title=item[0], year=item[1], genre=item[2], season_number=item[3],
                                  episode_number=item[4])
                    self.append(item)

                elif len(item) == 3:
                    item = Film(title=item[0], year=item[1], genre=item[2])
                    self.append(item)

    def get_movies(self):
        movies_list = []
        for item in self.film_list:
            if not isinstance(item, Series):
                movies_list.append(str(item))
        return sorted(movies_list)

    def get_series(self):
        series = []
        for item in self.film_list:
            if isinstance(item, Series):
                series.append(str(item))
        return sorted(series)

    def search(self, expression):
        search_results = []
        for item in self.film_list:
            if expression.casefold() in item.title.casefold():
                search_results.append(item)

        print(f"Wyniki wyszukiwania '{expression}': ")
        for result in search_results:
            print(result)

    def generate_views(self):
        lucky_number = random.randint(0, len(self.film_list) - 1)
        lucky_item = self.film_list[lucky_number]
        lucky_item.views_number += random.randint(0, 100)

    def generate_times_10(self):
        for j in range(10):
            self.generate_views()

    def top_titles(self, content_type, number=3):
        relevant_list = []
        if content_type == Series:
            for item in self.film_list:
                if isinstance(item, Series):
                    relevant_list.append(item)
        elif content_type == Film:
            for item in self.film_list:
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
            print(str(by_views[-(i + 1)]) + " - wyświetleń: " + str(by_views[-(i + 1)].views_number))

    def add_series(self, title: str, year: int, genre: str, season_number: int, episodes: int):
        for i in range(episodes):
            item = Series(title=title, year=year, genre=genre, season_number=season_number, episode_number=i + 1)
            self.append(item)

    def episode_count(self, title):
        episode_counter = 0
        for item in self.film_list:
            if item.title == title and isinstance(item, Series):
                episode_counter += 1
        print(f"Liczba odcinków serialu {title} to {episode_counter}")


print("Biblioteka filmów")
print()
library = DataBase()
for a in range(10):
    library.generate_times_10()
library.top_titles(Series)
library.top_titles(Film)
