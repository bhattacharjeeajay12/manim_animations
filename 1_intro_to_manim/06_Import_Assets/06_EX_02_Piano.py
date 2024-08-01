import numpy as np
from manim import *
import os
from pathlib import Path

FLAGS = f"-pqm"
SCENE = "Solution"
flush_cache = "--flush_cache"
config.background_color = WHITE


class Solution(Scene):
    def get_piano(self):
        piano = []
        white_key = Rectangle(width=1, height=5, fill_opacity=1, fill_color=WHITE, stroke_color=BLACK)
        black_key = Rectangle(width=0.6, height=3, fill_opacity=1, color=BLACK)
        keys = "WBWBWWBWBWBW"  # * 2 for 2 octaves
        notes = "CXDXEFXGXAXB"
        white_keys = []
        black_keys = []

        for i, k in enumerate(keys):
            rec = white_key.copy() if k == "W" else black_key.copy()
            rec.key = keys[i]
            rec.note = notes[i]
            if i >= 1:
                if k == "W":
                    if piano[i - 1].key == "B":
                        rec.next_to(piano[i - 1], buff=-black_key.width / 2, aligned_edge=UP)
                    else:
                        rec.next_to(piano[i - 1], buff=0, aligned_edge=UP)
                else:
                    rec.next_to(piano[i - 1], buff=-black_key.width / 2, aligned_edge=UP)
            piano.append(rec)
            if k == "W":
                white_keys.append(rec)
            else:
                black_keys.append(rec)

        return Group(*white_keys,*black_keys)

    def construct(self):
        piano = self.get_piano()
        piano.move_to(ORIGIN)
        self.add(piano)

        melody_progression1 = "CCGGAAGPFFEEDDC"
        melody_progression2 = "CDECCDECEFGPEFGP"
        for note in melody_progression1:
            if note != "P":
                self.add_sound(f"notes/{note}")
                key_note = list(filter(lambda x: (x.note == note), piano))[0]
                # print("note : ", note)
                # print(list(filter(lambda x: (x.note == note), piano)))
                # print("key_note : ", key_note)

                print("-"*10)
                self.play(FadeToColor(key_note, RED, rate_func=there_and_back, run_time=0.2))
                self.wait(0.3)
            else:
                self.wait(0.5)


if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS} {flush_cache}")
