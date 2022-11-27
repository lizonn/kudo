

def action_left (event,name,side):
    if (name == koka) or (name == koka_blue):
        side.config(text=int(side.cget("text")) + 1)
    elif (name == yuko) or (name == yuko_blue):
        side.config(text=int(side.cget("text")) + 2)
    elif (name == wari) or (name == wari_blue):
        side.config(text=int(side.cget("text")) + 4)


    name.config(text=int(name.cget("text")) + 1)


def action_right(event, name,side):

    if (int(side.cget("text")) > 0) and (int(name.cget("text")) > 0):
        if (name == koka) or (name == koka_blue):
            side.config(text=int(side.cget("text")) - 1)
        elif (name == yuko) or (name == yuko_blue):
            side.config(text=int(side.cget("text")) - 2)
        elif (name == wari) or (name == wari_blue):
            side.config(text=int(side.cget("text")) - 4)

    name.config(text=int(name.cget("text")) - 1) if int(name.cget("text")) > 0 else None





# root.tk.call('tk', 'scaling', 1.0)

# root.tk.call('tk', 'scaling', 1.5)
#
blue_gr = Frame(root)
blue_gr.grid(row=1, column=0,columnspan=3, pady=(10, 10))
side = Label(blue_gr,text="Белый",font='Times 24')
side.grid(row=0, column=1)
# side = Label(text="Синий",font='Times 24')
# side.grid(row=1, column=0,columnspan=3, pady=(10, 20))

text = Label(text="KOKA",font='Times 18')
text.grid(row=2, column=0, sticky='we',padx=(30, 0))
# text.grid(row=2, column=0, sticky='we',padx=(90, 0))
koka_blue = Label(text="0",width=5, height=4, bg='white',borderwidth = 2, relief="raised",  font='Times 36')
koka_blue.bind('<Button-1>', lambda event: action_left (event,koka_blue,score_blue))
koka_blue.bind('<Button-3>', lambda event: action_right(event,koka_blue,score_blue))
koka_blue.grid(row=3, column=0, sticky='we',padx=(30, 5))


text_yuko = Label(text="YUKO",font='Times 18')
text_yuko.grid(row=2, column=2, sticky='we')
yuko_blue = Label(text="0",width=5, height=4, bg='white', borderwidth = 2, relief="raised", font='Times 36')
yuko_blue.bind('<Button-1>', lambda event: action_left (event,yuko_blue,score_blue))
yuko_blue.bind('<Button-3>', lambda event: action_right(event,yuko_blue,score_blue))
yuko_blue.grid(row=3, column=1, sticky='we',padx=(5, 5))


text_wari = Label(text="W-ARI",font='Times 18')
text_wari.grid(row=2, column=1, sticky='we')
wari_blue = Label(text="0",width=5, height=4, bg='white', borderwidth = 2, relief="raised", font='Times 36')
wari_blue.bind('<Button-1>', lambda event: action_left (event,wari_blue,score_blue))
wari_blue.bind('<Button-3>', lambda event: action_right(event,wari_blue,score_blue))
wari_blue.grid(row=3, column=2, sticky='we',padx=(5, 5))


score_blue = Label(text="0",width=3, height=3,  bg='white', borderwidth = 2, relief="raised", font='Times 60')
score_blue.grid(row=6, column=1, sticky='we',padx=(0, 5),pady=(30,20))



# белая сторона
white_gr = Frame(root)
white_gr.grid(row=1, column=5,columnspan=3, pady=(10, 10))
side = Label(white_gr,text="Синий",font='Times 24')
side.grid(row=0, column=1)

text = Label(text="KOKA",font='Times 18')
text.grid(row=2, column=5, sticky='we')
koka = Label(text="0",width=5, height=4, bg='blue',borderwidth = 2, relief="raised",  font='Times 36')
koka.bind('<Button-1>', lambda event: action_left (event,koka,score_white))
koka.bind('<Button-3>', lambda event: action_right(event,koka,score_white))
koka.grid(row=3, column=5, sticky='we',padx=(5, 5))


text_yuko = Label(text="YUKO",font='Times 18')
text_yuko.grid(row=2, column=6, sticky='we')
yuko = Label(text="0",width=5, height=4, bg='blue', borderwidth = 2, relief="raised", font='Times 36')
yuko.bind('<Button-1>', lambda event: action_left (event,yuko,score_white))
yuko.bind('<Button-3>', lambda event: action_right(event,yuko,score_white))
yuko.grid(row=3, column=6, sticky='we',padx=(5, 5))


text_wari = Label(text="W-ARI",font='Times 18')
text_wari.grid(row=2, column=7, sticky='we',padx=(0, 30))
wari = Label(text="0",width=5, height=4, bg='blue', borderwidth = 2, relief="raised", font='Times 36')
wari.bind('<Button-1>', lambda event: action_left (event,wari,score_white))
wari.bind('<Button-3>', lambda event: action_right(event,wari,score_white))
wari.grid(row=3, column=7, sticky='we',padx=(5, 30))


score_white = Label(text="0",width=3, height=3, bg='blue', borderwidth = 2, relief="raised", font='Times 60')
score_white.grid(row=6, column=6, sticky='we',padx=(5, 5),pady=(30,20))


###############################################
# hansoku

title_hansoku = Label(text="Hansoku",font='Times 24')
title_hansoku.grid(row=4, column=0,columnspan=3, pady=(30, 20) )
title_hansoku_white = Label(text="Hansoku",font='Times 24')
title_hansoku_white.grid(row=4, column=5,columnspan=3, pady=(30, 20) )

#
blue_counter = 0
white_counter = 0
def push_hansoku(event,name,):
    global  blue_counter
    if (name == hansoku_one_blue):
        if (name.cget("bg") != 'red'):
            name.config(bg='red')
            blue_counter += 1
            if (blue_counter > 1) and (blue_counter < 4):
                score_white.config(text=int(score_white.cget("text")) + 1)
        else:
            if (blue_counter > 1) and (blue_counter < 4):
                score_white.config(text=int(score_white.cget("text")) - 1)
            name.config(bg='white')
            blue_counter -= 1
    elif name == hansoku_two_blue:
        if (name.cget("bg") != 'red'):
            name.config(bg='red')
            blue_counter += 1
            if (blue_counter > 1) and (blue_counter < 4):
                score_white.config(text=int(score_white.cget("text")) + 1)
        else:
            name.config(bg='white')
            if (blue_counter > 1) and (blue_counter < 4):
                score_white.config(text=int(score_white.cget("text")) - 1)
            blue_counter -= 1
    elif name == hansoku_three_blue:
        if (name.cget("bg") != 'red'):
            name.config(bg='red')
            blue_counter += 1
            if (blue_counter > 1) and (blue_counter < 4):
                score_white.config(text=int(score_white.cget("text")) + 1)
        else:
            if (blue_counter > 1) and (blue_counter < 4):
                score_white.config(text=int(score_white.cget("text")) - 1)
            name.config(bg='white')
            blue_counter -= 1
    elif name == hansoku_four_blue:
        if (name.cget("bg") != 'red'):
            name.config(bg='red')
            blue_counter += 1
            if (blue_counter > 1) and (blue_counter < 4):
                score_white.config(text=int(score_white.cget("text")) + 1)
        else:
            if (blue_counter > 1) and (blue_counter < 4):
                score_white.config(text=int(score_white.cget("text")) - 1)
            name.config(bg='white')
            blue_counter -= 1


def push_hansoku_white(event,name):
    global white_counter
    if (name == hansoku_one_white):
        if (name.cget("bg") != 'red'):
            name.config(bg='red')
            white_counter += 1
            if (white_counter > 1) and (white_counter < 4):
                score_blue.config(text=int(score_blue.cget("text")) + 1)
        else:
            if (white_counter > 1) and (white_counter < 4):
                score_blue.config(text=int(score_blue.cget("text")) - 1)
            name.config(bg='white')
            white_counter -= 1
    elif name == hansoku_two_white:
        if (name.cget("bg") != 'red'):
            name.config(bg='red')
            white_counter += 1
            if (white_counter > 1) and (white_counter < 4):
                score_blue.config(text=int(score_blue.cget("text")) + 1)
        else:
            name.config(bg='white')
            if (white_counter > 1) and (white_counter < 4):
                score_blue.config(text=int(score_blue.cget("text")) - 1)
            white_counter -= 1
            # score_blue.config(text=int(score_blue.cget("text")) - 1)
    elif name == hansoku_three_white:
        if (name.cget("bg") != 'red'):
            name.config(bg='red')
            white_counter += 1
            if (white_counter > 1) and (white_counter < 4):
                score_blue.config(text=int(score_blue.cget("text")) + 1)
        else:
            if (white_counter > 1) and (white_counter < 4):
                score_blue.config(text=int(score_blue.cget("text")) - 1)
            name.config(bg='white')
            white_counter -= 1
    elif name == hansoku_four_white:
        if (name.cget("bg") != 'red'):
            name.config(bg='red')
            white_counter += 1
            if (white_counter > 1) and (white_counter < 4):
                score_blue.config(text=int(score_blue.cget("text")) + 1)
        else:
            if (white_counter > 1) and (white_counter < 4):
                score_blue.config(text=int(score_blue.cget("text")) - 1)
            name.config(bg='white')
            white_counter -= 1



blue_side = Frame(root)
blue_side.grid(row=4, column=0, sticky='we',columnspan=3,padx=(20, 20))

hansoku_one_blue = Label(blue_side,width=12, height=6, bg='white', borderwidth = 2, relief="raised")
hansoku_one_blue.grid(row=0, column=0, sticky='we',pady=(10, 0),padx=(55, 10))
hansoku_one_blue.bind('<Button-1>', lambda event: push_hansoku (event,hansoku_one_blue))

hansoku_two_blue = Label(blue_side,width=12, height=6, bg='white', borderwidth = 2, relief="raised")
hansoku_two_blue.grid(row=0, column=1, sticky='we',pady=(10, 0),padx=(10, 10))
hansoku_two_blue.bind('<Button-1>', lambda event: push_hansoku (event,hansoku_two_blue))

hansoku_three_blue = Label(blue_side,width=12, height=6, bg='white', borderwidth = 2, relief="raised")
hansoku_three_blue.grid(row=0, column=2, sticky='we',pady=(10, 0),padx=(10, 10))
hansoku_three_blue.bind('<Button-1>', lambda event: push_hansoku (event,hansoku_three_blue))

hansoku_four_blue = Label(blue_side,width=12, height=6, bg='white', borderwidth = 2, relief="raised")
hansoku_four_blue.grid(row=0, column=3, sticky='we',pady=(10, 0),padx=(10, 10))
hansoku_four_blue.bind('<Button-1>', lambda event: push_hansoku (event,hansoku_four_blue))


# hansoku white side

white_side = Frame(root)
white_side.grid(row=4, column=5, sticky='we',columnspan=3,padx=(20, 20))

hansoku_one_white = Label(white_side,width=12, height=6, bg='white', borderwidth = 2, relief="raised")
hansoku_one_white.grid(row=0, column=0, sticky='we',pady=(10, 0),padx=(30, 10))
hansoku_one_white.bind('<Button-1>', lambda event: push_hansoku_white (event,hansoku_one_white))

hansoku_two_white = Label(white_side,width=12, height=6, bg='white', borderwidth = 2, relief="raised")
hansoku_two_white.grid(row=0, column=1, sticky='we',pady=(10, 0),padx=(10, 10))
hansoku_two_white.bind('<Button-1>', lambda event: push_hansoku_white (event,hansoku_two_white))

hansoku_three_white = Label(white_side,width=12, height=6, bg='white', borderwidth = 2, relief="raised")
hansoku_three_white.grid(row=0, column=2, sticky='we',pady=(10, 0),padx=(10, 10))
hansoku_three_white.bind('<Button-1>', lambda event: push_hansoku_white (event,hansoku_three_white))

hansoku_four_white = Label(white_side,width=12, height=6, bg='white', borderwidth = 2, relief="raised")
hansoku_four_white.grid(row=0, column=3, sticky='we',pady=(10, 0),padx=(10, 10))
hansoku_four_white.bind('<Button-1>', lambda event: push_hansoku_white (event,hansoku_four_white))



def seconds_to_time(seconds):
    minutes = seconds // 60
    seconds -= minutes * 60
    return f'{minutes:02d}:{seconds:02d}'

def update(seconds):
    global after
    if seconds >= 0:
        countdown.set(seconds_to_time(seconds))
        after = root.after(1000, lambda: update(seconds - 1))
    else:
        root.after_cancel(after)


def stop():
    try:
        root.after_cancel(after)
    except NameError:
        pass

def resume():
    seconds = int(countdown.get().split(':')[0]) * 60 + int(countdown.get().split(':')[1])
    update(seconds)

def restart():
    try:
        root.after_cancel(after)
    except NameError:
        pass
    countdown.set(combotime.get())
    hansoku_one_white.config(bg='white')
    hansoku_two_white.config(bg='white')
    hansoku_three_white.config(bg='white')
    hansoku_four_white.config(bg='white')
    hansoku_one_blue.config(bg='white')
    hansoku_two_blue.config(bg='white')
    hansoku_three_blue.config(bg='white')
    hansoku_four_blue.config(bg='white')
    score_white.config(text=0)
    score_blue.config(text=0)
    koka.config(text=0)
    yuko.config(text=0)
    wari.config(text=0)
    wari_blue.config(text=0)
    koka_blue.config(text=0)
    yuko_blue.config(text=0)


def set_time():
    print(combotime.get())

def start():
    try:
        root.after_cancel(after)
    except NameError as e:
        # print(e)
        pass

    seconds = int(combotime.get().split(':')[0]) * 60 + int(combotime.get().split(':')[1])
    update(seconds)





time_frame = Frame(root)
time_frame.grid(row=5, column=3,  sticky=N,columnspan=2, rowspan=2)




countdown = StringVar()
countdown.set("00:00")

time = Label(time_frame,textvariable=countdown, width=6, height=1, borderwidth = 2, relief="raised",font='Times 60')
time.grid(row=0, column=0,columnspan=2,rowspan=1, sticky='we',pady=(0, 0),padx=(40, 40))



combotime = ttk.Combobox(time_frame,
                            values=[
                                    "0:30",
                                    "1:00",
                                    "1:30",
                                    "2:00",
                                    "3:00"],
                            state="readonly", font="Times 18", width=5)

combotime.grid(column=1, row=2,pady=(5,0))
combotime.current(4)
# combotime.config(height=30)

text = Label(time_frame,text='Время раунда:',  font='Times 18')
text.grid(column=0, row=2,padx=(30, 0),pady=(5,0))



btn_frame = Frame(root)
btn_frame.grid(row=5, column=2,columnspan=4,rowspan=2, pady=(60,0))
# btn_frame.pack(side="bottom")


btn_stop = Button(btn_frame,text="Пауза", width=11, height=2, command=stop)
btn_stop.grid(row=0, column=1, sticky='we',pady=(0, 0),padx=(20, 20))

btn_resume = Button(btn_frame,text="Продолжить", width=11, height=2, command=resume)
btn_resume.grid(row=0, column=2, sticky='we',pady=(0, 0),padx=(20, 20))

btn_restart = Button(btn_frame,text="Сбросить все", width=11, height=2, command=restart)
btn_restart.grid(row=0, column=3, sticky='we',pady=(0, 0),padx=(20, 20))

btn_start = Button(btn_frame,text="Старт", width=11, height=2, command=start)
btn_start.grid(row=0, column=4, sticky='we',pady=(0, 0),padx=(20, 20))

frame_quit = Frame(root)
frame_quit.grid(row=6, column=0, sticky='sw',pady=(0, 10),padx=(5, 0),rowspan=2)
btn_quit = Button(frame_quit, text="Выход", command=root.destroy)
btn_quit.grid(row=0, column=0, sticky='we')



root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1,weight=1)
root.grid_columnconfigure(2,weight=1)
root.grid_columnconfigure(3,weight=1)
root.grid_columnconfigure(4,weight=1)
root.grid_columnconfigure(5,weight=1)
root.grid_columnconfigure(6,weight=1)
root.grid_columnconfigure(7,weight=1)
root.grid_columnconfigure(8,weight=1)
root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=1)
root.grid_rowconfigure(2,weight=1)
root.grid_rowconfigure(3,weight=1)
root.grid_rowconfigure(4,weight=1)
root.grid_rowconfigure(5,weight=1)
root.grid_rowconfigure(6,weight=1)
root.grid_rowconfigure(7,weight=1)

Grid.grid_rowconfigure(btn_frame,0,weight=1)
Grid.grid_columnconfigure(btn_frame,0,weight=1)
Grid.grid_columnconfigure(btn_frame,1,weight=1)
Grid.grid_columnconfigure(btn_frame,2,weight=1)
Grid.grid_columnconfigure(btn_frame,3,weight=1)


root.mainloop()
