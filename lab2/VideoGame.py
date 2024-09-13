class VideoGame:

    def __init__(self, genres=None, mechanics=None, types=None, ageLimit=None, name=None):
        self.__genres: list[str] = genres
        self.__mechanics: list[str] = mechanics
        self.__types: list[str] = types
        self.__ageLimit: int = ageLimit
        self.__name: str = name

    def getGenres(self):
        return self.__genres

    def setGenres(self, genres):
        self.__genres = genres

    def getMechanics(self):
        return self.__mechanics

    def setMechanics(self, mechanics):
        self.__mechanics = mechanics

    def getTypes(self):
        return self.__types

    def setTypes(self, types):
        self.__types = types

    def getAgeLimit(self):
        return self.__ageLimit

    def setAgeLimit(self, ageLimit):
        self.__ageLimit = ageLimit

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def __str__(self):
        return (
            f"Название: {self.__name} | Возрастные ограничения: {str(self.__ageLimit) + '+' if self.__ageLimit is not None else '-'}\n"
            f"\tМеханики: {[el.name for el in self.__mechanics] if self.__mechanics is not None else '-'}\n"
            f"\tЖанры: {[el.name for el in self.__genres] if self.__genres is not None else '-'}\n"
            f"\tТипы: {[el.name for el in self.__types] if self.__types is not None else '-'}\n")
