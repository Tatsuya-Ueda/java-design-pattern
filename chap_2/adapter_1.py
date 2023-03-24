"""
Adapterパターン(継承を使った例)
・interface Print(APIのひな形となるインターフェース)を用意して，実装したいAPI(Adapt，適応させた後のクラス)でimplementsし
  ，実際に実装する，という二段階になっている
・継承ではAdapteeのメソッドを何もせず使うことができるが，委譲ではAdapteeのインスタンスを使っていちいちAdapter側のメソッドを
  定義する必要が出てくる．トレードオフの関係にありそう．
・interfaceいらないのでは？Adapt後のクラスだけ用意すればよいのでは？と思ってしまった．
"""


from abc import ABC, abstractmethod


# Adaptee
class Banner:
    def __init__(self, string: str) -> None:
        self.__string: str = string

    def show_with_paren(self) -> None:
        print("({})".format(self.__string))

    def show_with_aster(self) -> None:
        print("*{}*".format(self.__string))


# Target of adaptation
class Print(ABC):  # interface
    @abstractmethod
    def print_weak(self) -> None:
        pass

    @abstractmethod
    def print_strong(self) -> None:
        pass


# Adapter
class PrintBanner(Banner, Print):  # implements Print
    def __init__(self, string: str) -> None:
        super().__init__(string)

    # @override
    def print_weak(self) -> None:
        self.show_with_paren()

    # @override
    def print_strong(self) -> None:
        self.show_with_aster()


class Main:
    def __init__(self) -> None:  # Javaのmain関数を模して，これをmainとする
        p: Print = PrintBanner("Hello")
        p.print_weak()
        p.print_strong()


Main()
