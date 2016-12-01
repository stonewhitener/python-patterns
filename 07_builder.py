# Builder Pattern
# 複雑なインスタンスを組み立てる
import sys


class Builder:
    def make_title(self, title):
        pass

    def make_text(self, text):
        pass

    def make_items(self, items):
        pass

    def close(self):
        pass


class Director:
    def __init__(self, builder):
        self.__builder = builder

    def construct(self):
        self.__builder.make_title('Greeting')
        self.__builder.make_text('朝から昼にかけて')
        self.__builder.make_items(['おはようございます。', 'こんにちは。'])
        self.__builder.make_text('夜に')
        self.__builder.make_items(['こんばんは。', 'おやすみなさい。', 'さようなら。'])
        self.__builder.close()


class TextBuilder(Builder):
    def make_title(self, title):
        self.__buffer = '==============================\n'
        self.__buffer += '『' + title + '』\n'
        self.__buffer += '\n'

    def make_text(self, text):
        self.__buffer += '■' + text + '\n'
        self.__buffer += '\n'

    def make_items(self, items):
        for item in items:
            self.__buffer += '　・' + item + '\n'
        self.__buffer += "\n"

    def close(self):
        self.__buffer += '==============================\n'

    def get_result(self):
        return self.__buffer


class HTMLBuilder(Builder):
    def make_title(self, title):
        self.__filename = title + '.html'
        self.__file = open(self.__filename, 'w')
        self.__file.write('<html><head><title>' + title + '</title></head><body>')
        self.__file.write('<h1>' + title + '</h1>')

    def make_text(self, text):
        self.__file.write('<p>' + text + '</p>')

    def make_items(self, items):
        self.__file.write('<ul>')
        for item in items:
            self.__file.write('<li>' + item + '</li>')
        self.__file.write('</ul>')

    def close(self):
        self.__file.write('</body></html>')
        self.__file.close()

    def get_result(self):
        return self.__filename


def main():
    if len(sys.argv) is not 2:
        usage()
        sys.exit(0)

    if sys.argv[1] == 'plain':
        text_builder = TextBuilder()
        director = Director(text_builder)
        director.construct()
        result = text_builder.get_result()
        print(result)
    elif sys.argv[1] == 'html':
        html_builder = HTMLBuilder()
        director = Director(html_builder)
        director.construct()
        result = html_builder.get_result()
        print(result)
    else:
        usage()
        sys.exit(0)


def usage():
    print('Usage: python 07_builder.py plain    プレーンテキストで文書作成')
    print('Usage: python 07_builder.py html     HTML ファイルで文書作成')


if __name__ == '__main__':
    main()
