from manim import *

class Logo:
    def __init__(self, scene):
        text_o = Text("Ö", font="Arial", font_size=496, color=YELLOW)
        text_bottom = Text("YRƏN.", font="Arial", font_size=224, color=WHITE) \
            .next_to(text_o, direction=RIGHT, aligned_edge=DOWN)
        text_top = Text("ZÜN", font="Arial", font_size=224, color=WHITE) \
            .next_to(text_bottom, direction=UP, aligned_edge=LEFT)

        green_shape = get_top_left_shape()
        bluee_shape = get_top_right_shape().next_to(green_shape, direction=RIGHT)
        grey_shape = get_bottom_left_shape().next_to(green_shape, direction=DOWN)
        yellow_shape = get_bottom_right_shape().next_to(grey_shape, direction=RIGHT)

        group_shapes = VGroup(green_shape, bluee_shape, grey_shape, yellow_shape).scale(0.1)

        text_group = VGroup(text_o, text_top, text_bottom).next_to(group_shapes, direction=RIGHT)

        _ = VGroup(group_shapes, text_group).move_to(ORIGIN)

        animations = [Create(green_shape, run_time=1),
                      Create(bluee_shape, run_time=1),
                      Create(grey_shape, run_time=1),
                      Create(yellow_shape, run_time=1),
                      AddTextWordByWord(text_group)]

        scene.play(*animations, run_time=1)
        scene.wait(0.5)
        scene.play(*[shape.animate.set_opacity(0.25) for shape in _])


def create_shape(control_points, fill_color):
    ln1 = Line(control_points[0], control_points[1])
    cb1 = CubicBezier(control_points[1], control_points[2], control_points[3], control_points[4])
    cb2 = CubicBezier(control_points[4], control_points[5], control_points[6], control_points[7])
    cb3 = CubicBezier(control_points[7], control_points[8], control_points[9], control_points[10])
    ln2 = Line(control_points[10], control_points[11])

    shape = VGroup(ln1, cb1, cb2, cb3, ln2).move_to(ORIGIN)

    combined_shape = VMobject()
    for mob in shape:
        combined_shape.append_vectorized_mobject(mob)

    # Set fill and stroke for the combined shape
    combined_shape.set_fill(fill_color, opacity=1.0)
    combined_shape.set_stroke(BLACK, width=3)

    return combined_shape


def get_left_shape(control_points, fill_color):
    return create_shape(control_points, fill_color)


def get_right_shape(control_points, fill_color):
    # Mirror the control points horizontally about x = 28.5
    mirrored_points = [[57 - pt[0], pt[1], pt[2]] for pt in control_points]
    return create_shape(mirrored_points, fill_color)


# Top Left Shape Control Points
top_left_points = [
    np.array([28.5, 4, 0]),
    np.array([28.5, 18.25, 0]),
    np.array([28.5, 26.1201, 0]),
    np.array([34.8799, 32.5, 0]),
    np.array([42.75, 32.5, 0]),
    np.array([50.6201, 32.5, 0]),
    np.array([57, 26.1201, 0]),
    np.array([57, 18.25, 0]),
    np.array([57, 10.3799, 0]),
    np.array([50.6201, 4, 0]),
    np.array([42.75, 4, 0]),
    np.array([28.5, 4, 0])
]


def get_top_left_shape():
    return get_left_shape(top_left_points, "#00CB8D")


def get_top_right_shape():
    return get_right_shape(top_left_points, "#1F4CED")


# Bottom Left Shape Control Points (essentially the top but shifted down by 28.5)
bottom_left_points = [np.array([pt[0], pt[1] + 28.5, pt[2]]) for pt in top_left_points]


def get_bottom_left_shape():
    return get_left_shape(bottom_left_points, "#C9C9C9")


def get_bottom_right_shape():
    return get_right_shape(bottom_left_points, "#FFCF24")