class Line:
    def __init__(self, lines=None, delimiter=' '):
        if lines is None:
            self.__words = []
        else:
            self.__words = lines.split(delimiter)

    def set_char(self):
        pass

    def char(self):
        pass

    def word(self):
        pass
