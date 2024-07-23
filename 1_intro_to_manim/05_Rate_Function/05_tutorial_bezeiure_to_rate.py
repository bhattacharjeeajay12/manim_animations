import matplotlib.pyplot as plt
import numpy as np
from manim import *


def simple_cubic_bezier(x1, x2, y1, y2):
    return bezier([
        np.array([0, 0, 0]),
        np.array([x1, y1, 0]),
        np.array([x2, y2, 0]),
        np.array([1, 1, 0]),
    ])


# handles = [0, 1.03, .33, .99]
# handles = [0.29, .34, .78, .38]
# handles = [0, .96, 0, .96]
handles = [1, 0, 1, 0]

parametric_bezier = simple_cubic_bezier(*handles)
print("parametric_bezier : ", parametric_bezier)
T_RANGE = np.arange(0, 1.02, 0.02)

X_VAL = [parametric_bezier(t)[0] for t in T_RANGE]
Y_VAl = [parametric_bezier(t)[1] for t in T_RANGE]

plt.plot(X_VAL, Y_VAl, "g")
plt.show()
