"""
Adapterパターン(移譲を使った例)
・こちらの例でも結局，Printを用意している．(こちらはinterfaceではなくabstract Printではあるが)
・Adapteeのメソッドへのアクセス制限を行いたいなら委譲．Adapter側で定義されなければ呼び出されないため．
"""


from abc import ABC, abstractmethod


class Banner:
    def __init__(self, string: str) -> None:
        self.__string: str = string

    def show_with_paren(self) -> None:
        print("({})".format(self.__string))

    def show_with_aster(self) -> None:
        print("*{}*".format(self.__string))


class Print(ABC):
    @abstractmethod
    def print_weak(self) -> None:
        pass

    @abstractmethod
    def print_strong(self) -> None:
        pass


class PrintBanner(Print):
    def __init__(self, string: str) -> None:
        self.__banner = Banner(string)

    # @override
    def print_weak(self) -> None:
        self.__banner.show_with_paren()

    # @override
    def print_strong(self) -> None:
        self.__banner.show_with_aster()


class Main:
    def __init__(self) -> None:  # Javaのmain関数を模して，これをmainとする
        p: Print = PrintBanner("Hello")
        p.print_weak()
        p.print_strong()


Main()
