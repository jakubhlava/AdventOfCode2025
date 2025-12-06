import operator
from functools import reduce

with open("input", "r") as f:
    raw_matrix = f.read().splitlines()
    input_matrix = [ln.split() for ln in raw_matrix]

problem_list = [
    [input_matrix[i][j] for i in range(len(input_matrix))] for j in range(len(input_matrix[0]))
]

grand_total = 0
for problem in problem_list:
    numbers = [int(n) for n in problem[:-1]]
    if problem[-1] == "+":
        op = operator.add
    else:
        op = operator.mul

    result = reduce(op, numbers)
    grand_total += result

print("P1:", grand_total)

# P2
max_w = max([len(ln) for ln in raw_matrix])
for i in range(len(raw_matrix)):
    raw_matrix[i] = str.ljust(raw_matrix[i], max_w + 1)

problem_widths = []
current_width = 0
for char in raw_matrix[-1]:
    if current_width == 0: # start
        current_width += 1
        continue
    match char:
        case " ":
            current_width += 1
        case "+" | "*":
            problem_widths.append(current_width)
            current_width = 1
problem_widths.append(len(raw_matrix[-1]) - sum(problem_widths))

offset = 0
total_p2 = 0
for width in problem_widths:
    submatrix = []
    for i in range(len(raw_matrix) - 1):
        submatrix.append(
            raw_matrix[i][offset:offset+width]
        )
    for i in range(len(submatrix)):
        submatrix[i] = submatrix[i][:-1]
    current_problem = []
    for i in range(len(submatrix[0])):
        num = int("".join([submatrix[j][i] for j in range(len(submatrix))]))
        current_problem.append(num)

    if raw_matrix[-1][offset:offset+width].strip() == "+":
        op = operator.add
    else:
        op = operator.mul

    result = reduce(op, current_problem)
    total_p2 += result
    offset += width

print("P2:", total_p2)