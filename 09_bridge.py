# Bridge Pattern
# 機能の階層と実装の階層を分ける


class Display:
    def __init__(self, impl):
        self.__impl = impl

    def open(self):
        self.__impl.raw_open()

    def print(self):
        self.__impl.raw_print()

    def close(self):
        self.__impl.raw_close()

    def display(self):
        self.open()
        self.print()
        self.close()


class CountDisplay(Display):
    def __init__(self, impl):
        super().__init__(impl)

    def multi_display(self, times):
        self.open()
        for i in range(times):
            self.print()
        self.close()


class DisplayImpl:
    def raw_open(self):
        pass

    def raw_print(self):
        pass

    def raw_close(self):
        pass


class TextDisplay(DisplayImpl):
    def __init__(self, text):
        self.__text = text

    def raw_open(self):
        self.__print_line()

    def raw_print(self):
        print('|' + self.__text + '|')

    raw_close = raw_open

    def __print_line(self):
        print('+', end='')
        for i in range(len(self.__text)):
            print('-', end='')
        print('+')


def main():
    d1 = Display(TextDisplay('Hello, Japan.'))
    d2 = CountDisplay(TextDisplay('Hello, World.'))
    d3 = CountDisplay(TextDisplay('Hello, Universe.'))

    d1.display()
    d2.display()
    d3.display()
    d3.multi_display(5)


if __name__ == '__main__':
    main()
