import tkinter as tk


class Problem(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Solve Problem")

        self.state = True

        self.label_text = tk.StringVar()
        self.label_text = "Button Click"

        self.label = tk.Label(self, text=self.label_text)
        self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=30)

        self.bnt_hello = tk.Button(self, text="Hello", command=self.greeting1)
        self.bnt_hello.pack(side=tk.LEFT, padx=20, pady=20)

        self.bnt_bye = tk.Button(self, text="Bye", command=self.greeting2)
        self.bnt_bye.pack(side=tk.RIGHT, padx=20, pady=20)

    # 상태 변환
    def greeting1(self):
        if self.state:
            self.bnt_hello.configure(text="Hello !!")
            self.state = not self.state
        else:
            self.bnt_hello.configure(text="Hello")
            self.state = not self.state

    def greeting2(self):
        self.bnt_bye.configure(text="Goodbye !!")
        self.after(2000, self.destroy)


if __name__ == "__main__":
    win = Problem()
    win.mainloop()

