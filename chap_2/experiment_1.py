"""
Printクラス(一つ目の例ではインターフェース，二つ目の例では抽象基底クラス)がいらないのでは？と思った人のための実験
・やっぱりこの例だと，adapter_1.pyと変わらなくないか？interface Printを用意するうまみが感じられない．
・基本，委譲でいいのではないか．Adaptee側クラスのインスタンスをラップする形のため，Adaptee側クラスのふるまいを
  細かく考える必要はなく手軽．
"""


class Banner:
    def __init__(self, string: str) -> None:
        self.__string: str = string

    def show_with_paren(self) -> None:
        print("({})".format(self.__string))

    def show_with_aster(self) -> None:
        print("*{}*".format(self.__string))


class PrintBanner(Banner):
    def __init__(self, string: str) -> None:
        super().__init__(string)

    def print_weak(self) -> None:
        self.show_with_paren()

    def print_strong(self) -> None:
        self.show_with_aster()


class Main:
    def __init__(self) -> None:  # Javaのmain関数を模して，これをmainとする
        p = PrintBanner("Hello")
        p.print_weak()
        p.print_strong()


Main()
