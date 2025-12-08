from collections import defaultdict
from copy import deepcopy

with open("input", "r") as f:
    manifold = [list(ln) for ln in f.read().splitlines()]

start = (0, manifold[0].index("S"))
bottom = len(manifold)

beams = {start, }

splits = 0
for i in range(bottom - 1):
    new_beams = set()
    for beam in beams:
        if manifold[beam[0] + 1][beam[1]] == "^":
            new_beams.add((beam[0] + 1, beam[1] - 1))
            new_beams.add((beam[0] + 1, beam[1] + 1))
            splits += 1
        else:
            new_beams.add((beam[0] + 1, beam[1]))
    beams = new_beams

beams_p2 = defaultdict(int)
beams_p2[start] = 1
timelines = 1
for i in range(bottom - 1):
    new_beams = defaultdict(int)
    for beam in beams_p2.keys():
        if manifold[beam[0] + 1][beam[1]] == "^":
            new_beams[(beam[0] + 1, beam[1] - 1)] += beams_p2[beam]
            new_beams[(beam[0] + 1, beam[1] + 1)] += beams_p2[beam]
            timelines += beams_p2[beam]
        else:
            new_beams[(beam[0] + 1, beam[1])] += beams_p2[beam]
    beams_p2 = deepcopy(new_beams)

print("P1:", splits)
print("P2:", timelines)