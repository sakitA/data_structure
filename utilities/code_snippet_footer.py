from manim import *
from .cfg import *


class CodeSnippetFooter:
    def __init__(self):
        self.object = self.construct()

    @staticmethod
    def construct():
        rounded_footer = RoundedRectangle(
            corner_radius=0.3,
            width=WIDTH,
            height=0.5
        )
        rounded_footer.set_stroke(COLOR_BODY)
        rounded_footer.set_fill(color=COLOR_BODY, opacity=1)

        return rounded_footer
