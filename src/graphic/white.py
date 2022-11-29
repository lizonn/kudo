from tkinter import *

from src.logic.points import MouseClick, MarkType,SideType


class WhiteSide:
    def __init__(self,root,score_white,score_blue):
        self.score_blue = score_blue
        self.score_white = score_white

        white_gr = Frame(root)
        white_gr.grid(row=0, column=0, rowspan=2, pady=(10, 10))

        t_side_lable = Label(white_gr, text=SideType.WHITE.value, font='Times 24')
        t_side_lable.grid(row=0, column=0,columnspan=12,sticky='nsew')

        t_koka_lable = Label(white_gr,text="KOKA", font='Times 18')
        t_koka_lable.grid(row=1, column=0,columnspan=4,sticky='nsew')

        t_yuko_lable = Label(white_gr,text="YUKO", font='Times 18')
        t_yuko_lable.grid(row=1, column=4,columnspan=4,sticky='nsew')

        t_wari_lable = Label(white_gr,text="W-ARI", font='Times 18')
        t_wari_lable.grid(row=1, column=8,columnspan=4,sticky='nsew')

        # TODO: переписать width,height под проценты

        click = MouseClick()

        b_koka = Label(white_gr,text="0",width=5, height=4, bg='white',borderwidth = 2, relief="raised",  font='Times 36')
        b_koka.bind('<Button-1>', lambda event: click.left_click(MarkType.KOKA, b_koka, self.score_white))
        b_koka.bind('<Button-3>', lambda event: click.right_click(MarkType.KOKA,b_koka,self.score_white))
        b_koka.grid(row=2, column=0,columnspan=4,rowspan=6,sticky='nsew',padx=(5, 5))

        b_yuko = Label(white_gr,text="0", width=5, height=4, bg='white', borderwidth=2, relief="raised", font='Times 36')
        b_yuko.bind('<Button-1>', lambda event: click.left_click(MarkType.YUKO, b_yuko, self.score_white))
        b_yuko.bind('<Button-3>', lambda event: click.right_click(MarkType.YUKO, b_yuko, self.score_white))
        b_yuko.grid(row=2, column=4,columnspan=4,rowspan=6,sticky='nsew',padx=(5, 5))

        b_wari = Label(white_gr,text="0",width=5, height=4, bg='white', borderwidth = 2, relief="raised", font='Times 36')
        b_wari.bind('<Button-1>', lambda event: click.left_click(MarkType.WARI, b_wari, self.score_white))
        b_wari.bind('<Button-3>', lambda event: click.right_click(MarkType.WARI, b_wari, self.score_white))
        b_wari.grid(row=2, column=8,columnspan=4,rowspan=6,sticky='nsew',padx=(5, 5))



        # # TODO: общий счет добавить потом отдельно создав отдельный грид
        # self.score_white = Label(text="0",width=3, height=3,  bg='white', borderwidth = 2, relief="raised", font='Times 60')
        # self.score_white.grid(row=4, column=0, sticky='we',padx=(0, 5),pady=(30,20))




