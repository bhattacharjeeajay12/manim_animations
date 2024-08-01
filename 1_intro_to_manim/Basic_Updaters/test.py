from manim import *
import os
from pathlib import Path

FLAGS = f"-pqm"
SCENE = "Solution"
flush_cache = "--flush_cache"


class Solution(Scene):
    def construct(self):
        # Initialize slope (m) and y-intercept (c)
        self.m = 1
        self.c = 1

        # Create axes
        axes = Axes(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            axis_config={"color": BLUE}
        )

        # Function to create the line
        def get_line():
            return Line(
                start=axes.c2p(-10, self.m * -10 + self.c),
                end=axes.c2p(10, self.m * 10 + self.c),
                color=YELLOW
            )

        # Create the initial line
        line = get_line()

        # Updater function to update the line based on self.m and self.c
        def update_line(mob):
            mob.become(get_line())

        # Add updater to the line
        line.add_updater(update_line)

        # Add axes and line to the scene
        self.add(axes, line)
        self.wait(1)

        # Example of updating the slope and y-intercept
        self.m = 2
        self.c = -3
        self.wait(1)

        # Another update example
        self.m = -1
        self.c = 2
        self.wait(1)

        # Removing the updater when done
        # line.remove_updater(update_line)


# To render this scene, run the following command in your terminal:
# manim -pql script_name.py DynamicLine

if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS} {flush_cache}")
