"""
Stateパターン
・GoFの中でも屈指の難解さ！
・Stateインターフェースで定めたメソッドの第1引数にはContextが入る．インターフェースContextを実装しているクラスは，Contextで定義されたAPIが
  実装されている．Stateにcontextを引数で渡すと，今度はState側が，Contextを実装したクラスのメソッドを呼びに行く
・具象Stateで定義されたメソッドに自身のインスタンスを参照で渡す(これがContextが引数になっていることに該当する)ことで，自クラスで実装された
  メソッド(なおこれはContextで定義されたAPI)を使って，具象Stateに応じた処理をしてくれる．

・結局よくわからん
・あとでみる
  https://qiita.com/Gorayan/items/92baa9108985d79e2ef9
"""


import tkinter as tk
from abc import ABC, abstractmethod


class Context(ABC):
    @abstractmethod
    def set_clock(self, hour: int) -> None:
        pass

    @abstractmethod
    def change_state(self, nextstate: "State") -> None:
        pass

    @abstractmethod
    def call_security_center(self, msg: str) -> None:
        pass

    @abstractmethod
    def record_log(self, msg: str) -> None:
        pass


# 状態に対するAPI(機能)を定義
# interface
class State(ABC):
    @abstractmethod
    def do_clock(self, context: Context, hour: int):
        pass

    @abstractmethod
    def do_use(self, context: Context):
        pass

    @abstractmethod
    def do_alarm(self, context: Context):
        pass

    @abstractmethod
    def do_phone(self, context: Context):
        pass

    def to_string(self):
        pass


class NightState(State):
    # クラス変数
    __singleton = None

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
    def get_instance(cls) -> "NightState":
        assert cls is not None
        return cls.__singleton

    # @override
    def do_clock(self, context: Context, hour: int):
        # ある範囲に時間が来ると，Contextが実装されたクラスのchange_stateを呼ぶ
        if 9 <= hour and hour < 17:
            context.change_state(DayState.get_instance())

    # @override
    def do_use(self, context: Context):
        context.call_security_center(msg="非常：夜間に金庫使用")

    # @override
    def do_alarm(self, context: Context):
        context.call_security_center(msg="非常ベル(夜間)")

    # @override
    def do_phone(self, context: Context):
        context.record_log(msg="夜間の通話録音")

    def to_string(self):
        return "[夜間]"


class DayState(State):
    # クラス変数
    __singleton = None

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
    def get_instance(cls) -> "DayState":
        assert cls is not None
        return cls.__singleton

    # @override
    def do_clock(self, context: Context, hour: int):
        # ある範囲に時間が来ると，Contextが実装されたクラスのchange_stateを呼ぶ
        if hour < 9 or 17 <= hour:
            context.change_state(NightState.get_instance())

    # @override
    def do_use(self, context: Context):
        context.record_log(msg="金庫使用(昼間)")

    # @override
    def do_alarm(self, context: Context):
        context.call_security_center(msg="非常ベル(昼間)")

    # @override
    def do_phone(self, context: Context):
        context.call_security_center(msg="通常の通話(昼間)")

    def to_string(self):
        return "[昼間]"


class SafeFrame(tk.Tk, Context):
    def __init__(self, *a, **ka):
        super().__init__(*a, **ka)

        # SafeFrame固有の初期化
        self.state: State = DayState.get_instance()

        # windowの初期化
        self.geometry("300x150+50+50")

        self.button_use = tk.Button(
            master=self, text="金庫使用", command=lambda: self.action_performed("use")
        )
        self.button_alarm = tk.Button(
            master=self, text="非常ベル", command=lambda: self.action_performed("alarm")
        )
        self.button_phone = tk.Button(
            master=self, text="通常通話", command=lambda: self.action_performed("phone")
        )
        self.button_exit = tk.Button(
            master=self, text="終了", command=lambda: self.action_performed("exit")
        )
        self.button_use.pack()
        self.button_alarm.pack()
        self.button_phone.pack()
        self.button_exit.pack()

    def action_performed(self, s: str):
        if s == "use":
            self.state.do_use(self)
        elif s == "alarm":
            self.state.do_alarm(self)
        elif s == "phone":
            self.state.do_phone(self)
        elif s == "exit":
            exit(0)
        else:
            print("?")

    # @override
    def set_clock(self, hour: int) -> None:
        print("現在時刻は{}:00".format(hour))
        self.state.do_clock(self, hour)

    # 状態遷移を行うのは自分(Contextを実装しているクラス)だが，
    # 次の状態を投げてくれるのは状態である
    # @override
    def change_state(self, nextstate: "State") -> None:
        print("{}から{}へ状態が変化しました．".format(self.state.to_string(), nextstate.to_string()))
        self.state = nextstate

    # @override
    def call_security_center(self, msg: str) -> None:
        print("call! {}".format(msg))

    # @override
    def record_log(self, msg: str) -> None:
        print("record... {}".format(msg))


class Main:
    def __init__(self) -> None:  # Javaのmain関数を模して，これをmainとする
        NightState()  # やむなくSingletonの初期化
        DayState()  # やむなくSingletonの初期化

        self.hour = 0

        self.frame = SafeFrame()
        self.frame.after(1000, self.loop)
        self.frame.mainloop()

    def loop(self):
        self.frame.set_clock(self.hour)
        self.hour += 1
        if self.hour >= 24:
            self.hour = 0
        self.frame.after(1000, self.loop)


Main()
