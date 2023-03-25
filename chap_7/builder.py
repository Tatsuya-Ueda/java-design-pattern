"""
Builderパターン
"""

from abc import ABC, abstractmethod
from typing import List


class Builder(ABC):
    @abstractmethod
    def make_title(self, title: str) -> None:
        pass

    @abstractmethod
    def make_string(self, string: str) -> None:
        pass

    @abstractmethod
    def make_items(self, items: List[str]) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass


class Director:
    def __init__(self, builder: Builder) -> None:
        self.__builder = builder

    def construct(self) -> None:
        self.__builder.make_title("Greeting")
        self.__builder.make_string("一般的なあいさつ")
        self.__builder.make_items(["How are you?", "Hello.", "Hi."])
        self.__builder.make_string("時間帯に応じたあいさつ")
        self.__builder.make_items(["Good morning.", "Good afternoon.", "Good evening."])
        self.__builder.close()

class TextBuillder(Builder):
    
class Main:
    def __init__(self) -> None:  # Javaのmain関数を模して，これをmainとする
        print("Start.")
        print("End.")


Main()
