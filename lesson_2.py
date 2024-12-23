report = [[int(n) for n in line.split()] for line in open("day2.txt").readlines()]

def is_safe(levels):
    deltas = [b - a for a, b in zip(levels, levels[1:])]
    
    # Check for strictly increasing or strictly decreasing
    is_increasing = all(1 <= d <= 3 for d in deltas)
    is_decreasing = all(-3 <= d <= -1 for d in deltas)
    
    return is_increasing or is_decreasing

def is_safe_with_dampener(levels):
    # If the original report is already safe
    if is_safe(levels):
        return True
    
    # Try removing each level and check if the resulting list is safe
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]  # Remove the i-th level
        if is_safe(new_levels):
            return True
    
    return False

# Count the reports that are safe with or without the dampener
part_2 = sum(1 for levels in report if is_safe_with_dampener(levels))

print(part_2)
