# Abstract Factory Pattern
#
import sys


class BaseItem:
    def __init__(self, caption):
        self._caption = caption

    def make_html(self):
        pass


class Link(BaseItem):
    def __init__(self, caption, url):
        super().__init__(caption)
        self._url = url


class Tray(BaseItem):
    def __init__(self, caption):
        super().__init__(caption)
        self._tray = []

    def add(self, item):
        self._tray.append(item)


class Page:
    def __init__(self, title, author):
        self._title = title
        self._author = author
        self._contents = []

    def add(self, content):
        self._contents.append(content)

    def output(self):
        try:
            filename = self._title + '.html'
            file = open(filename, 'w')
            file.write(self.make_html())
            file.close()
            print(filename + 'を作成しました。')
        except IOError:
            pass

    def make_html(self):
        pass


class Factory:
    @classmethod
    def get_factory(cls, class_name):
        parts = class_name.split('.')
        module = '.'.join(parts[:-1])
        m = __import__(module)
        for comp in parts[1:]:
            m = getattr(m, comp)
        return m()


class ListFactory(Factory):
    def create_link(self, caption, url):
        return ListLink(caption, url)

    def create_tray(self, caption):
        return ListTray(caption)

    def create_page(self, title, author):
        return ListPage(title, author)


class ListLink(Link):
    def __init__(self, caption, url):
        super().__init__(caption, url)

    def make_html(self):
        return '  <li><a href="' + self._url + '">' + self._caption + '</a></li>\n'


class ListTray(Tray):
    def __init__(self, caption):
        super().__init__(caption)

    def make_html(self):
        buffer = ''
        buffer += '<li>\n'
        buffer += self._caption + '\n'
        buffer += '<ul>\n'
        for t in self._tray:
            buffer += t.make_html()
        buffer += '</ul>\n'
        buffer += '</li>\n'
        return buffer


class ListPage(Page):
    def __init__(self, title, author):
        super().__init__(title, author)

    def make_html(self):
        buffer = ''
        buffer += '<html><head><title>' + self._title + '</title></head>\n'
        buffer += '<body>\n'
        buffer += '<h1>' + self._title + '</h1>'
        buffer += '<ul>\n'
        for content in self._contents:
            buffer += content.make_html()
        buffer += '</ul>'
        buffer += '<hr><address>' + self._author + '</address>'
        buffer += '</body></html>\n'
        return buffer


class TableFactory(Factory):
    def create_link(self, caption, url):
        return TableLink(caption, url)

    def create_tray(self, caption):
        return TableTray(caption)

    def create_page(self, title, author):
        return TablePage(title, author)


class TableLink(Link):
    def __init__(self, caption, url):
        super().__init__(caption, url)

    def make_html(self):
        return '<td><a href="' + self._url + '">' + self._caption + '</a></td>\n'


class TableTray(Tray):
    def __init__(self, caption):
        super().__init__(caption)

    def make_html(self):
        buffer = ''
        buffer += '<td>'
        buffer += '<table width="100" border="1"><tr>'
        buffer += '<td bgcolor="#ccc" align="center" colspan="' + str(len(self._tray)) + '"><b>' + self._caption + '</b></td>'
        buffer += '</tr>\n'
        buffer += '<tr>'
        for t in self._tray:
            buffer += t.make_html()
        buffer += '</tr></table>'
        buffer += '</td>'
        return buffer


class TablePage(Page):
    def __init__(self, title, author):
        super().__init__(title, author)

    def make_html(self):
        buffer = ''
        buffer += '<html><head><title>' + self._title + '</title></head>\n'
        buffer += '<body>\n'
        buffer += '<h1>' + self._title + '</h1>'
        buffer += '<table width="80" border="3">\n'
        for content in self._contents:
            buffer += '<tr>' + content.make_html() + '</tr>'
        buffer += '</table>\n'
        buffer += '<hr><address>' + self._author + '</address>'
        buffer += '</body></html>\n'
        return buffer


def main():
    if len(sys.argv) is not 2:
        print('Usage: python 08_abstract_factory.py <class_name_of_concrete_factory>')
        print('Example 1: python 08_abstract_factory.py 08_abstract_factory.ListFactory')
        print('Example 2: python 08_abstract_factory.py 08_abstract_factory.TableFactory')

    factory = Factory.get_factory(sys.argv[1])

    link_asahi = factory.create_link('朝日新聞', 'http://www.asahi.com/')
    link_yomiuri = factory.create_link('読売新聞', 'http://www.yomiuri.co.jp/')

    link_us_yahoo = factory.create_link('Yahoo!', 'http://www.yahoo.com/')
    link_jp_yahoo = factory.create_link('Yahoo! Japan', 'http://www.yahoo.co.jp/')

    link_excite = factory.create_link('Excite', 'http://www.excite.com/')
    link_google = factory.create_link('Google', 'http://www.google.com/')

    tray_news = factory.create_tray('新聞')
    tray_news.add(link_asahi)
    tray_news.add(link_yomiuri)

    tray_yahoo = factory.create_tray('Yahoo!')
    tray_yahoo.add(link_us_yahoo)
    tray_yahoo.add(link_jp_yahoo)

    tray_search = factory.create_tray('サーチエンジン')
    tray_search.add(tray_yahoo)
    tray_search.add(link_excite)
    tray_search.add(link_google)

    page = factory.create_page('LinkPage', '結城浩')
    page.add(tray_news)
    page.add(tray_search)
    page.output()


if __name__ == '__main__':
    main()
