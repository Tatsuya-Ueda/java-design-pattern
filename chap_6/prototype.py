"""
Prototypeパターン
・この例だと少しわかりにくいかもしれないが，Productの継承先クラスのインスタンスが状態を持つような場合にメリットがはっきりと現れそうである
e.g.) Productの継承先がある種類の敵のパラメータを持っていて，create_copyで自己複製．こうすると，あるパラメータを持つ敵を複数生成するのが簡単．
・ゲームの例でいえば，ザコ敵1種類1種類をPrototypeの役を持つクラスとするのがよいのかもしれない．
  ・モンスターごとに行動やパラメータは異なり，これはどうしても人間がプログラミングしなければならない．どうしてもモンスターの数ぶんのクラスはできる．
  ・しかし，何度も同じような敵が出てくる以上，敵を出現させるときは，原型を完全に複製するか，複製してちょっと手を加えるのが処理としては楽．
  ・いちいちコンストラクタにパラメタを渡すのはめんどくさいし，インスタンス引数にデフォルト値を設定して対応しようとも「結局インスタンスを生成するときに
    絶対コンストラクタが呼ばれる」という制約ができて小回りが効かなくなりそう．
・JavaにおけるClonableはマーカーインターフェースと呼ばれる中身が空のインターフェースであり，単なる識別子として使われる
・型アノテーションには引用符で囲った文字列を使うこともでき，この場合はundefinedエラーが出ない
"""

from abc import ABC
from abc import abstractmethod
from typing import Dict
from copy import deepcopy


class Product(ABC):  # interface
    @abstractmethod
    def use(self, s: str) -> None:
        pass

    @abstractmethod
    def create_copy(self) -> "Product":  # インスタンスの複製を作るもの
        pass


class Manager:  # uses Product
    def __init__(self) -> None:
        self.__showcase: Dict[str, "Product"] = {}  # JavaにおけるHashMapを辞書で再現

    def register(self, name: str, prototype: Product) -> None:
        self.__showcase.update([(name, prototype)])

    def create(self, prototype_name: str) -> Product:
        p: Product = self.__showcase[prototype_name]
        return p.create_copy()


class MessageBox(Product):  # implements Product
    def __init__(self, decochar: str) -> None:
        assert len(decochar) == 1, "This argument needs to be 1 character string."
        self.__decochar = decochar

    # @override
    def use(self, s: str):
        decolen = 1 + len(s) + 1
        print(self.__decochar * decolen)
        print(self.__decochar + s + self.__decochar)
        print(self.__decochar * decolen)

    def create_copy(self) -> "Product":
        return deepcopy(self)


class UnderlinePen(Product):  # implements Product
    def __init__(self, ulchar: str) -> None:
        assert len(ulchar) == 1, "This argument needs to be 1 character string."
        self.__ulchar = ulchar

    # @override
    def use(self, s: str) -> None:
        ulen = len(s)
        print(s)
        print(self.__ulchar * ulen)

    # @override
    def create_copy(self) -> "Product":
        return deepcopy(self)


class Main:
    def __init__(self) -> None:  # Javaのmain関数を模して，これをmainとする
        # 準備
        manager = Manager()
        upen = UnderlinePen("-")
        mbox = MessageBox("*")
        sbox = MessageBox("/")

        # 登録
        manager.register("strong message", upen)
        manager.register("warning box", mbox)
        manager.register("slash box", sbox)

        # 生成と使用
        p1 = manager.create("strong message")
        p1.use("Hello, world.")

        p2 = manager.create("warning box")
        p2.use("Hello, world.")

        p3 = manager.create("slash box")
        p3.use("Hello, world.")


Main()
