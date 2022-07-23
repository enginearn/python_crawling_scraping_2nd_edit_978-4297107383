#!/usr/bin/env python3

import sys

import japanize_matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use("Agg")
mpl.rcParams["font.sans-serif"] = "hack FN"

image_folder = "graph_images"
ext = ".png"
image_name = input("Enter image name: ") + ext
dpi = 500
graph_title = input("Enter graph title: ")
y = x = [i for i in range(1, 6)]
label_1 = "一次関数"

plt.plot(x, y, "bx-", label=label_1)
# plt.savefig(f"{image_folder}/{image_name}", dpi=dpi)

x = [i for i in range(1, 6)]
y = [i * 5 for i in x]
label_2 = "二次関数"

plt.plot(x, y, "ro--", label=label_2)
plt.title(graph_title)
plt.xlabel("xの値")
plt.ylabel("yの値")
plt.legend(loc="best")
plt.xlim(0, 6)

plt.savefig(f"{image_folder}/{image_name}", dpi=dpi)

for i in mpl.style.available:
    print(i)


if __name__ == '__main__':
    sys.exit(0)
