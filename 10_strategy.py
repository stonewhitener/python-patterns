# Strategy Pattern
# 戦略を切り替え可能にする
import random
from enum import Enum

import sys


class Hand(Enum):
    rock = 1
    paper = 2
    scissors = 3

    def __fight(self, other):
        if self.value == other.value:
            return 0
        elif self.value % 3 == other.value - 1:
            return -1
        else:
            return 1

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.__fight(other) is -1
        raise NotImplementedError

    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.__fight(other) is 1
        raise NotImplementedError

    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.__fight(other) is 0
        raise NotImplementedError


class BaseStrategy:
    def next_hand(self):
        pass

    def study(self, win):
        pass


class WinningStrategy(BaseStrategy):
    def __init__(self):
        self.__won = False
        self.__prev = None

    def next_hand(self):
        if not self.__won:
            self.__prev = random.choice(list(Hand))
        return self.__prev

    def study(self, win):
        self.__won = win


class ProbStrategy(BaseStrategy):
    def __init__(self):
        self.__prev = Hand.rock
        self.__current = Hand.rock
        self.__history = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]

    def next_hand(self):
        bet = random.randrange(self.__get_sum(self.__current.value))
        hand = None
        if bet < self.__history[self.__current.value - 1][0]:
            hand = Hand.rock
        elif bet < self.__history[self.__current.value - 1][0] + self.__history[self.__current.value - 1][1]:
            hand = Hand.paper
        else:
            hand = Hand.scissors

        self.__prev = self.__current
        self.__current = hand
        return hand

    def study(self, win):
        if win:
            self.__history[self.__prev.value - 1][self.__current.value - 1] += 1
        else:
            self.__history[self.__prev.value - 1][self.__current.value % 3] += 1
            self.__history[self.__prev.value - 1][(self.__current.value + 1) % 3] += 1

    def __get_sum(self, hv):
        sum = 0
        for h in range(3):
            sum += h
        return sum


class Player:
    def __init__(self, name, strategy):
        self.__name = name
        self.__strategy = strategy

        self.__win_count = 0
        self.__lose_count = 0
        self.__game_count = 0

    def next_hand(self):
        return self.__strategy.next_hand()

    def win(self):
        self.__strategy.study(True)
        self.__win_count += 1
        self.__game_count += 1

    def lose(self):
        self.__strategy.study(False)
        self.__lose_count += 1
        self.__game_count += 1

    def even(self):
        self.__game_count += 1

    def __str__(self):
        return '[' + self.__name + ': ' + str(self.__game_count) + ' games, ' + str(self.__win_count) + ' win, ' + str(self.__lose_count) + ' lose]'


def main():
    if len(sys.argv) != 2:
        pass

    p1 = Player('Taro', WinningStrategy())
    p2 = Player('Hana', ProbStrategy())

    for i in range(10000):
        h1 = p1.next_hand()
        h2 = p2.next_hand()
        if h1 > h2:
            print('Winner: ' + str(p1))
            p1.win()
            p2.lose()
        elif h1 < h2:
            print('Winner: ' + str(p2))
            p1.lose()
            p2.win()
        else:
            print('Even...')
            p1.even()
            p2.even()
    print('Total result: ')
    print(str(p1))
    print(str(p2))


if __name__ == '__main__':
    main()
