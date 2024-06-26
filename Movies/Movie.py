class Movie():
    def __init__(self, year, title):
        self.__title = title
        self.__year = year

    def set_title(self, title):
        if len(title) > 0:
            self.__title = title
        else:
            raise ValueError("The title must exist")

    def set_year(self, year):
        if year < 1:
            raise ValueError("The year must be positive")
        else:
            self.__year = year

    def get_tile(self):
        return self.__title

    def get_year(self):
        return self.__year

    def __str__(self):
        return self.__title + "The title is", str(self.__year) + "The year is"
