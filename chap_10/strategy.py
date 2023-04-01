"""
Strategyパターン

・よもやまだが，Javaでは，int型のインスタンス変数は，0で初期化される．
・三すくみの勝ち負けの計算は，「1ずらして3の余りをとる」がカギ
"""

from enum import Enum
from abc import ABC, abstractmethod
import random


class Hand(Enum):
    # じゃんけんの手を表す3つのenum定数
    ROCK = 0
    SCISSOR = 1
    PAPER = 2

    def is_stronger_than(self, h: "Hand") -> bool:
        return self.__fight(h) == 1

    def is_weaker_than(self, h: "Hand") -> bool:
        return self.__fight(h) == -1

    def __fight(self, h: "Hand") -> int:
        if self.value == h.value:
            return 0
        elif (self.value + 1) % 3 == h.value:
            return 1
        else:
            return -1


class Player:
    def __init__(self, name: str, strategy: "Strategy") -> None:
        self.__name: str = name
        self.__strategy: "Strategy" = strategy

        self.__wincount: int = 0
        self.__losecount: int = 0
        self.__gamecount: int = 0

    def next_hand(self):
        return self.__strategy.next_hand()

    def win(self):
        self.__strategy.study(True)
        self.__wincount += 1
        self.__gamecount += 1

    def lose(self):
        self.__strategy.study(False)
        self.__losecount += 1
        self.__gamecount += 1

    def even(self):
        self.__gamecount += 1

    def to_string(self):
        return "[{}:{}games, {}win, {}lose]".format(
            self.__name, self.__gamecount, self.__wincount, self.__losecount
        )


class Strategy(ABC):
    @abstractmethod
    def next_hand(self) -> Hand:
        pass

    @abstractmethod
    def study(self, win: bool) -> None:
        pass


class ProbStrategy(Strategy):
    def __init__(self) -> None:
        self.__prev_hand: Hand = Hand(0)
        self.__current_hand: Hand = Hand(0)
        # fmt:off
        self.__history = [[1, 1, 1, ], [1, 1, 1, ], [1, 1, 1, ], ]
        # fmt:on

    # @override
    def next_hand(self) -> Hand:
        second_table = self.__history[self.__current_hand.value]
        bet = random.randint(0, sum(second_table))
        if bet < second_table[0]:
            hand_value = 0
        elif bet < second_table[0] + second_table[1]:
            hand_value = 1
        else:
            hand_value = 2
        self.__prev_hand = self.__current_hand
        self.__current_hand = Hand(hand_value)
        return Hand(hand_value)

    # @override
    def study(self, win: bool) -> None:
        pval = self.__prev_hand.value
        cval = self.__current_hand.value
        if win:
            self.__history[pval][cval] += 1
        else:
            self.__history[pval][(cval + 1) % 3] += 1
            self.__history[pval][(cval + 1) % 3] += 1


class WinningStrategy(Strategy):
    def __init__(self) -> None:
        self.won: bool = False
        self.prev_hand: Hand = None

    # @override
    # 今のロジックなら，self.won = Falseで初期化されていれば，Noneが返されることはない. 一応assertする
    def next_hand(self) -> Hand:
        if not self.won:
            self.prev_hand = Hand(random.randrange(3))
        assert isinstance(self.prev_hand, Hand)
        return self.prev_hand

    # @override

    def study(self, win: bool) -> None:
        self.won = win


class Main:
    def __init__(self) -> None:  # Javaのmain関数を模して，これをmainとする
        player1: Player = Player("Taro", WinningStrategy())
        player2: Player = Player("Hana", ProbStrategy())
        for _ in range(10000):
            next_hand1 = player1.next_hand()
            next_hand2 = player2.next_hand()
            if next_hand1.is_stronger_than(next_hand2):
                print("Winner:{}".format(player1.to_string()))
                player1.win()
                player2.lose()
            elif next_hand2.is_stronger_than(next_hand1):
                print("Winner:{}".format(player2.to_string()))
                player1.lose()
                player2.win()
            else:
                print("Even...")
                player1.even()
                player2.even()
        print("Total result:")
        print(player1.to_string())
        print(player2.to_string())


Main()
