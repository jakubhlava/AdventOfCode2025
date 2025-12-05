with open('input', 'r') as f:
    cmds = f.read().splitlines()

dial = 50
nulls = 0
p2_nulls = 0
for cmd in cmds:
    amnt = int(cmd[1:])
    if cmd[0] == "L":
        for_params = amnt, 0, -1
    else:
        for_params = 0, amnt, 1
    direction = for_params[-1]
    for _ in range(*for_params):
        if dial == 0 and direction == -1:
            dial = 99
        elif dial == 99 and direction == 1:
            dial = 0
        else:
            dial += direction
        if dial == 0:
            p2_nulls += 1

    if dial == 0:
        nulls += 1

print("P1:", nulls)
print("P2:", p2_nulls)