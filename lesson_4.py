grid = open("day4.txt", "r").read().splitlines()

rows = len(grid)
cols = len(grid[0])


found_mas_center_coordinates = {}
def get_xmas_score(r, c):
    score = 0

    for dr in (-1, 1):
        for dc in (-1, 1):
            if dr == dc == 0:
                continue
            
            for i in range(len("MAS")):
                if i > 0:
                    prev_nr = nr
                    prev_nc = nc

                nr = r + dr * i
                nc = c + dc * i

                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == "MAS"[i]:                        
                        if i == 2:
                            try:
                                if found_mas_center_coordinates[(prev_nr, prev_nc)] and found_mas_center_coordinates[(prev_nr, prev_nc)] <2:
                                    score += 1                            
                                    found_mas_center_coordinates[(prev_nr, prev_nc)] += 1
                            except:
                                found_mas_center_coordinates[(prev_nr, prev_nc)] = 1
                    else:
                        break                    
    return score                



total = 0
for r in range(rows):
    for c in range(cols):
        total += get_xmas_score(r, c)

print(total)


