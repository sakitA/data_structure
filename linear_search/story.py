import random
from os.path import dirname, abspath

from manim import *

import sys

sys.path.insert(0, dirname(dirname(abspath(__file__))) + '/')

config.background_color = "#14074a"
config.frame_width = 64
config.frame_height = 36


class Story(Scene):
    def construct(self):
        cloud_group = self.create_cloud_group()
        tree_group = self.create_tree_group()
        fence_group = self.create_fence_group()
        person_group = self.create_person_group()
        tree = SVGMobject("../assets/tree.svg").shift(12 * LEFT, -3 * UP).scale(6)
        post = SVGMobject("../assets/post_office.svg").move_to(tree.get_right() + [15, 0, 0]).scale(7)
        sun = SVGMobject("../assets/sun_solid.svg").set_color(YELLOW).move_to(post.get_center()).scale(2)
        sun.opacity = 0

        group1 = Group(cloud_group, tree_group, fence_group, tree, sun, post)

        self.play(FadeIn(group1), run_time=0.5)

        sun.opacity = 100
        self.play(sun.animate.shift(UP + [-10, 0, 0]), run_time=2)

    def create_cloud_group(self):
        cloud = SVGMobject("../assets/cloud_solid.svg").set_color(WHITE)

        clouds = Group()
        position = 1
        for i in range(7):
            mobj = cloud.copy().shift((-23 + i * 8.5) * LEFT, (14.5 + 1.5 * position) * UP)
            clouds.add(mobj).scale(1.05)
            position = position * -1

        return clouds

    def create_tree_group(self):
        tree = self.create_tree_object()

        trees = Group()
        for i in range(3):
            mobj = tree.copy()
            mobj.shift((20 - i * 20) * LEFT, UP).scale(1.2)
            trees.add(mobj)
        return trees

    def create_fence_group(self):
        fence = SVGMobject("../assets/fence_solid.svg").set_color(WHITE).scale(2.5)

        fences = Group()
        for i in range(14):
            mobj = fence.copy().move_to(DOWN + [-29.9 + i * 4.6, -4.5, 0], DOWN+[0, 0.5, 0])
            fences.add(mobj)

        return fences

    def create_person_group(self):
        persons = Group()
        person1 = SVGMobject(
            "../assets/person.svg"
        ).move_to(DOWN + [0, -2, 0]).scale(5)

        person2 = SVGMobject(
            "../assets/people-old.svg"
        ).move_to(person1.get_right() + [7, 0, 0]).scale(5)

        person3 = SVGMobject(
            "../assets/people_with_dog.svg"
        ).move_to(person2.get_right() + [7, 0, 0]).scale(5)

        persons.add(person1, person2, person3)

        return persons
    def create_tree_object(self):
        tree = SVGMobject("../assets/tree_solid.svg")\
            .set_color(GREEN)\
            .scale(2.5)

        tree_obj = Group()

        tree_left = tree.copy().shift(-5 * RIGHT, -0.6 * UP)
        tree_middle = tree.copy().move_to(tree_left.get_center() + [3, -1.5, 0])
        tree_right = tree.copy().move_to(tree_middle.get_center() + [3, 1.2, 0])

        tree_obj.add(tree_left, tree_right, tree_middle)

        return tree_obj

