with open("input", "r") as f:
    fresh, available = f.read().split("\n\n")
    fresh = [[int(x) for x in line.split("-")] for line in fresh.splitlines()]
    available = [int(line) for line in available.splitlines()]

fresh_total = 0
for ingredient in available:
    for start, stop in fresh:
        if start <= ingredient <= stop:
            fresh_total += 1
            break

print("P1:", fresh_total)

fresh = list(sorted(fresh, key=lambda x: x[0])) # to properly handle inner

while True:
    changes = 0
    for i in range(len(fresh)):
        for j in range(i+1, len(fresh)):
            start1, stop1 = fresh[i]
            start2, stop2 = fresh[j]

            if start1 <= start2 <= stop1:
                if stop2 > stop1:
                    stop1 = stop2
            elif start1 <= stop2 <= stop1:
                if start2 < start1:
                    start1 = start2
            else:
                continue

            fresh[i] = [start1, stop1]

            fresh.pop(j)
            changes += 1
            break

    if changes == 0:
        break

counts = [r[1] - r[0] for r in fresh]
result = sum(counts) + len(counts) # both sides are inclusive
print("P2:", result)