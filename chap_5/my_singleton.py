"""
細けえことはいいから簡易的にサッと自分で実装したい人のためのSingletonパターン
・「Singletonを継承すればSingletonなクラスができる」的な実装はもはや黒魔術に近く，単純に複雑なので，
  クラス一つ一つをSingletonとして実装して，あとは手間かもしれないがローカルルール(規約)で何とかするという発想
"""


class Singleton:
    # クラス変数
    __singleton: None | "Singleton" = None

    # 2回を超えてコンストラクタを呼び出せない
    def __init__(self) -> None:
        # 必要な初期化処理
        # ...

        # インスタンスをクラス変数に登録
        assert (
            self.__class__.__singleton is None
        ), "Singleton class but its constructor called twice"
        self.__class__.__singleton = self

    # コンストラクタを1回呼び出すまでに実行できない
    @classmethod
    def get_instance(cls) -> "Singleton":
        assert cls is not None
        return cls.__singleton


class Main:
    def __init__(self) -> None:  # Javaのmain関数を模して，これをmainとする
        s = Singleton()
        ss = Singleton.get_instance()
        print(id(s))
        print(id(ss))

        Singleton()  # 2回呼ばれるのでエラー


Main()
