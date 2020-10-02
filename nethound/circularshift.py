from nethound.line import Line

class CircularShift:
    def __init__(self):
        self.__input_controller = None
        self.__shifted_lines = []

    # interface to call internal functions
    def get_lines(self, input_controller=None):
        if input_controller is not None:
            self.__input_controller = input_controller
        self.__get_data()

    # get lines from controller, and shift each one
    def __get_data(self):
        for line in self.__input_controller.lines():
            self.__cs_line(line)

    # produce all shifts of given line, and store them
    def __cs_line(self, line):
        for i in range(len(line)):
            shifted_str = ' '.join(line.words()[i::] + line.words()[:i:]) # some black magic stuff
            shifted_line = Line(shifted_str)
            self.__store_line(shifted_line)

    # store line into __shifted_lines
    def __store_line(self, line):
        self.__shifted_lines.append(line)

    # return an array of all shifted lines
    def lines(self):
        return self.__shifted_lines

    # return the ith shifted line
    def line(self, i):
        return self.__shifted_lines[i]
