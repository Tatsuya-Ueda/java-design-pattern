"""
Visitorパターン
・データ構造と処理を分離
・Elementが，「Visitorを引数として受け入れるacceptメソッドがある」という大前提を，インターフェースを利用して定義している．
  ・Visitorは引数で順次渡されていく．「データ構造がVisitorを持っている」としてしまうと依存関係がおかしいことを考えると，つじつまが合う．
・Entry，File，DirectoryはCompositeのときとほぼ変わらない．
・VisitorはEntryを継承するインスタンスに対して，ひたすらvisitすることしかできない．
  ・ここではisinstanceを使っているが，Javaだと関数のオーバーロード（多重定義）ができるため，もう少しわかりやすくなるだろうか．
  受け取る引数によって処理が変わらなければならないのに，メソッドが分かれないのがなんとも変な感じがする．ここはJavaに軍配が上がるか．
"""

from abc import ABC, abstractmethod
from typing import List


class Visitor(ABC):
    @abstractmethod
    def visit(self, entry: "Entry"):
        if isinstance(entry, File):
            pass
        elif isinstance(entry, Directory):
            pass
        else:
            assert False


# interface
class Element(ABC):
    @abstractmethod
    def accept(self, sv: "Visitor") -> None:
        pass


class Entry(Element):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass

    # str型との演算を定義
    def __add__(self, s: str):  # self + s の演算結果を定義 (実行されることはないが，気分でこちらも実装)
        assert isinstance(s, str)
        _ = self.get_name() + " ({})".format(self.get_size())
        return _ + s

    def __radd__(self, s: str):  # s + self の演算結果を定義
        assert isinstance(s, str)
        _ = self.get_name() + " ({})".format(self.get_size())
        return s + _


class File(Entry):
    def __init__(self, name: str, size: int) -> None:
        self.__name: str = name
        self.__size: int = size

    # @override
    def get_name(self) -> str:
        return self.__name

    # @override
    def get_size(self) -> int:
        return self.__size

    # @override
    def accept(self, v: "Visitor") -> None:
        v.visit(self)


class Directory(Entry):
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__directory: List[Entry] = []

    # @override
    def get_name(self) -> str:
        return self.__name

    # @override
    def get_size(self) -> int:
        return sum(e.get_size() for e in self.__directory)

    # @override
    def accept(self, v: "Visitor") -> None:
        v.visit(self)

    def add(self, entry: Entry) -> Entry:
        self.__directory += [entry]
        return self

    def __iter__(self):
        self.__cnt = 0
        return self

    def __next__(self):
        if self.__cnt >= len(self.__directory):
            raise StopIteration
        result = self.__directory[self.__cnt]
        self.__cnt += 1
        return result


class ListVisitor(Visitor):
    def __init__(self) -> None:
        self.__current_dir = "C:"

    # @override
    def visit(self, entry: "Entry"):
        if isinstance(entry, File):
            file: File = entry  # 変数名を変えたいだけ

            print(self.__current_dir + "/" + file)
        elif isinstance(entry, Directory):
            directory: Directory = entry  # 変数名を変えたいだけ

            print(self.__current_dir + "/" + directory)
            # 今いるディレクトリのパスをcurrentdirに記憶した状態で
            # 次のEntryをvisitしないといけないのでこうなる(ここはちょっとロジックが難しい)
            savedir = self.__current_dir
            self.__current_dir = self.__current_dir + "/" + directory.get_name()
            for e in directory:
                e.accept(self)
            self.__current_dir = savedir
        else:
            assert False


class Main:
    def __init__(self) -> None:  # Javaのmain関数を模して，これをmainとする
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
        rootdir.accept(ListVisitor())
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
        rootdir.accept(ListVisitor())


Main()
