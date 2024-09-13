from owlready2 import *

import VideoGame


class Ontology:

    def __init__(self, path=r"file://ontology/videogames.owl"):
        self.__ontology = get_ontology(path).load()
        owlready2.sync_reasoner_pellet()

    def getOntology(self):
        return self.__ontology

    def getGenres(self):
        return self.__ontology.search(type=self.__ontology.Genre)

    def getTypes(self):
        return self.__ontology.search(type=self.__ontology.Type)

    def getMechanics(self):
        return self.__ontology.search(type=self.__ontology.Mechanic)

    def getVideoGames(self):
        return self.__ontology.search(type=self.__ontology.VideoGame)

    def choosePreferenceGames(self, videoGame):
        allVideoGames = self.getVideoGames()

        # Фильтрация по возрастным ограничениям
        if videoGame.getAgeLimit() is not None:
            age = videoGame.getAgeLimit()
            allVideoGames = [game for game in allVideoGames if game.hasAgeLimit and game.hasAgeLimit <= age]

        # Фильтрация по жанрам
        if videoGame.getGenres() is not None and len(videoGame.getGenres()) != 0:
            genres = videoGame.getGenres()
            allVideoGames = [game for game in allVideoGames if
                             game.hasGenre and any(genre.name in genres for genre in game.hasGenre)]

        # Фильтрация по механикам
        if videoGame.getMechanics() is not None and len(videoGame.getMechanics()) != 0:
            mechanics = videoGame.getMechanics()
            allVideoGames = [game for game in allVideoGames if
                             game.hasMechanic and any(mechanic.name in mechanics for mechanic in game.hasMechanic)]

        # Фильтрация по типам
        if videoGame.getTypes() is not None and len(videoGame.getTypes()) != 0:
            types = videoGame.getTypes()
            allVideoGames = [game for game in allVideoGames if
                             game.hasType and any(type.name in types for type in game.hasType)]

        # Формирование финального списка игр
        filtered_games = [
            VideoGame.VideoGame(
                genres=game.hasGenre if game.hasGenre else None,
                types=game.hasType if game.hasType else None,
                ageLimit=int(game.hasAgeLimit) if game.hasAgeLimit else None,
                mechanics=game.hasMechanic if game.hasMechanic else None,
                name=game.name
            )
            for game in allVideoGames
        ]

        print(*filtered_games)
