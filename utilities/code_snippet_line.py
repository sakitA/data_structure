from manim import *


class CodeSnippetLine:
    def __init__(self, code, line, indent, left, top, color_dict):
        self.code = code
        self.line = line
        self.indent = indent
        self.left = left
        self.top = top
        self.color_dict = color_dict
        self.object = self.construct()
        self.highlight = self.create_highlight()

    def construct(self):
        rendered_code = Text(
            self.code,
            font="Monospace",
            t2c=self.color_dict,
            font_size=50,
            fill_opacity=0
        )
        # print(self.left + rendered_code.width / 2 + self.indent, self.top - self.line - rendered_code.height/2)
        rendered_code.move_to([
            self.left + rendered_code.width / 2 + self.indent,
            self.top - self.line - rendered_code.height/2,
            0
        ])
        # point = Point(location=[self.left + rendered_code.width / 2 + self.indent, self.top - self.line - rendered_code.height/2, 0], color=RED)

        return rendered_code

    def create_highlight(self):
        highlight = Polygram(
            [
                [self.object.get_left()[0] - 0.1, self.object.get_top()[1] + 0.1, 0],
                [self.object.get_left()[0] - 0.1, self.object.get_bottom()[1] - 0.1, 0],
                [self.object.get_right()[0] + 0.1, self.object.get_bottom()[1] - 0.1, 0],
                [self.object.get_right()[0] + 0.1, self.object.get_top()[1] + 0.1, 0]
            ],
            color=YELLOW_C,
            stroke_opacity=0
        )

        return highlight
