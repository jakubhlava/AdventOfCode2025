with open("input", "r") as f:
    ranges = [r.split("-") for r in f.read().split(",")]

invalid_ids_p1 = []
invalid_ids_p2 = []
for start, end in ranges:
    for i in range(int(start), int(end) + 1):
        istring = str(i)
        for j in range(1, len(istring) // 2 + 1):
            if len(istring) % j != 0:
                continue
            if istring[:j] * (len(istring) // j) == istring:
                invalid_ids_p2.append(i)
                break
        if len(istring) % 2 == 1:
            continue
        if istring[:len(istring) // 2] == istring[len(istring) // 2:]:
            invalid_ids_p1.append(i)

print("P1:", sum(invalid_ids_p1))
print("P2:", sum(invalid_ids_p2))