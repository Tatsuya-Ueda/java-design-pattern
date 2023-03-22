"""
Compositeパターン
・容器と中身を同一視して再帰的な構造を作るパターン
・Entryを継承しているDirectoryクラスが，Entryをリストで持つことができる部分がミソ(つまり再帰)
・BNF記法で解釈するなら
<Entry>::=<File>|<Directory>
<Directory>::={<Entry>}
だろうか
・Entryクラスは抽象基底クラスに見えて，実装を含むためmixinであるともいえる
"""

from abc import ABC
from abc import abstractmethod
from typing import List

class Entry(ABC):
    # 継承先クラスでインスタンス変数の定義を強制
    @property
    @abstractmethod
    def name(self) -> str:
        pass
    @property
    @abstractmethod
    def size(self) -> int:
        pass
    
    @abstractmethod
    def print_list(self, prefix: str = ""):
        pass

    # str型との演算を定義
    def __add__(self, s: str): # self + s の演算結果を定義 (実行されることはないが，気分でこちらも実装)
        assert isinstance(s, str)
        _ = self.name + " ({})".format(self.size)
        return _ + s
    def __radd__(self, s: str): # s + self の演算結果を定義
        assert isinstance(s, str)
        _ = self.name + " ({})".format(self.size)
        return s + _

class File(Entry):
    def __init__(self, name: str, size: int) -> None:
        self.__name = name
        self.__size = size

    @property
    def name(self) -> str:
        return self.__name
    @property
    def size(self) -> int:
        return self.__size
    
    def print_list(self, prefix: str = ""):
        print(prefix + "/" + self)

class Directory(Entry):
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__directory: List[Entry] = []
    
    @property
    def name(self) -> str:
        return self.__name
    @property
    def size(self) -> int:
        return sum(e.size for e in self.__directory)

    def print_list(self, prefix: str = ""): # Directory以下のEntryについて再帰的に表示
        print(prefix + "/" + self)
        for e in self.__directory:
            e.print_list(prefix + "/" + self.name)

    def add(self, entry: Entry):
        self.__directory += [entry]
        return self

class Main():
    def __init__(self) -> None: # Javaのmain関数を模して，これをmainとする

        print("Making root entries...")
        rootdir = Directory("root")
        bindir = Directory("bin")
        tmpdir = Directory("tmp")
        usrdir = Directory("usr")
        rootdir.add(bindir)
        rootdir.add(tmpdir)
        rootdir.add(usrdir)
        bindir.add(File("vi", 10000))
        bindir.add(File("latex", 20000))
        rootdir.print_list("")
        print("")

        print("Making user entries...")
        yuki = Directory("yuki")
        hanako = Directory("hanako")
        tomura = Directory("tomura")
        usrdir.add(yuki)
        usrdir.add(hanako)
        usrdir.add(tomura)
        yuki.add(File("diary.html", 100))
        yuki.add(File("Composite.java", 200))
        hanako.add(File("memo.tex", 300))
        tomura.add(File("game.doc", 400))
        tomura.add(File("junk.mail", 500))
        rootdir.print_list()

Main()