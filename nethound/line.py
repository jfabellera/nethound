import re


class Line:
    def __init__(self, lines=None, delimiter=r'\s+'):
        if lines is None:
            self.__words = []
        else:
            self.__words = re.split(delimiter, lines)

    def words(self):
        return self.__words

    def word(self, i):
        return self.__words[i]

    def __len__(self):
        return len(self.__words)

    def __str__(self):
        return ' '.join(self.__words)
