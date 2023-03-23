"""
Adapterパターン(継承を使った例)
・適合される，adapteeの役を持つのがBanner，
"""

from abc import ABC, abstractmethod


class Banner:
    def __init__(self, string: str) -> None:
        self.__string: str = string

    def show_with_paren(self) -> None:
        print("({})".format(self.__string))

    def show_with_aster(self) -> None:
        print("*{}*".format(self.__string))


class Print(ABC):  # interface
    @abstractmethod
    def print_weak(self) -> None:
        pass

    @abstractmethod
    def print_strong(self) -> None:
        pass


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
