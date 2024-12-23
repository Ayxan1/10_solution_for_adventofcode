from collections import deque

def read_file_create_grid():
    return [list(line) for line in open("day6.txt", "r").read().splitlines()]

def find_start_position(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] in {'^', '>', '<', 'v'}:
                return r, c, grid[r][c]
    raise ValueError("No starting position found in the grid.")

def reachable_positions(grid, start_r, start_c, direction):
    movement = {'^': (-1, 0), '>': (0, 1), '<': (0, -1), 'v': (1, 0)}
    change_direction = {'^': '>', '>': 'v', '<': '^', 'v': '<'}
    visited = set()
    queue = deque([(start_r, start_c, direction)])
    
    while queue:
        r, c, d = queue.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        
        next_r, next_c = r + movement[d][0], c + movement[d][1]
        if (0 <= next_r < len(grid)) and (0 <= next_c < len(grid[0])):
            if grid[next_r][next_c] == '#':
                queue.append((r, c, change_direction[d]))
            elif grid[next_r][next_c] == '.':
                queue.append((next_r, next_c, d))
    
    return visited

def causes_cycle(grid, start_r, start_c, direction, obs_r, obs_c):
    movement = {'^': (-1, 0), '>': (0, 1), '<': (0, -1), 'v': (1, 0)}
    change_direction = {'^': '>', '>': 'v', '<': '^', 'v': '<'}
    visited = set()
    r, c, d = start_r, start_c, direction
    
    while (0 <= r < len(grid)) and (0 <= c < len(grid[0])):
        state = (r, c, d)
        if state in visited:
            return True  # Cycle detected
        visited.add(state)
        
        next_r, next_c = r + movement[d][0], c + movement[d][1]
        if (0 <= next_r < len(grid)) and (0 <= next_c < len(grid[0])):
            if (next_r, next_c) == (obs_r, obs_c) or grid[next_r][next_c] == '#':
                d = change_direction[d]
            else:
                r, c = next_r, next_c
        else:
            break
    
    return False

def count_cycle_positions(grid):
    init_r, init_c, init_dir = find_start_position(grid)
    reachable = reachable_positions(grid, init_r, init_c, init_dir)
    
    total_positions = 0
    for r, c in reachable:
        if (r, c) != (init_r, init_c) and grid[r][c] == '.':
            grid[r][c] = 'O'  # Temporarily place obstruction
            if causes_cycle(grid, init_r, init_c, init_dir, r, c):
                total_positions += 1
            grid[r][c] = '.'  # Remove obstruction
    
    return total_positions

# Read and process the grid
grid = read_file_create_grid()
total_possible_positions = count_cycle_positions(grid)
print("Total possible positions for obstruction:", total_possible_positions)
