from manim import *


class StackAdventure(Scene):
    def construct(self):
        # Scene 1: The Post Office Setting
        post_office = Text("Post Office", font_size=36).move_to(UP * 2)
        alex = Circle().scale(0.2).next_to(post_office, DOWN)
        self.play(Write(post_office), Create(alex))

        # Scene 2: Push Operation - Adding Packages
        package1 = Rectangle(width=1, height=0.5, fill_opacity=1, fill_color=BLUE)
        package1_label = Text("Package 1", font_size=24).next_to(package1, DOWN)
        package2 = package1.copy().next_to(package1, DOWN)
        package2_label = Text("Package 2", font_size=24).next_to(package2, DOWN)
        package3 = package1.copy().next_to(package2, DOWN)
        package3_label = Text("Package 3", font_size=24).next_to(package3, DOWN)
        package_stack = VGroup(package1, package2, package3).arrange(DOWN)
        package_stack.next_to(alex, RIGHT)
        counter = Integer(0).next_to(package_stack, RIGHT)

        self.play(Create(package1), Write(package1_label), run_time=1)
        self.play(Create(package2), Write(package2_label), run_time=1)
        self.play(Create(package3), Write(package3_label), run_time=1)
        self.wait(1)
        self.play(Write(counter), run_time=1)

        # Scene 3: Pop Operation - Removing Packages
        delivery_box = RoundedRectangle(width=2, height=2, fill_opacity=0.5, fill_color=GREEN)
        delivery_box_label = Text("Delivery Box", font_size=24).next_to(delivery_box, UP)
        self.play(Create(delivery_box), Write(delivery_box_label), run_time=1)
        self.wait(1)

        # Simulate pop operation
        popped_package = package_stack[-1].copy()
        popped_package_label = Text("Package 3", font_size=24).next_to(popped_package, DOWN)
        popped_package.move_to(delivery_box)
        popped_package_label.move_to(delivery_box_label)
        self.play(FadeOut(package_stack[-1]), FadeOut(package1_label))
        self.play(Write(popped_package), Write(popped_package_label))
        self.play(FadeOut(counter), run_time=1)

        # Scene 4: Technical Explanation with Code
        code = Code(language="python", code="Python code for stack\n\n# Define a class for a Package\n"
                    "class Package:\n    def __init__(self, name, code, address):\n"
                    "        self.name = name\n        self.code = code\n        self.address = address\n\n"
                    "# Define the main Stack class\n"
                    "class Stack:\n    def __init__(self, capacity):\n"
                    "        self.capacity = capacity\n        self.top = -1\n"
                    "        self.stack = [None]*capacity\n\n"
                    "# Methods for push, pop, isEmpty, isFull, peek, and size\n"
                    "    ...  # (Code continues)")
        code.scale(0.5)
        code.next_to(alex, DOWN)
        self.play(Write(code, run_time=4))
        self.wait(1)

        # Scene 5: Conclusion
        conclusion = Text("And that's how stacks work!", font_size=36).next_to(alex, DOWN)
        self.play(Transform(code, conclusion), run_time=2)
        self.wait(2)

        # Closing Credits
        self.play(FadeOut(code), FadeOut(alex), FadeOut(post_office))
        self.wait(1)
