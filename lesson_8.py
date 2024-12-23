grid = [list(line) for line in open("day8.txt", "r").read().split("\n")]

antinode_grid = [['.' for _ in range(len(grid[1]))] for _ in range(len(grid[0]))]

def print_grid(grid):
    for row in grid:
        print(row)

def place_antinode(antinode_grid, distance, base_antena_coordinates, found_antena_coordinates):
    direction = tuple()
    if base_antena_coordinates[0] < found_antena_coordinates[0] and base_antena_coordinates[1] > found_antena_coordinates[1]:
        direction = (1, -1)
    if base_antena_coordinates[0] < found_antena_coordinates[0] and base_antena_coordinates[1] == found_antena_coordinates[1]:
        direction = (1, 0)
    if base_antena_coordinates[0] < found_antena_coordinates[0] and base_antena_coordinates[1] < found_antena_coordinates[1]:
        direction = (1, 1)

    try:
        fr = found_antena_coordinates[0]
        fc = found_antena_coordinates[1]

        while 0 <= fr < len(antinode_grid) and 0 <= fc < len(antinode_grid[0]):
            fr += distance[0]*direction[0]
            fc += distance[1]*direction[1]
            
            if 0 <= fr < len(antinode_grid) and 0 <= fc < len(antinode_grid[0]):
                antinode_grid[fr][fc] = '#'

        fr = found_antena_coordinates[0]
        fc = found_antena_coordinates[1]

        while 0 <= fr < len(antinode_grid) and 0 <= fc < len(antinode_grid[0]):
            fr += (-1) * distance[0]*direction[0]
            fc += (-1) * distance[1]*direction[1]
            
            if 0 <= fr < len(antinode_grid) and 0 <= fc < len(antinode_grid[0]):
                antinode_grid[fr][fc] = '#'


        br = base_antena_coordinates[0]
        bc = base_antena_coordinates[1]

        while 0 <= br < len(antinode_grid) and 0 <= bc < len(antinode_grid[0]):
            br += (-1) * distance[0]*direction[0]
            bc += (-1) * distance[1]*direction[1]

            if 0 <= br < len(antinode_grid) and 0 <= bc < len(antinode_grid[0]):
                antinode_grid[br][bc] = '#'

        br = base_antena_coordinates[0]
        bc = base_antena_coordinates[1]

        while 0 <= br < len(antinode_grid) and 0 <= bc < len(antinode_grid[0]):
            br += distance[0]*direction[0]
            bc += distance[1]*direction[1]

            if 0 <= br < len(antinode_grid) and 0 <= bc < len(antinode_grid[0]):
                antinode_grid[br][bc] = '#'        
    except:
        pass


def mark_antinode_grid_for_specific_antena(antinode_grid, grid, antena_coordinates, antena):
    for r in range(antena_coordinates[0], len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == antena:
                distance = (abs(r - antena_coordinates[0]), abs(c - antena_coordinates[1]))
                place_antinode(antinode_grid, distance, antena_coordinates, (r, c))


def prepare_antinode_grid(antinode_grid, grid, antena):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == antena:
                mark_antinode_grid_for_specific_antena(antinode_grid, grid, (r, c), antena)


def print_antinode_grid(antinode_grid):
    for row in antinode_grid:
        print(row)



for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] != '.':
            antena = grid[r][c]
            prepare_antinode_grid(antinode_grid, grid, antena)

total_antinodes = 0

for r in range(len(antinode_grid)):
    for c in range(len(antinode_grid[0])):
        if antinode_grid[r][c] == '#':
            total_antinodes += 1

print(total_antinodes)
# print_antinode_grid(antinode_grid)