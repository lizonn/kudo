from enum import Enum
from tkinter import Label


class MarkType(Enum):
    KOKA = 1
    YUKO = 2
    WARI = 4


class SideType(Enum):
    BLUE = 'Синий'
    WHITE = 'Белый'


class MouseClick:

    def left_click(self, name_button: MarkType, button_to_click: Label, side_main_score: Label) -> None:

        self._add_mark_to_main_score(name_button, side_main_score, is_left_click=True)
        self._add_mark_to_current_button(button_to_click)

    def right_click(self, name_button: MarkType, button_to_click: Label, side_main_score: Label) -> None:
        if self.__check_old_score(side_main_score, name_button.value) and self.__check_button_to_click(button_to_click):
            self._add_mark_to_main_score(name_button, side_main_score, is_left_click=False)
            self._subtract_mark_to_current_button(button_to_click)

    def _add_mark_to_main_score(self, name_button: MarkType, side_main_score: Label, is_left_click: bool = True):
        if is_left_click:
            self.__refresh_score_add(side_main_score, name_button.value)

        else:
            self.__refresh_score_subtract(side_main_score, name_button.value)

    def _add_mark_to_current_button(self, button_to_click: Label) -> None:
        old_score = self.__get_old_score(button_to_click)
        button_to_click.config(text=old_score + 1)

    def _subtract_mark_to_current_button(self, button_to_click: Label) -> None:
        current_old_score = self.__get_old_score(button_to_click)
        if (current_old_score > 0):
            button_to_click.config(text=current_old_score - 1)

    def __get_old_score(self, score: Label) -> int:
        return int(score.cget("text"))

    def __refresh_score_add(self, side_main_score: Label, new_mark: int) -> None:
        old_score = self.__get_old_score(side_main_score)
        side_main_score.config(text=old_score + new_mark)

    def __refresh_score_subtract(self, side_main_score: Label, new_mark: int) -> None:
        old_score = self.__get_old_score(side_main_score)
        side_main_score.config(text=old_score - new_mark)

    def __check_old_score(self, side_main_score: Label, new_mark: int) -> bool:
        old_score = self.__get_old_score(side_main_score)
        if old_score - new_mark >= 0:
            return True
        else:
            return False

    def __check_button_to_click(self, button_to_click: Label) -> bool:
        current_old_score = self.__get_old_score(button_to_click)
        if (current_old_score > 0):
            return True
        else:
            return False