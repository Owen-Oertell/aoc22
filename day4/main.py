import os
import sys

# Reat the input file and split it into a list of strings
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    input = f.read().splitlines()
    overlaps = 0
    for i in input:
        w1, w2 = i.split(",")
        x1, y1 = w1.split("-")
        x2, y2 = w2.split("-")
        # check if they overlap at all
        l1 = range(int(x1), int(y1) + 1)
        l2 = range(int(x2), int(y2) + 1)
        if (len(set(l1).intersection(l2)) > 0):
            overlaps += 1
    print(overlaps)