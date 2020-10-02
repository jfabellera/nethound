class AlphabeticShift:
    def __init__(self):
        self.__input_controller = None
        self.__unsorted_lines = []
        self.__sorted_lines = []

    def get_shifts(self, input_controller=None):
        if input_controller is not None:
            self.__input_controller = input_controller
        self.__get_data()

    def __get_data(self):
        self.__unsorted_lines = self.__input_controller.lines()
        self.__sort()

    def __sort(self):
        lines = self.__unsorted_lines
        for i in range(1, len(lines)):
            key = lines[i]
            j = i - 1
            while j >= 0 and key < lines[j]:
                lines[j + 1] = lines[j]
                j -= 1
            lines[j + 1] = key
        self.__store_lines(lines)

    # kinda useless but it was in the architecture
    def __store_lines(self, lines):
        self.__sorted_lines = lines

    # returns an array of all alphabetically shifted lines
    def lines(self):
        return self.__sorted_lines

    # returns the ith alphabetically shifted line
    def line(self, i):
        return self.__sorted_lines[i]
