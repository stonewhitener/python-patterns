# Template Method Pattern: 処理の枠組みを決め，具体的な内容はサブクラスに任せる


class BaseDisplay:
    def open(self):
        pass

    def print(self):
        pass

    def close(self):
        pass

    def display(self):
        self.open()
        for i in range(5):
            self.print()
        self.close()


class CharDisplay(BaseDisplay):
    def __init__(self, c):
        self.__c = c

    def open(self):
        print('<<', end='')

    def print(self):
        print(self.__c, end='')

    def close(self):
        print('>>')


class StringDisplay(BaseDisplay):
    def __init__(self, s):
        self.__s = s

    def open(self):
        self.__print_line()

    def print(self):
        print('|' + self.__s + '|')

    close = open

    def __print_line(self):
        print('+', end='')
        for i in range(len(self.__s)):
            print('-', end='')
        print('+')


def main():
    d1 = CharDisplay('H')
    d2 = StringDisplay('Hello, world.')
    d3 = StringDisplay('Hello, Python.')

    d1.display()
    d2.display()
    d3.display()


if __name__ == '__main__':
    main()
