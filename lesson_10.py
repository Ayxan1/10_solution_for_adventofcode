# Parse the topographic map, ignoring '.'
topographic_map = [
    [int(char) if char.isdigit() else None for char in line]
    for line in open("day10.txt", "r").read().split("\n")
]

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def find_total_hiking_trail(start_info):
    total = 0
    step_r, step_c, hill_height = start_info
    visited = [[False for _ in range(len(topographic_map[0]))] for _ in range(len(topographic_map))]
    visited[step_r][step_c] = True

    queue = [(step_r, step_c, 0, [(step_r, step_c)])]  # Add path tracking to queue
    paths = []  # To store valid paths

    while queue:
        step_r, step_c, hill_height, path = queue.pop(0)

        if hill_height == 9:
            total += 1
            paths.append(path)  # Append the completed path

        for dr, dc in directions:
            nr, nc = step_r + dr, step_c + dc

            # Check bounds and valid path
            if (
                0 <= nr < len(topographic_map)
                and 0 <= nc < len(topographic_map[0])
                # and not visited[nr][nc]
                and topographic_map[nr][nc] is not None  # Ignore impassable areas
                and topographic_map[nr][nc] == hill_height + 1
            ):
                queue.append((nr, nc, topographic_map[nr][nc], path + [(nr, nc)]))
                visited[nr][nc] = True

    return total, paths


# Find total score and all paths
total = 0
all_paths = []

for i in range(len(topographic_map)):
    for j in range(len(topographic_map[0])):
        if topographic_map[i][j] == 0:
            score, paths = find_total_hiking_trail((i, j, topographic_map[i][j]))
            total += score
            all_paths.extend(paths)

print("Total Score:", total)
# print("All Paths:")
# for path in all_paths:
#     print(path)
