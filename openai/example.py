from manim import *

class PostOffice(Scene):
    def construct(self):
        # Draw the post office building
        building = Rectangle(width=4, height=3, color=BLUE, fill_opacity=0.5)
        building.to_edge(LEFT)

        # Draw the post office sign
        sign = Text("Post Office", color=WHITE).scale(1.2)
        sign.next_to(building, UP, buff=0.2)

        # Draw the pkg_queue
        queue = VGroup()
        for i in range(5):
            person = Circle(radius=0.3, color=YELLOW, fill_opacity=1)
            person.next_to(queue, RIGHT, buff=0.2)
            queue.add(person)

        queue.next_to(building, RIGHT, buff=0.5)

        # Add everything to the scene
        self.add(building, sign, queue)
        self.wait()
