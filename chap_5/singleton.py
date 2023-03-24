"""
Singletonパターン
・あえてSingletonクラスを継承することで，Singletonパターンを適用する形をとった
・次のqiita記事のものを参考に作成
  https://qiita.com/ttsubo/items/c4af71ceba15b5b213f8
"""


class Singleton:
    def __new__(cls, *args, **kwargs):  # 継承先クラスがclsに入る
        if not hasattr(cls, "_instance"):  # 継承先クラスで__instanceが定義されているなら
            cls._instance = super().__new__(cls)  # ここ意味不明
            print("インスタンスを生成しました")
        return cls._instance


class MyClass(Singleton):
    pass


class Main:
    def __init__(self) -> None:  # Javaのmain関数を模して，これをmainとする
        print("Start.")
        obj1: MyClass = MyClass()
        obj2: MyClass = MyClass()
        print(obj1 is obj2)
        print("End.")


Main()
