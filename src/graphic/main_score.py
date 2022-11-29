from tkinter import *


class MainScore:
    def __init__(self, root):
        self.score_blue = Label(text="0", width=3, height=3, bg='blue', borderwidth=2, relief="raised", font='Times 60')
        self.score_blue.grid(row=10, column=2, sticky='we', padx=(0, 5), pady=(30, 20))

        # TODO: общий счет добавить потом отдельно создав отдельный грид
        self.score_white = Label(text="0", width=3, height=3, bg='white', borderwidth=2, relief="raised",
                                 font='Times 60')
        self.score_white.grid(row=4, column=0, sticky='we', padx=(0, 5), pady=(30, 20))

    @property
    def blue(self):
        return self.score_blue

    @property
    def white(self):
        return self.score_white
