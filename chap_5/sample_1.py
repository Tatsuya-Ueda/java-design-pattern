"""
某qiitaのサンプルプログラムほぼそのまま+コメント
"""


# 継承先クラスにSingletonパターンを適用するためのクラス
# __init__の前に呼ばれるメソッドである__new__に仕掛けを仕込む
class Singleton(object):
    def __new__(cls, *args, **kwargs):  # 継承先クラスがclsに入る
        if not hasattr(cls, "_instance"):  # 継承先クラスで__instanceが定義されているなら
            cls._instance = super().__new__(cls)
        return cls._instance


class Myclass(Singleton):
    def __init__(self, input):
        self.input = input


class Main:
    def __init__(self) -> None:  # Javaのmain関数を模して，これをmainとする
        one = Myclass(1)
        print("one.input={0}".format(one.input))
        two = Myclass(2)
        print("one.input={0}, two.input={1}".format(one.input, two.input))
        one.input = 0
        print("one.input={0}, two.input={1}".format(one.input, two.input))


Main()
