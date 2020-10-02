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

    def __lt__(self, other):
        return self.__str__() < str(other)

    def __gt__(self, other):
        return self.__str__() > str(other)

    def __le__(self, other):
        return self.__str__() <= str(other)

    def __ge__(self, other):
        return self.__str__() >= str(other)

    def __eq__(self, other):
        return self.__str__() == str(other)

    def __ne__(self, other):
        return self.__str__() != str(other)

    def __len__(self):
        return len(self.__words)

    def __str__(self):
        return ' '.join(self.__words)
