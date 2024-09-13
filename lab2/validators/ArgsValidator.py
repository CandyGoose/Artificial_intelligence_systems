from datetime import datetime

from exceptions.IncorrectValueException import IncorrectValueException


class ArgsValidator:
    SEPARATOR = ', '
    NONE_INPUT = '-'
    ONE_STR = 1

    @staticmethod
    def validateLists(inputStr, templateList):
        inputs: list[str] = []
        if not inputStr:
            raise IncorrectValueException('Некорректно введены данные. Попробуйте еще раз.')
        if inputStr is not ArgsValidator.NONE_INPUT:
            for inp in inputStr.split(ArgsValidator.SEPARATOR):
                if inp.strip() not in templateList:
                    raise IncorrectValueException('Упс! Такого варианта нет:(')
                inputs.append(inp)
        return inputs

    @staticmethod
    def validateYear(inputStr):
        currentYear = datetime.now().year
        validatedInput = ArgsValidator.validateOneString(inputStr)
        if validatedInput is not None:
            try:
                validatedInput = int(inputStr)
                if validatedInput <= 0 or validatedInput > currentYear:
                    raise IncorrectValueException('Год выпуска должен быть положительным числом.')
            except:
                raise IncorrectValueException('Год выпуска введён некорректно. Необходимо ввести целое число.')
        return validatedInput

    @staticmethod
    def validateRating(inputStr):
        validatedInput = ArgsValidator.validateOneString(inputStr)
        if validatedInput is not None:
            try:
                validatedInput = float(inputStr)
                if validatedInput <= 0 or validatedInput > 10.0:
                    raise IncorrectValueException('Рейтинг должен быть положительным вещественным числом.')
            except:
                raise IncorrectValueException('Рейтинг введён некорректно. Необходимо ввести вещественное число.')
        return validatedInput

    @staticmethod
    def validateAge(inputStr):
        validatedInput = ArgsValidator.validateOneString(inputStr)
        if validatedInput is not None:
            try:
                validatedInput = int(inputStr)
                if validatedInput <= 0:
                    raise IncorrectValueException('Возраст должен быть положительным числом.')
            except:
                raise IncorrectValueException('Возраст введён некорректно. Необходимо ввести целое число.')
        return validatedInput

    @staticmethod
    def validateOneString(inputStr, templateList=None):
        validatedInput = None
        if not inputStr:
            raise IncorrectValueException('Некорректно введены данные. Попробуйте еще раз.')
        if inputStr is not ArgsValidator.NONE_INPUT:
            inputLength = len(inputStr.split(ArgsValidator.SEPARATOR))
            if inputLength == ArgsValidator.ONE_STR:
                if templateList is not None:
                    if inputStr in templateList:
                        validatedInput = inputStr
                else:
                    validatedInput = inputStr
            else:
                raise IncorrectValueException('Необходимо ввести одно значение.')
        return validatedInput
