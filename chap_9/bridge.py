"""
Bridgeパターン
・必要な機能をサブクラスで順次定義していくことがしばしばある．この方法でどこまでも進んでいこうとすると，スーパークラスで定義されたメソッドのより具体的な処理を
実装したいことも，スーパークラスでは定義されていない機能の追加をしたいこともあるため，「機能のクラス階層と実装のクラス階層の混在」が起きてクラス階層を煩雑
にしてしまう．これを避けたいというのがモチベーション．
・Displayクラスの機能追加版が，CountDisplayクラス．これが「機能のクラス階層」と言われる部分．両クラスとも，中身がまるで「手順のひな形」のように見える．
・DisplayImplは必要なあらゆる基本機能の名前だけ(API)を定義する．StringDisplayTmplが，その基本機能の実際の実装を定義する．StringDisplayTmplに相当するクラス
の類型を作る（ヨコに増やす）と，APIの実装の版を複数種類に分けることができる(重要)．APIの版を複数用意しておき，版を挿げ替えてAPI呼び出せるため，ここで「委譲」
を使っている．
・APIがほとんど決まっていて，APIの変更がおおむね起きないが，実装のバージョンをいくつか持っていなくてはいけない場合に有効そう．
・ぶっちゃけ機能の階層のほうはそんなに重要じゃないのでは？
・実装と機能の階層と言ってしまうので，タテの階層化を意識してしまいやすいが，どちらかというとヨコが重要．「あるAPIに対して複数の実装を用意することと，
機能を継承によって階層化することを，簡潔な形で両立するためのパターン」といえる．
"""


from abc import ABC, abstractmethod


class Display:
    def __init__(self, impl: "DisplayImpl") -> None:
        self.__impl: "DisplayImpl" = impl

    def open(self) -> None:
        self.__impl.raw_open()

    def print(self) -> None:
        self.__impl.raw_print()

    def close(self) -> None:
        self.__impl.raw_close()

    def display(self):
        self.open()
        self.print()
        self.close()


class CountDisplay(Display):
    def __init__(self, impl: "DisplayImpl") -> None:
        super().__init__(impl)

    def multi_display(self, times: int):
        self.open()
        for _ in range(times):
            self.print()
        self.close()


class DisplayImpl(ABC):
    @abstractmethod
    def raw_open(self):
        pass

    @abstractmethod
    def raw_print(self):
        pass

    @abstractmethod
    def raw_close(self):
        pass


class StringDisplayImpl(DisplayImpl):
    def __init__(self, string) -> None:
        self.__string = string

    # @override
    def raw_open(self):
        self.print_line()

    # @override
    def raw_print(self):
        print("|{}|".format(self.__string))

    # @override
    def raw_close(self):
        self.print_line()

    def print_line(self):
        print("+{}+".format("-" * len(self.__string)))


class Main:
    def __init__(self) -> None:  # Javaのmain関数を模して，これをmainとする
        d1: Display = Display(StringDisplayImpl("Hello, Japan."))
        d2: Display = CountDisplay(StringDisplayImpl("Hello, World."))
        d3: CountDisplay = CountDisplay(StringDisplayImpl("Hello, Universe."))

        d1.display()
        d2.display()
        d3.display()
        d3.multi_display(5)


Main()
