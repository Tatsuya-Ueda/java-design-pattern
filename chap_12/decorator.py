"""
Decoratorパターン
・デコレータパターンは、入れ子の関係だけを要求するようなクラス階層を組むことが主目的である
・コンストラクタ呼び出し時に入れ子の内側を引数として要求するクラスと、
コンストラクタ呼び出しによる入れ子構造の終端条件を担うクラスが用意されなくてはいけない
・再帰構造ではあるが、Compositeより構造としては弱い。線形にしか繋ぐことができないので、
ディレクトリみたいな木構造を作ることはできないが、手続きを高階関数として記述するために使えるのでパターンとして存在するっぽい。
・デコレータを横並びに増やしていって、欲しい機能の付加をメソッドの入れ子で実現できるようにしよう、というのがモチベーション
・Pythonだと適用したいメソッドをアットマークで書く記法があるからJavaよりは使いやすそう。
ただし、実装するときは、適用する順番に注意したほうがよいかもしれない？(デコレータが順不同に適用されてもバグが起きない、とか)
・Adapterでリストをメソッドの入れ子構造にパースして使いやすくするとかいうアイデア(使いやすいかは別として)
"""

from abc import ABC, abstractmethod
from typing import final


class Display(ABC):
    @abstractmethod
    def get_columns(self) -> int:
        pass

    @abstractmethod
    def get_rows(self) -> int:
        pass

    @abstractmethod
    def get_row_text(self, row: int) -> str:
        pass

    @final
    def show(self) -> None:
        for i in range(self.get_rows()):
            print(self.get_row_text(i))


class StringDisplay(Display):
    def __init__(self, string: str) -> None:
        self.__string = string

    # @override
    def get_columns(self) -> int:
        return len(self.__string)

    # @override
    def get_rows(self) -> int:
        return 1

    # @override
    def get_row_text(self, row: int) -> str:
        assert row == 0
        return self.__string


class Border(Display):
    def __init__(self, display: Display) -> None:
        self._display: Display = display


class SideBorder(Border):
    def __init__(self, display: Display, ch: str) -> None:
        assert len(ch) == 1
        super().__init__(display)
        self.__border_char = ch

    # @override
    def get_columns(self) -> int:
        return 1 + self._display.get_columns() + 1

    # @override
    def get_rows(self) -> int:
        return self._display.get_rows()

    # @override
    def get_row_text(self, row: int) -> str:
        return self.__border_char + self._display.get_row_text(row) + self.__border_char


class FullBorder(Border):
    def __init__(self, display: Display) -> None:
        super().__init__(display)

    # @override
    def get_columns(self) -> int:
        return 1 + self._display.get_columns() + 1

    # @override
    def get_rows(self) -> int:
        return 1 + self._display.get_rows() + 1

    # @override
    def get_row_text(self, row: int) -> str:
        if row == 0:
            return "+" + "-" * self._display.get_columns() + "+"
        elif row == self._display.get_rows() + 1:
            return "+" + "-" * self._display.get_columns() + "+"
        else:
            return "|" + self._display.get_row_text(row - 1) + "|"


class Main:
    def __init__(self) -> None:  # Javaのmain関数を模して，これをmainとする
        b1 = StringDisplay("Hello, world.")
        b2 = SideBorder(b1, "#")
        b3 = FullBorder(b2)
        b1.show()
        b2.show()
        b3.show()
        b4 = SideBorder(
            FullBorder(
                FullBorder(SideBorder(FullBorder(StringDisplay("Hello, world.")), "*"))
            ),
            "/",
        )
        b4.show()


Main()
