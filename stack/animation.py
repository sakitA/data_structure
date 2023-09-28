from manim import *

from os.path import dirname
from os.path import abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))) + '/')

from utilities.logo import Logo
from utilities.animations import DrawBoxThenWrite

config.background_color = "#14074a"
config.frame_width = 128
config.frame_height = 64


class Stack(Scene):
    def __init__(self):
        super().__init__()

    def construct(self):
        self.opening()
        self.intro_to_concept()
        #self.history()
        #self.practical_application()
        #self.technical_explanation()
        #self.conclusion()

    def opening(self):
        Logo(self)

        stack_svg = SVGMobject("assets/stack.svg").scale(5)
        text = Text("Stack", font="Arial", font_size=96, color=WHITE).scale(6).next_to(stack_svg, DOWN)

        self.play(Create(stack_svg), stack_svg.animate.shift(2 * UP), Write(text), run_time=1)
        self.wait(1)
        self.play(*[FadeOut(shape) for shape in self.mobjects])

    def intro_to_concept(self):
        chalkboard = SVGMobject("assets/EmptyChalkboard.svg")
        self.add(chalkboard.scale(25))
        #self.play(DrawBoxThenWrite("The stack is a linear data structure that serves as a collection of elements, "
        #                           "with two main principal operations. It is an ordered list of similar data types "
        #                          "and follows the Last-In-First-Out (LIFO) principle. It means the item that goes "
        #                           "in last is that comes out.", location=30 * UP))
        self.wait(1)

    def history(self):
        self.play(DrawBoxThenWrite("The concept of the stack traces its roots to the early works of British computer "
                                   "scientist Alan Turing in the 1930s, whose foundational ideas on data processing laid "
                                   "the groundwork for stack-like structures. The term \"stack\" and its formalization in "
                                   "computing were later championed by Donald Knuth in his influential series, \"The Art "
                                   "of Computer Programming.\" Originally developed to manage subroutine calls in "
                                   "programming, especially recursion, stacks became crucial with the advent of high-level "
                                   "programming languages like FORTRAN and Algol. Over the decades, as computer architectures "
                                   "evolved, the implementation and importance of stacks grew, becoming an integral part of "
                                   "modern computing, from function calls to software features like \"Undo.\"",
                                   location=self.mobjects[1].get_bottom() + 5 * DOWN))
        self.wait(1)

    def practical_application(self):
        len = self.mobjects.__len__()
        self.play(DrawBoxThenWrite("Imagine working at a post office where you're in charge of placing packages into "
                                   "a delivery box for couriers to pick up. As each package arrives, it's added to the box, "
                                   "resembling the “push” operation in a stack. However, the box has a limited capacity. "
                                   "Once it's full, no more packages can be added until some are removed. When the courier "
                                   "arrives, they take the first package from the top – this represents the “pop” operation "
                                   "in a stack. The latest package added becomes the first to be taken out, demonstrating the "
                                   "Last-In-First-Out (LIFO) principle that's at the heart of stacks.",
                                   location=self.mobjects[len - 1].get_bottom() + 5 * DOWN))
        self.wait(1)

    def technical_explanation(self):
        pass

    def conclusion(self):
        pass


class Demo(Scene):
    def construct(self):
        logo = Logo(self)
