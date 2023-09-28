import gettext

from manim import tempconfig
from stack.animation import Stack


class Tutorial:
    def __init__(self, lecture, locale='en', quality="low_quality", preview=True):
        i18n = gettext.translation("algo", "locales", fallback=False, languages=[locale])

        # Create the "magic" function
        i18n.install()

        with tempconfig({"quality": quality, "preview": preview}):
            scene = self.get_scene(lecture)
            scene.render()

    def get_scene(self, lecture):
        if lecture == "stack":
            return Stack()
        return None


if __name__ == "__main__":
    Tutorial("stack", "en", "low_quality", True)
