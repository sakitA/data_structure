from manim import *


class DrawBoxThenWrite(AnimationGroup):
    """Draw the border first and then write the text inside.

    Examples
    --------
    .. manim:: DrawBoxThenWriteExample

        class Demo(Scene):
            def construct(self):
                self.play(DrawBoxThenWrite("Test", location=UP))
        self.wait(1)
    """

    def __init__(
            self,
            text: str = None,
            location: np.ndarray = UP,
            box_config: dict = {},
            text_config: dict = {},
            run_time: float = 2,
            **kwargs,
    ) -> None:
        text_width = text_config.get("width", 32.5)
        text_font = text_config.get("font", "Arial")
        text_font_size = text_config.get("font_size", 96)
        text_color = text_config.get("color", WHITE)
        text_scale = text_config.get("scale", 1.5)

        text = Text(text, width=text_width, font=text_font,
                    font_size=text_font_size, color=text_color).scale(text_scale)

        width = box_config.get("width", text.get_width() + 1)
        height = box_config.get("height", text.get_height() + 1)
        fill_opacity = box_config.get("fill_opacity", 0.6)
        fill_color = box_config.get("fill_color", LIGHT_GREY)
        stroke_width = box_config.get("stroke_width", 5)
        stroke_color = box_config.get("stroke_color", WHITE)

        box = RoundedRectangle(width=width, height=height,
                               fill_opacity=fill_opacity, fill_color=fill_color,
                               stroke_width=stroke_width, stroke_color=stroke_color)

        box.move_to(location)


        text.move_to(box.get_center())

        box_anim = DrawBorderThenFill(box)
        text_anim = Write(text)

        super().__init__(box_anim, text_anim,
                         run_time=run_time,
                         lag_ratio=0.8,
                         **kwargs)
