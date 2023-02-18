from manim import *
from .cfg import *
import os


class CodeSnippetHeader:
    logo_extension_map = {
        "py": "utilities/assets/lang_icons/icon_py.png",
        "js": "utilities/assets/lang_icons/icon_js.png",
        "cs": "utilities/assets/lang_icons/icon_cs.png",
        "java": "utilities/assets/lang_icons/icon_java.png",
        "php": "utilities/assets/lang_icons/icon_php.png",
    }

    def __init__(self, file_names, extension):
        self.file_names = file_names
        self.extension = extension
        self.files = []
        self.images = []
        self.object = self.construct()

    def construct(self):
        header_box = self.create_header_box()
        circle_group = self.create_circles()
        self.files = self.create_file_boxes()

        circle_group.move_to(header_box.get_left() + 1.4 * RIGHT)
        # file_group.next_to(circle_group, 2 * RIGHT)
        for i in range(len(self.files)):
            if i == 0:
                self.files[i].next_to(circle_group, buff=0.25)
            elif i == 1:
                self.files[i].next_to(self.files[0], buff=0.25)
            else:
                self.files[i].next_to(self.files[1], buff=0.25)

        header = Group()
        header.add(header_box, circle_group)
        for file in self.files:
            header.add(file)

        return header

    @staticmethod
    def create_circles():
        red_circle = Circle(radius=0.2, color=RED, fill_opacity=1)
        yellow_circle = Circle(radius=0.2, color=YELLOW, fill_opacity=1).next_to(red_circle, buff=0.25)
        green_circle = Circle(radius=0.2, color=GREEN, fill_opacity=1).next_to(yellow_circle, buff=0.25)

        circle_group = Group()
        circle_group.add(red_circle, yellow_circle, green_circle)

        return circle_group

    def create_file_boxes(self):
        files = []
        for i in range(len(self.file_names)):
            file_group = Group()
            file_name_box = Rectangle(
                width=7,
                height=1.3,
                fill_opacity=0,
                stroke_opacity=0
            )
            file_name_box_header = RoundedRectangle(
                corner_radius=0.2,
                width=7,
                height=0.3,
                stroke_opacity=0,
                fill_opacity=0
            ).next_to(file_name_box, 0.2 * UP, buff=-1)
            file_name_box_header.set_stroke(COLOR_BODY)
            file_name_box_header.set_fill(color=COLOR_BODY, opacity=0)

            py_logo = ImageMobject(self.logo_extension_map[self.extension])
            # py_logo.set_opacity(0)
            py_logo.move_to(file_name_box.get_left() + 0.5 * RIGHT).scale(0.5)

            file_name = Text(f"{self.file_names[i]}.{self.extension}", font_size=44, font="Ubuntu", fill_opacity=0).next_to(py_logo)
            file_name_box.set_stroke(COLOR_BODY)
            file_name_box.set_fill(color=COLOR_BODY, opacity=0)

            # py_logo = ImageMobject(self.logo_extension_map[self.extension])
            # py_logo.next_to(file_name, 0.01 * LEFT, buff=0.0).scale(0.5)

            file_group.add(file_name_box, file_name, file_name_box_header)
            self.images.append(py_logo)

            files.append(file_group)

        return files

    @staticmethod
    def create_header_box():
        header = Rectangle(
            width=WIDTH,
            height=1.5
        )

        header.set_stroke(COLOR_HEADER)
        header.set_fill(color=COLOR_HEADER, opacity=1)
        # header.shift(
        #     16 * LEFT,
        #     16 * UP
        # )

        rounded_header = RoundedRectangle(
            corner_radius=0.3,
            width=WIDTH,
            height=0.5
        ).next_to(header, 0.2 * UP, buff=-1)
        rounded_header.set_stroke(COLOR_HEADER)
        rounded_header.set_fill(color=COLOR_HEADER, opacity=1)

        header_group = Group()
        header_group.add(header, rounded_header)

        return header_group