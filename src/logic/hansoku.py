from tkinter import Label

RED_COLOR = 'red'
WHITE_COLOR = 'white'

class HansokyMouseClick:
    def __init__(self):
        self.counter = 0

    def left_click(self, button_to_click: Label, opposite_side_main_score: Label) -> None:
        self._change_color(button_to_click)
        self.counter +=1
        print(self.counter)


    def _change_color(self,button:Label) -> None:
        if self.__get_button_color(button) == RED_COLOR:
            self._set_white_color(button)
        else:
            self._set_red_color(button)


    def _set_red_color(self,button:Label) -> None:
        button.config(bg=RED_COLOR)

    def _set_white_color(self,button:Label) -> None:
        button.config(bg=WHITE_COLOR)

    def __is_red_button(self,button:Label) -> bool:
        return self.__get_button_color(button) == RED_COLOR

    def __get_button_color(self,button:Label) -> str:
        return button.cget("bg")