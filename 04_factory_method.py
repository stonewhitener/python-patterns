# Factory Method Pattern: インスタンスの生成をサブクラスに任せる


class BaseProduct:
    def use(self):
        pass


class BaseFactory:
    def create(self, owner):
        product = self.create_product(owner)
        self.register_product(product)
        return product

    def create_product(self, owner):
        pass

    def register_product(self, product):
        pass


# IDCard, IDCardFactory はそれぞれ BaseProduct, BaseFactory に依存していない

class IDCard(BaseProduct):
    def __init__(self, owner):
        print(owner + 'のカードを作ります。')
        self.__owner = owner

    @property
    def owner(self):
        return self.__owner

    def use(self):
        print(self.__owner + 'のカードを使います。')


class IDCardFactory(BaseFactory):
    __owners = []

    @property
    def owners(self):
        return self.__owners

    def create_product(self, owner):
        return IDCard(owner)

    def register_product(self, product):
        self.__owners.append(product.owner)


def main():
    factory = IDCardFactory()
    card1 = factory.create('結城浩')
    card2 = factory.create('とむら')
    card3 = factory.create('佐藤花子')

    card1.use()
    card2.use()
    card3.use()


if __name__ == '__main__':
    main()
