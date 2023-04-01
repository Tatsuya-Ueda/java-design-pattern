"""
Builderパターン
・Builderは，文書を作るための機能(API)だけを定める．DirectorはそのAPIを使って，文書を作る手順を定義している．
  ・つまり，Builderには，「文書を構築する」という目的を達成しうる過不足のないメソッド群が定義されている必要がある．
  一方，HTMLやテキストそれぞれに固有なメソッドを含んではいけない．
・Builderの2つの具象クラスは，APIの中身について，それぞれ異なった実装になっている．
・Directorは，担当する(持っている)Builderがどの具象Builderなのかを意識しないでconstructを行う．
・Directorに対して，「あなたにはこの種類のBuilderを与えるので，constructをやってくださいな」と仕事を任せる感じ
"""

from abc import ABC, abstractmethod
from typing import List
import sys


# abstract class
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
    def __init__(self) -> None:
        self.__sb: List[str] = []

    # @override
    def make_title(self, title: str) -> None:
        self.__sb.append("==============================\n")
        self.__sb.append("『")
        self.__sb.append(title)
        self.__sb.append("』\n\n")

    # @override
    def make_string(self, string: str) -> None:
        self.__sb.append("■")
        self.__sb.append(string)
        self.__sb.append("\n\n")

    # @override
    def make_items(self, items: List[str]) -> None:
        for s in items:
            self.__sb.append("　・")
            self.__sb.append(s)
            self.__sb.append("\n")
        self.__sb.append("\n")

    # @override
    def close(self) -> None:
        self.__sb.append("==============================\n")

    def get_text_result(self):
        return "".join(self.__sb)  # 連結する


class HTMLBuilder(Builder):
    def __init__(self) -> None:
        self.__filename: str = "untitled.html"
        self.__sb: List[str] = []

    # @override
    def make_title(self, title: str) -> None:
        self.__filename = title + ".html"
        self.__sb.append("<!DOCTYPE html>\n")
        self.__sb.append("<html>\n")
        self.__sb.append("<head><title>")
        self.__sb.append(title)
        self.__sb.append("</title></head>\n")
        self.__sb.append("<body>\n")
        self.__sb.append("<h1>")
        self.__sb.append(title)
        self.__sb.append("</h1>\n\n")

    # @override
    def make_string(self, string: str) -> None:
        self.__sb.append("<p>")
        self.__sb.append(string)
        self.__sb.append("</p>\n\n")

    # @override
    def make_items(self, items: List[str]) -> None:
        self.__sb.append("<ul>\n")
        for s in items:
            self.__sb.append("<li>")
            self.__sb.append(s)
            self.__sb.append("</li>\n")
        self.__sb.append("</ul>\n\n")

    # @override
    def close(self) -> None:
        self.__sb.append("</body>")
        self.__sb.append("</html>\n")
        with open(self.__filename, "w") as f:
            f.write("".join(self.__sb))

    def get_html_result(self):
        return self.__filename


class Main:
    def __init__(self) -> None:  # Javaのmain関数を模して，これをmainとする
        if len(sys.argv) != 2:
            print("usage: python ___.py [text or html]")
            exit()
        if sys.argv[1] == "text":
            text_builder = TextBuillder()
            director = Director(text_builder)
            director.construct()
            result = text_builder.get_text_result()
            print(result)
        elif sys.argv[1] == "html":
            html_builder = HTMLBuilder()
            director = Director(html_builder)
            director.construct()
            filename = html_builder.get_html_result()
            print("HTMLファイル{}が作成されました．".format(filename))
        else:
            print("usage: python ___.py [text or html]")
            exit()


Main()
