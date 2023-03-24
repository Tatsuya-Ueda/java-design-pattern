"""
Factory Methodパターン
・注：テキストではパッケージ分けを行っているが，ここではデザインパターンの学習のため一つのファイルに収める
"""

from abc import ABC, abstractmethod
from typing import final


class Product(ABC):
    @abstractmethod
    def use(self):
        pass


class Factory(ABC):
    @final
    def create(self, owner: str) -> Product:
        p: Product = self.create_product(owner)
        self.register_product(p)
        return p

    @abstractmethod
    def create_product(self, owner: str) -> Product:
        pass

    @abstractmethod
    def register_product(self, product: Product) -> None:
        pass


class IDCard(Product):
    def __init__(self, owner: str) -> None:
        print(owner + "のカードを作ります．")
        self.__owner = owner

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner: str):
        self.__owner = owner

    # @override
    def use(self) -> None:
        print(self + "を使います．")

    # str型との演算を定義
    def __add__(self, s: str):  # self + s の演算結果を定義
        assert isinstance(s, str)
        _ = "[IDCard:{}]".format(self.__owner)
        return _ + s

    def __radd__(self, s: str):  # s + self の演算結果を定義
        assert isinstance(s, str)
        _ = "[IDCard:{}]".format(self.__owner)
        return s + _


class IDCardFactory(Factory):
    # @override
    def create_product(self, owner: str) -> Product:
        return IDCard(owner)

    # @override
    def register_product(self, product: Product) -> None:
        print(product + "を登録しました．")


class Main:
    def __init__(self) -> None:  # Javaのmain関数を模して，これをmainとする
        factory: Factory = IDCardFactory()
        card1: Product = factory.create("Hiroshi Yuki")
        card2: Product = factory.create("Tomura")
        card3: Product = factory.create("Hanako Sato")
        card1.use()
        card2.use()
        card3.use()


Main()
