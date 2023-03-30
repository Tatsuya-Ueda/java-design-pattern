"""
Strategyパターン

・よもやまだが，Javaでは，int型のインスタンス変数は，0で初期化される．
"""

from enum import Enum
from abc import ABC, abstractmethod
import random


class Hand(Enum):
    # じゃんけんの手を表す3つのenum定数
    ROCK = 0
    SCISSOR = 1
    PAPER = 2


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

    # @override
    def to_string(self):
        return "[{}:{}games, {}win, {}lose]".format(
            self.__name, self.__gamecount, self.__wincount, self.__losecount
        )


class Strategy(ABC):
    @abstractmethod
    def next_hand(self):
        pass

    def study(self, win: bool):
        pass


class ProbStrategy(Strategy):
    def __init__(self) -> None:
        self.__prev_hand: Hand = Hand(0)
        self.__current_hand: Hand = Hand(0)
        # fmt:off
        self.__history = [[1, 1, 1, ], [1, 1, 1, ], [1, 1, 1, ], ]
        # fmt:on

    def next_hand(self):
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
        return self.__current_hand

    # @override
    def study(self, win: bool):
        pre = self.__prev_hand.value
        cur = self.__current_hand.value
        if win:
            self.__history[pre][cur] += 1
        else:
            self.__history[pre][(cur + 1) % 3] += 1
            self.__history[pre][(cur + 1) % 3] += 1


# public class ProbStrategy implements Strategy {
#     private Random random;
#     private int prevHandValue = 0;
#     private int currentHandValue = 0;
#     private int[][] history = {
#         { 1, 1, 1, },
#         { 1, 1, 1, },
#         { 1, 1, 1, },
#     };

#     public ProbStrategy(int seed) {
#         random = new Random(seed);
#     }

#     @Override
#     public Hand nextHand() {
#         int bet = random.nextInt(getSum(currentHandValue));
#         int handvalue = 0;
#         if (bet < history[currentHandValue][0]) {
#             handvalue = 0;
#         } else if (bet < history[currentHandValue][0] + history[currentHandValue][1]) {
#             handvalue = 1;
#         } else {
#             handvalue = 2;
#         }
#         prevHandValue = currentHandValue;
#         currentHandValue = handvalue;
#         return Hand.getHand(handvalue);
#     }

#     private int getSum(int handvalue) {
#         int sum = 0;
#         for (int i = 0; i < 3; i++) {
#             sum += history[handvalue][i];
#         }
#         return sum;
#     }

#     @Override
#     public void study(boolean win) {
#         if (win) {
#             history[prevHandValue][currentHandValue]++;
#         } else {
#             history[prevHandValue][(currentHandValue + 1) % 3]++;
#             history[prevHandValue][(currentHandValue + 2) % 3]++;
#         }
#     }
# }
