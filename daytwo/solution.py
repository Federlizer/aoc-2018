import sys

data = open("./input.txt", "r")

box_ids = data.read().split("\n")
data.close()

def spit(arr):
    for i in arr:
        for j in arr:
            if i == j:
                continue
            yield (i, j)

contestents = []

for v in spit(box_ids):
    strikes = 1
    for i in range(len(v[0])):
        if v[0][i] != v[1][i]:
            strikes -= 1
    if strikes == 0:
        for i in range(len(v[0])):
            if v[0][i] == v[1][i]:
                print(v[0][i], end="")
        sys.exit(0)