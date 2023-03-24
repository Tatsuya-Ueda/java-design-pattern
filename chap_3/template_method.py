"""
Template Methodパターン
・処理の枠組みやフローがスーパークラスで決定されていて，サブクラスでその中の部分部分を定義するようなパターン
・要は，共通のロジックを持ったクラスをまとめるパターン．副効果として，AbstractDisplayクラスとサブクラス2つを同一視できている
・この例では，一次元的に3種類の小処理が並んだ大処理が存在し，小処理のそれぞれをサブクラスで定義した感じになっている
  ・大処理を複数用意して，それに必要な小処理をサブクラスで定義させることでもっと多機能化できそう
"""

from abc import ABC, abstractmethod
from typing import final


class AbstractDisplay(ABC):
    @abstractmethod
    def open(self) -> None:
        pass

    @abstractmethod
    def print(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @final
    def display(self) -> None:
        self.open()
        for _ in range(5):
            self.print()
        self.close()


class CharDisplay(AbstractDisplay):
    def __init__(self, ch: str) -> None:
        assert len(ch) == 1
        self.__ch = ch

    # @override
    def open(self) -> None:
        print("<<", end="")

    # @override
    def print(self) -> None:
        print(self.__ch, end="")

    # @override
    def close(self) -> None:
        print(">>")


class StringDisplay(AbstractDisplay):
    def __init__(self, string: str) -> None:
        self.__string = string

    # @override
    def open(self) -> None:
        self.__print_line()

    # @override
    def print(self) -> None:
        print("|{}|".format(self.__string))

    # @override
    def close(self) -> None:
        self.__print_line()

    def __print_line(self) -> None:
        print("+{}+".format("-" * len(self.__string)))


class Main:
    def __init__(self) -> None:  # Javaのmain関数を模して，これをmainとする
        d1: AbstractDisplay = CharDisplay("H")
        d2: AbstractDisplay = StringDisplay("Hello, world.")

        d1.display()
        d2.display()


Main()
