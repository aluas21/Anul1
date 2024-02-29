class Duplicate_Error(Exception):
    def __init__(self, mesaj):
        self.__mesaj = mesaj

    def __str__(self):
        return f'Duplicate: {self.__mesaj}'


