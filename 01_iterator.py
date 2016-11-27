# Iterator Pattern: 数え上げの動作を一般化


class Book:
    def __init__(self, title):
        self.__title = title

    @property
    def title(self):
        return self.__title


class BookShelf:
    def __init__(self, n):
        self.__books = [None] * n
        self.__last = 0

    def append(self, book):
        self.__books[self.__last] = book
        self.__last += 1

    def __getitem__(self, index):
        return self.__books[index]

    def __len__(self):
        return self.__last

    def __iter__(self):
        return BookShelfIterator(self)


class BookShelfIterator:
    def __init__(self, book_shelf):
        self.__book_shelf = book_shelf
        self.__index = 0

    def __next__(self):
        if self.__index < len(self.__book_shelf):
            book = self.__book_shelf[self.__index]
            self.__index += 1
            return book
        else:
            raise StopIteration()

    def __iter__(self):
        return self


def main():
    book_shelf = BookShelf(4)

    book_shelf.append(Book('Around the World in 80 Days'))
    book_shelf.append(Book('Bible'))
    book_shelf.append(Book('Cinderella'))
    book_shelf.append(Book('Daddy-Long-Legs'))

    for b in book_shelf:
        print(b.title)


if __name__ == '__main__':
    main()
