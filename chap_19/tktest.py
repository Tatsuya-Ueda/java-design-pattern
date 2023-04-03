import tkinter as tk


class SafeFrame(tk.Tk):
    def __init__(self, *a, **ka):
        super().__init__(*a, **ka)

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
            pass
        elif s == "alarm":
            pass
        elif s == "phone":
            pass
        elif s == "exit":
            pass


s = SafeFrame()

s.mainloop()
