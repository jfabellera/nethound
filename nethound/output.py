class Output:
    def __init__(self):
        self.__input_controller = None

    def display(self, controller=None):
        if controller is not None:
            self.__input_controller = controller
            self.__get_data()

    def __get_data(self):
        string = ''
        for line in self.__input_controller.lines():
            string += str(line) + '\n'
        print(string)
