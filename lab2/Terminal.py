import re

from Ontology import Ontology
from VideoGame import VideoGame
from exceptions.IncorrectValueException import IncorrectValueException


class Terminal:

    def __init__(self):
        self.__videoGame = None
        self.__ontology = Ontology()

    def work(self):
        try:
            print('Добрый день! Данная программа поможет найти подходящую игру')
            self.enterArguments()
            self.getPreferGame()
        except IncorrectValueException as ex:
            print(ex.message)
            return

    def enterArguments(self):
        input_str = input("Формат строки: Мне 13 лет, нравятся жанры: Sandbox, Open_world; механики: Crafting, Social_Deduction; тип: Single_player, Multiplayer \nВведите параметры: ")
        age, genres, mechanics, types = self.__parse_input(input_str)

        self.__videoGame = VideoGame(
            genres=genres,
            mechanics=mechanics,
            types=types,
            ageLimit=age
        )

    def __parse_input(self, input_str):
        # Извлекаем возраст
        age_match = re.search(r'Мне (\d+)', input_str)
        if age_match:
            age_values = re.findall(r'\d+', input_str)
            if len(age_values) == 1:
                age = int(age_values[0])
                if age <= 0:
                    raise IncorrectValueException("Возраст не может быть нулевым или отрицательным.")
            else:
                raise IncorrectValueException("Указано неверное значение для возраста. ")
        else:
            age = None
        # Извлекаем жанры
        genres_match = re.search(r'нравятся жанры: ([^;]*)', input_str)
        genres = [genre.strip() for genre in genres_match.group(1).split(',') if
                  genre.strip()] if genres_match else None

        # Извлекаем механики
        mechanics_match = re.search(r'механики: ([^;]*)', input_str)
        mechanics = [mechanic.strip() for mechanic in mechanics_match.group(1).split(',') if
                     mechanic.strip()] if mechanics_match and mechanics_match.group(1).strip() != '...' else None

        # Извлекаем тип
        types_match = re.search(r'тип: ([^;]*)', input_str)
        types = [type_.strip() for type_ in types_match.group(1).split(',') if
                 type_.strip()] if types_match and types_match.group(1).strip() != '...' else None

        return age, genres, mechanics, types

    def getPreferGame(self):
        print(f'Итак, подобранные специально для Вас игры...')
        self.__ontology.choosePreferenceGames(self.__videoGame)
