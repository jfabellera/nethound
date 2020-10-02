class Input:
    def __init__(self):
        self.__input_data = ''
        self.__line_storage = None

    def get_input(self, line_storage):
        self.__line_storage = line_storage
        self.__get_data()

    def __get_data(self):
        self.__input_data = input()
        self.__line_storage.set_line(self.__input_data)
