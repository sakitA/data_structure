from manim import *
from .cfg import *
from .code_snippet_group import CodeSnippetGroup


class CodeSnippetBody:
    def __init__(self, code_groups_raw, color_dicts, scrollbar_rolls=None):
        self.code_groups_raw = code_groups_raw
        self.color_dicts = color_dicts
        self.scrollbar_rolls = scrollbar_rolls
        self.code_groups = []
        self.body_box = None
        self.scrollbar = None
        self.inner_scrollbars = []
        self.object = self.construct()

    def construct(self):
        self.create_body_box()
        self.create_scrollbar()
        self.create_code_groups()
        self.create_inner_scrollbars()

        self.scrollbar.move_to(self.body_box.get_right() - [0.25, -0.1, 0])

        body = Group()
        body.add(self.body_box, self.scrollbar)

        for i in range(len(self.scrollbar_rolls)):
            if self.scrollbar_rolls[i]:
                self.inner_scrollbars[i].move_to(self.scrollbar.get_top() - [0, self.inner_scrollbars[i].height / 2 + 0.25, 0])
                body.add(self.inner_scrollbars[i])

        for file in self.code_groups:
            for code_group in file:
                body.add(code_group.object, code_group.highlight)

        return body

    def create_code_groups(self):
        for i in range(len(self.code_groups_raw)):
            group = []
            for code_group in self.code_groups_raw[i]:
                group.append(
                    CodeSnippetGroup(
                        code_group,
                        self.color_dicts[i][self.code_groups_raw[i].index(code_group)],
                        self.body_box.get_left()[0],
                        self.body_box.get_top()[1]
                    )
                )
            self.code_groups.append(group)

    def create_body_box(self):
        self.body_box = Rectangle(
            width=WIDTH,
            height=HEIGHT
        )

        self.body_box.set_stroke(COLOR_BODY)
        self.body_box.set_fill(color=COLOR_BODY, opacity=1)

    def create_scrollbar(self):
        self.scrollbar = RoundedRectangle(
            corner_radius=0.3,
            width=0.5,
            height=HEIGHT-0.5
        )

        self.scrollbar.set_stroke(COLOR_HEADER)
        self.scrollbar.set_fill(color=COLOR_HEADER, opacity=1)

    def create_inner_scrollbars(self):
        for scrollbar_roll in self.scrollbar_rolls:
            if scrollbar_roll:
                scrollbar = RoundedRectangle(
                    corner_radius=0.2,
                    width=0.38,
                    height=HEIGHT / scrollbar_roll - 0.3
                )
                scrollbar.set_stroke(COLOR_BODY, opacity=0)
                scrollbar.set_fill(color=COLOR_BODY, opacity=0)

                self.inner_scrollbars.append(scrollbar)
            else:
                self.inner_scrollbars.append(None)
