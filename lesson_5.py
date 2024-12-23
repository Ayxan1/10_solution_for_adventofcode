top, bottom = open("day5.txt", "r").read().split("\n\n")

rules = set()

for line in top.split("\n"):
    a, b = line.split("|")
    rules.add((int(a), int(b)))

updates = [list(map(int, line.split(","))) for line in bottom.splitlines()]


def is_in_order(update):
    run_one_more_time = True
    was_reordered = False

    while run_one_more_time:
        run_one_more_time = False
        for rule in rules:
            before, after = rule
            try:
                lower_index = update.index(before)
                upper_index = update.index(after)
                
                if lower_index > upper_index:
                    update[lower_index], update[upper_index] = update[upper_index], update[lower_index]
                    run_one_more_time = True
                    was_reordered = True
            except:
                pass

    return was_reordered        


middle_sum = 0
for update in updates:
    if is_in_order(update):
        middle_index = (len(update)-1) // 2
        middle_sum += update[middle_index]    

print(middle_sum)