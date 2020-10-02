class Output:
    def __init__(self):
        self.__controller = None

    def display(self, controller=None):
        if controller is not None:
            self.__controller = controller
            self.__get_data()

    def __get_data(self):
        string = ''
        for line in self.__controller.lines():
            string += str(line) + '\n'
        print(string)
