# Singleton Pattern: インスタンスはひとつ


class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        print('インスタンスを生成しました')


def main():
    print('Start.')

    s1 = Singleton()
    s2 = Singleton()

    if s1 is s2:
        print('s1 と s2 は同じインスタンスです。')
    else:
        print('s1 と s2 は同じインスタンスではありません。')

    print('End.')


if __name__ == '__main__':
    main()
