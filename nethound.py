from nethound.input import Input
from nethound.output import Output
from nethound.linestorage import LineStorage
from nethound.line import Line
from nethound.circularshift import CircularShift
from nethound.alphabeticshift import AlphabeticShift


def main():
    input_controller = Input()
    line_storage = LineStorage()
    output_controller = Output()
    circular_shifter = CircularShift()
    alphabetic_shifter = AlphabeticShift()

    input_controller.get_input(line_storage)
    print("Input Lines")
    output_controller.display(line_storage)

    print("Circularly Shifted Lines")
    circular_shifter.get_lines(line_storage)
    output_controller.display(circular_shifter)


if __name__ == '__main__':
    main()
