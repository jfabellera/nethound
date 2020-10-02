from nethound.line import Line


class LineStorage:
    def __init__(self):
        self.__lines = []

    # parse input data
    def set_line(self, input_data):
        str_lines = input_data.split('$')
        for elem in str_lines:
            self.__lines.append(Line(elem.strip()))

    # returns an array of all the lines
    def lines(self):
        return self.__lines

    # return's the ith line
    def line(self, i):
        return self.__lines[i]
