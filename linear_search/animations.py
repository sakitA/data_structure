import random
from os.path import dirname, abspath

from manim import *

import sys

sys.path.insert(0, dirname(dirname(abspath(__file__))) + '/')

from utilities.cfg import BASE_COLOR_DICT
from utilities.code_snippet import CodeSnippet

interface_dict_1 = {
    **BASE_COLOR_DICT,
    "add": YELLOW,
    "get": YELLOW,
    "set": YELLOW,
    "size": YELLOW,
    "remove": YELLOW,
    "is_empty": YELLOW,
    "iterator": YELLOW,
    "NotImplementedError": BLUE_B,
}

config.background_color = "#14074a"
config.frame_width = 64
config.frame_height = 36

NUMBERS = [4, 8, 15, 17, 23, 42]
FOUND_SCENARIO = 17
NOT_FOUND_SCENARIO = 45
KOD = FOUND_SCENARIO if bool(random.getrandbits(1)) else NOT_FOUND_SCENARIO


class LinearSearchScene(Scene):
    def construct(self):
        self.wait(0.5)

        code_snippet = self.build_code_snippet()

        separator = Line((0, -17, 0), (0, 17, 0))
        self.add(separator)

        for i in range(len(code_snippet.header.images)):
            code_snippet.header.images[i].move_to(code_snippet.header.files[i][0].get_left() + 0.5 * RIGHT)

        self.wait(1)

        ############################################ Animations ########################################################
        self.animate_header(code_snippet)

        kod = self.animate_kod(separator)

        mektublar = self.animate_mektublar(kod)

        num_group = self.animate_number_block(NUMBERS, mektublar)

        self.animate_code_block(code_snippet, 0, 0, 1, 0.5)
        self.animate_code_block(code_snippet, 0, 1, 3, 0.5)
        self.animate_code_block(code_snippet, 0, 3, 4, 0.5)

        index = 0
        pre_box = None
        found = False

        self.animate_code_block(code_snippet, 0, 4, 5, 0.5)
        self.animate_code_block(code_snippet, 0, 5, 6, 0.5)
        code_arrow = self.animate_index_arrow(LEFT, RIGHT, None, (-28.2, 9.6, 0))
        box_arrow = self.animate_index_arrow(DOWN, UP, None, num_group[0])

        while index < len(NUMBERS):
            found = NUMBERS[index] == KOD

            code_arrow = self.animate_index_arrow(LEFT, RIGHT, code_arrow, DOWN)
            self.change_box_color(pre_box, num_group[index])

            self.animate_condition(KOD, NUMBERS[index], index, found)

            if found:
                break
            else:
                code_arrow = self.animate_index_arrow(LEFT, RIGHT, code_arrow, 2 * DOWN)
                pre_box = num_group[index]
                box_arrow = self.animate_index_arrow(DOWN, UP, box_arrow, 4 * RIGHT)
                code_arrow = self.animate_index_arrow(LEFT, RIGHT, code_arrow, 3 * UP, 1.0)
                index = index + 1

        if found:
            self.animate_index_arrow(LEFT, RIGHT, code_arrow, DOWN)
        else:
            self.change_box_color(pre_box, None)
            self.animate_index_arrow(LEFT, RIGHT, code_arrow, 5 * DOWN)
        self.wait(1.0)

        self.play(FadeOut(*self.mobjects))
        self.animate_result(found, index)

    def animate_number_block(self, numbers, relative_object):
        numbers_group = Group()
        for number in range(len(numbers)):
            box = Square(
                side_length=3,
                color=YELLOW,
                stroke_width=10
            ).next_to(relative_object, direction=RIGHT, buff=0.5) \
                .shift((number * 4) * RIGHT)

            number_object = Text(
                str(numbers[number]),
                font="Ubuntu",
                font_size=96,
                color=YELLOW
            ).move_to(box.get_center())

            index = Text(
                str(number),
                font="Ubuntu",
                font_size=80,
                color=WHITE
            )
            index.move_to(box.get_bottom() - [0, index.height / 2 + 0.5, 0])

            number_g = Group()
            number_g.add(box, number_object, index)
            numbers_group.add(number_g)
        for ng in numbers_group:
            self.play(FadeIn(ng), rate_func=linear, run_time=0.5)
        self.wait(0.5)

        return numbers_group

    def animate_mektublar(self, relative_object):
        mektublar = Text(
            str("Məktublar:"),
            font="Ubuntu",
            font_size=96,
            color=WHITE
        ).move_to(relative_object.get_bottom() + (1, -3, 0))
        self.play(FadeIn(mektublar), run_time=0.5)
        return mektublar

    def animate_header(self, code_snippet):
        self.add(code_snippet.object)
        self.play(
            *[ob.animate.set_opacity(1) for ob in code_snippet.header.files[0]],
            *[FadeIn(ob) for ob in code_snippet.header.images[0]]
        )

    def build_code_snippet(self):
        file_names = ["linear_search"]

        scrollbar_rolls = [None, 3, None, None, None]

        f1_code_groups_raw = [
            [
                ["def linear_search(mektublar, kod):", 1, 1],
            ],
            [
                ["say = len(mektublar)", 2, 2],
            ],
            [
                ["# {}".format(len(NUMBERS)), 2, 12.5],
            ],
            [
                ["indeks = 0", 4, 2],
            ],
            [
                ["while indeks < say:", 6, 2],
                ["if mektublar[indeks] == kod:", 7, 3],
                ["return indeks + 1", 8, 4],
                ["indeks += 1", 9, 3],
            ],
            [
                ["return \"Məktub yoxdur\"", 11, 2],
            ],
        ]

        f1_color_dicts = [interface_dict_1, interface_dict_1, interface_dict_1,
                          interface_dict_1, interface_dict_1, interface_dict_1]

        code_groups_raw = [f1_code_groups_raw]
        color_dicts = [f1_color_dicts]

        code_snippet = CodeSnippet(
            file_names=file_names,
            extension="py",
            code_groups_raw=code_groups_raw,
            color_dicts=color_dicts,
            shift=[16, 0, 0, 16],
            scrollbar_rolls=scrollbar_rolls
        )

        return code_snippet

    def animate_kod(self, relative_object):
        kod = Text(
            str("Kod: {}".format(KOD)),
            font="Ubuntu",
            font_size=96,
            color=WHITE
        ).next_to(relative_object) \
            .move_to(relative_object.get_top() + [3, -1, 0])
        self.play(FadeIn(kod), run_time=0.5)
        return kod

    def animate_code_block(self, code_snippet, code_block_index, start_inc, end_exc, duration):
        code_block = code_snippet.body.code_groups[code_block_index]

        self.play(
            *[line.object.animate.set_opacity(1) for group in code_block[start_inc:end_exc]
              for line in group.lines],
            run_time=1
        )
        self.wait(duration)

    def animate_index(self, relative_object):
        indeks = Text(
            str("İndeks"),
            font="Ubuntu",
            font_size=72,
            color=YELLOW
        ).move_to(relative_object.get_bottom() + (-1.2, -3, 0))

        self.play(FadeIn(indeks), run_time=0.5)

    def animate_index_arrow(self, arr_start, arr_end, arrow, position, duration=0.5):
        if arrow:
            arrow.shift(position)
        else:
            arrow = Arrow(start=arr_start,
                          end=arr_end,
                          color=YELLOW,
                          stroke_width=128) \
                .next_to(position, direction=DOWN)

        self.play(FadeIn(arrow), run_time=duration)

        return arrow

    def animate_condition(self, kod, value, index, match):
        is_match = "=" if match else "≠"
        condition_text = "Məktublar[{}] == vətəndaşın_kodu ?".format(index)
        equal_text = "{} {} {}".format(value, is_match, kod)

        condition_text_obj = Text(
            str(condition_text),
            font="Ubuntu",
            font_size=96,
            color=YELLOW
        ).center().shift(15 * RIGHT)

        equal_text_obj = Text(
            str(equal_text),
            font="Ubuntu",
            font_size=96,
            color=YELLOW
        ).next_to(condition_text_obj, DOWN, buff=0.5)

        self.play(FadeIn(condition_text_obj), run_time=1.0)
        self.play(FadeIn(equal_text_obj), run_time=1.0)

        self.wait(0.5)
        txt_grp = Group()
        txt_grp.add(condition_text_obj, equal_text_obj)
        self.play(FadeOut(txt_grp), run_time=0.5)

    def change_box_color(self, pre_box: Group, cur_box: Group):
        if pre_box:
            self.play(pre_box.animate.set_color(YELLOW), run_time=0.5)
        if cur_box:
            self.play(cur_box.animate.set_color(RED), run_time=0.5)

    def animate_result(self, found, index):
        result = "Yeni məktub {} cü sıradadır.".format(index+1) \
            if found else "Yeni məktub yoxdur."
        text = Text(
            str(result),
            font="Ubuntu",
            font_size=96,
            color=GREEN if found else RED
        ).center()
        self.play(FadeIn(text), run_time=1.0)
