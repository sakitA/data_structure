from manim import *

from .code_snippet_header import CodeSnippetHeader
from .code_snippet_body import CodeSnippetBody
from .code_snippet_footer import CodeSnippetFooter


class CodeSnippet:
    header = None
    body = None
    footer = None

    def __init__(self, file_names, extension, code_groups_raw, color_dicts, shift, scrollbar_rolls):
        self.file_names = file_names
        self.extension = extension
        self.code_groups_raw = code_groups_raw
        self.color_dicts = color_dicts
        self.shift = shift
        self.scrollbar_rolls = scrollbar_rolls
        self.object = self.construct()

    def construct(self):
        self.header = CodeSnippetHeader(self.file_names, self.extension)
        self.body = CodeSnippetBody(self.code_groups_raw, self.color_dicts, self.scrollbar_rolls)
        self.footer = CodeSnippetFooter()

        self.body.object.next_to(self.header.object, DOWN, buff=-0.2)
        self.footer.object.next_to(self.body.object, 0.2 * DOWN, buff=-1)

        code_snippet = Group()
        code_snippet.add(
            self.header.object,
            self.footer.object,
            self.body.object
        )
        code_snippet.shift(
            self.shift[3] * LEFT,
            self.shift[0] * UP
        )

        return code_snippet

