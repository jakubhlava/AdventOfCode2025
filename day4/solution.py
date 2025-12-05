with open("input", "r") as f:
    workspace = [list(l) for l in f.read().splitlines()]

def get_neib_8(point: tuple[int, int], max_bounds: tuple[int, int]):
    pts = []
    for off_y in range(-1, 2):
        for off_x in range(-1, 2):
            if not (off_x == 0 and off_y == 0) and (0 <= point[0] + off_y < max_bounds[0]) and (0 <= point[1] + off_x < max_bounds[1]):
                pts.append((point[0] + off_y, point[1] + off_x))
    return pts

def get_accessible_points(space):
    accessible = []
    for y in range(len(space)):
        for x in range(len(space[0])):
            if space[y][x] != "@":
                continue
            neighbors = get_neib_8((y, x), (len(space), len(space[0])))
            neighbor_values = [space[ny][nx] for (ny, nx) in neighbors]
            if neighbor_values.count("@") < 4:
                accessible.append((y, x))
    return accessible

print("P1:", len(get_accessible_points(workspace)))

removable = 0
while True:
    current_accessible = get_accessible_points(workspace)
    accessible_amount = len(current_accessible)
    if accessible_amount == 0:
        break
    removable += accessible_amount
    for pt in current_accessible:
        workspace[pt[0]][pt[1]] = "."

print("P2:", removable)

