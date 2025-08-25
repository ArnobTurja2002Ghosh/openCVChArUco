import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
g=[os.path.join(path, name) for path, subdirs, files in os.walk('global') for name in files if name.startswith('diff_')]
a=[os.path.join(path, name) for path, subdirs, files in os.walk('adaptive') for name in files if name.startswith('diff_')]

x = np.arange(min(len(a),len(g)))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for i,j in zip(g, a):
    img= np.sum(cv2.imread(i)==255)
    img2= np.sum(cv2.imread(j)==255)
    print(img, img2)

    offset = width * multiplier
    rects = ax.bar([multiplier, multiplier+width], [img, img2], width)
    ax.bar_label(rects, padding=3)
    multiplier += 1

plt.show()