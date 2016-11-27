# Adapter Pattern: 一皮かぶせて再利用


class Banner:
    def __init__(self, text):
        self.__text = text

    def show_with_paren(self):
        print('(' + self.__text + ')')

    def show_with_aster(self):
        print('*' + self.__text + '*')


class BasePrint:
    def print_weak(self):
        pass

    def print_strong(self):
        pass


class PrintBanner(BasePrint, Banner):
    def __init__(self, text):
        super().__init__(text)

    def print_weak(self):
        self.show_with_paren()

    def print_strong(self):
        self.show_with_aster()


def main():
    p = PrintBanner('Hello')
    p.print_weak()
    p.print_strong()


if __name__ == '__main__':
    main()
