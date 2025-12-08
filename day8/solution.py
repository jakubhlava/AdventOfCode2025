import math
import operator
from functools import reduce

with open("input", "r") as f:
    coords = [tuple(int(n) for n in ln.split(",")) for ln in f.read().splitlines()]

def get_euclidean_dist(point_a: tuple[int, int, int], point_b: tuple[int, int, int]):
    return math.sqrt((point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2 + (point_a[2] - point_b[2]) ** 2)

def do_step():
    global circuits
    global distances
    global next_shortest
    next_shortest = distances.pop()
    circuit_1 = None
    circuit_2 = None
    for j, circuit in enumerate(circuits):
        if next_shortest[0] in circuit:
            circuit_1 = j
        if next_shortest[1] in circuit:
            circuit_2 = j
    if circuit_1 == circuit_2:
        return
    to_remove = max(circuit_1, circuit_2)
    to_keep = min(circuit_1, circuit_2)

    circuits[to_keep].extend(circuits[to_remove])
    circuits.pop(to_remove)

distances_tmp = dict()

next_shortest = None

for pa in coords:
    for pb in coords:
        if pa == pb:
            continue
        dist = get_euclidean_dist(pa, pb)
        if (pa, pb) and (pb, pa) not in distances_tmp.keys():
            distances_tmp[(pa, pb)] = dist

distances = list(sorted([(pa, pb, dist) for (pa, pb), dist in distances_tmp.items()], key=lambda x: x[2], reverse=True))

circuits = [[coord] for coord in coords]
for i in range(1000):
    do_step()

lengths = sorted(tuple(len(circuit) for circuit in circuits), reverse=True)

print("P1:", reduce(operator.mul, lengths[:3]))

while len(circuits) > 1:
    do_step()

print("P2:", next_shortest[0][0] * next_shortest[1][0])

