# Prototype Pattern
# インスタンスの生成するための式を汎用化し，クラス名の束縛をなくしている
import copy


class BaseProduct:
    def use(self, text):
        pass

    def clone(self):
        return copy.deepcopy(self)


class Manager:
    __showcase = {}

    def register(self, name, product):
        self.__showcase[name] = product

    def create(self, name):
        p = self.__showcase[name]
        return p.clone()


class MessageBox(BaseProduct):
    def __init__(self, decochar):
        self.__decochar = decochar

    def use(self, text):
        for i in range(len(text) + 4):
            print(self.__decochar, end='')
        print()
        print(self.__decochar + ' ' + text + ' ' + self.__decochar)
        for i in range(len(text) + 4):
            print(self.__decochar, end='')
        print()


class UnderlinePen(BaseProduct):
    def __init__(self, ulchar):
        self.__ulchar = ulchar

    def use(self, text):
        print('"' + text + '"')
        print(' ', end='')
        for i in range(len(text)):
            print(self.__ulchar, end='')
        print()


def main():
    manager = Manager()
    ulpen = UnderlinePen('~')
    mbox = MessageBox('*')
    sbox = MessageBox('/')
    manager.register('strong message', ulpen)
    manager.register('warning box', mbox)
    manager.register('slash box', sbox)

    p1 = manager.create('strong message')
    p1.use('Hello, world.')
    p2 = manager.create('warning box')
    p2.use('Hello, world.')
    p3 = manager.create('slash box')
    p3.use('Hello, world.')


if __name__ == '__main__':
    main()
