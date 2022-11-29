from tkinter import *

from src.logic.hansoku import HansokyMouseClick
from src.logic.points import SideType, MarkType, MouseClick


class BlueSide:
    def __init__(self,root,score_white,score_blue):
        self.score_blue = score_blue
        self.score_white = score_white

        blue_gr = Frame(root)
        blue_gr.grid(row=0, column=2, rowspan=2, pady=(10, 10))

        t_side_lable = Label(blue_gr, text=SideType.BLUE.value, font='Times 24')
        t_side_lable.grid(row=0, column=0,columnspan=12,sticky='nsew')

        t_koka_lable = Label(blue_gr,text="KOKA", font='Times 18')
        t_koka_lable.grid(row=1, column=0,columnspan=4,sticky='nsew')

        t_yuko_lable = Label(blue_gr,text="YUKO", font='Times 18')
        t_yuko_lable.grid(row=1, column=4,columnspan=4,sticky='nsew')

        t_wari_lable = Label(blue_gr,text="W-ARI", font='Times 18')
        t_wari_lable.grid(row=1, column=8,columnspan=4,sticky='nsew')

        # TODO: переписать width,height под проценты

        click = MouseClick()

        b_koka = Label(blue_gr,text="0",width=5, height=4, bg='blue',borderwidth = 2, relief="raised",  font='Times 36')
        b_koka.bind('<Button-1>', lambda event: click.left_click(MarkType.KOKA, b_koka, self.score_blue))
        b_koka.bind('<Button-3>', lambda event: click.right_click(MarkType.KOKA,b_koka,self.score_blue))
        b_koka.grid(row=2, column=0,columnspan=4,rowspan=6,sticky='nsew',padx=(5, 5))

        b_yuko = Label(blue_gr,text="0", width=5, height=4, bg='blue', borderwidth=2, relief="raised", font='Times 36')
        b_yuko.bind('<Button-1>', lambda event: click.left_click(MarkType.YUKO, b_yuko, self.score_blue))
        b_yuko.bind('<Button-3>', lambda event: click.right_click(MarkType.YUKO, b_yuko, self.score_blue))
        b_yuko.grid(row=2, column=4,columnspan=4,rowspan=6,sticky='nsew',padx=(5, 5))

        b_wari = Label(blue_gr,text="0",width=5, height=4, bg='blue', borderwidth = 2, relief="raised", font='Times 36')
        b_wari.bind('<Button-1>', lambda event: click.left_click(MarkType.WARI, b_wari, self.score_blue))
        b_wari.bind('<Button-3>', lambda event: click.right_click(MarkType.WARI, b_wari, self.score_blue))
        b_wari.grid(row=2, column=8,columnspan=4,rowspan=6,sticky='nsew',padx=(5, 5))



        # # TODO: общий счет добавить потом отдельно создав отдельный грид
        # self.score_blue = Label(text="0",width=3, height=3,  bg='blue', borderwidth = 2, relief="raised", font='Times 60')
        # self.score_blue.grid(row=10, column=2, sticky='we',padx=(0, 5),pady=(30,20))

        click_hausoku = HansokyMouseClick()

        hansoku_one = Label(blue_gr, width=12, height=6, bg='white', borderwidth=2, relief="raised")
        hansoku_one.grid(row=8, column=0,columnspan=3,rowspan=2, sticky='nsew', pady=(10, 0), padx=(55, 10))
        print(self.score_white)
        hansoku_one.bind('<Button-1>', lambda event: click_hausoku.left_click(hansoku_one, self.score_white))

        hansoku_two = Label(blue_gr, width=12, height=6, bg='white', borderwidth=2, relief="raised")
        hansoku_two.grid(row=8, column=3,columnspan=3,rowspan=2, sticky='nsew', pady=(10, 0), padx=(10, 10))
        # hansoku_two.bind('<Button-1>', lambda event: push_hansoku(event, hansoku_two_blue))

        hansoku_three_blue = Label(blue_gr, width=12, height=6, bg='white', borderwidth=2, relief="raised")
        hansoku_three_blue.grid(row=8, column=6,columnspan=3,rowspan=2, sticky='nsew', pady=(10, 0), padx=(10, 10))
        # hansoku_three_blue.bind('<Button-1>', lambda event: push_hansoku(event, hansoku_three_blue))

        hansoku_four_blue = Label(blue_gr, width=12, height=6, bg='white', borderwidth=2, relief="raised")
        hansoku_four_blue.grid(row=8, column=9,columnspan=3,rowspan=2, sticky='nsew', pady=(10, 0), padx=(10, 10))
        # hansoku_four_blue.bind('<Button-1>', lambda event: push_hansoku(event, hansoku_four_blue))


