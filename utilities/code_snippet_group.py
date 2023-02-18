from manim import *
from .code_snippet_line import CodeSnippetLine


class CodeSnippetGroup:
    def __init__(self, lines_raw, color_dict, left, top):
        self.lines_raw = lines_raw
        self.color_dict = color_dict
        self.left = left
        self.top = top
        self.lines = []
        self.object = self.construct()
        self.highlight = self.create_highlight()

    def construct(self):

        group = Group()
        for code, line, indent in self.lines_raw:
            line_c = CodeSnippetLine(code, line, indent, self.left, self.top, self.color_dict)
            self.lines.append(line_c)
            group.add(line_c.object)
            group.add(line_c.highlight)

        return group

    def create_highlight(self):

        max_right = [len(line.code) for line in self.lines].index(max([len(line.code) for line in self.lines]))

        highlight = Polygram(
            [
                [self.lines[0].object.get_left()[0] - 0.1, self.lines[0].object.get_top()[1] + 0.1, 0],
                [self.lines[0].object.get_left()[0] - 0.1, self.lines[len(self.lines)-1].object.get_bottom()[1] - 0.1, 0],
                [self.lines[max_right].object.get_right()[0] + 0.1, self.lines[len(self.lines)-1].object.get_bottom()[1] - 0.1, 0],
                [self.lines[max_right].object.get_right()[0] + 0.1, self.lines[0].object.get_top()[1] + 0.1, 0]
            ],
            color=YELLOW_C,
            stroke_opacity=0
        )

        return highlight
