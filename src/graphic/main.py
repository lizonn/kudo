from tkinter import *
from tkinter import ttk

from white import WhiteSide
from blue import BlueSide

from src.graphic.main_score import MainScore

root = Tk()
# root.wm_state('zoomed')
root.attributes('-fullscreen', 1)
# root.config(bg='#9FD996')



# TODO: переписать размеры
if (root.winfo_screenwidth() >= 1950) or (root.winfo_screenheight() >= 1200):
    root.tk.call('tk', 'scaling', 2)
elif  (root.winfo_screenwidth() >= 1900) or (root.winfo_screenheight() >= 1080):
    root.tk.call('tk', 'scaling', 1.80)
elif (root.winfo_screenwidth() > 1500) or (root.winfo_screenheight() > 800):
    root.tk.call('tk', 'scaling', 1.5)
elif (root.winfo_screenwidth() > 1200) or (root.winfo_screenheight() > 700):
    root.tk.call('tk', 'scaling', 1.25)




main_score = MainScore(root)
r = WhiteSide(root,main_score.white,main_score.blue)
b = BlueSide(root,main_score.white,main_score.blue)

root.mainloop()