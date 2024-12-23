test_input = open("1_input.txt", "r").read()
test_input_list = [int(n) for n in test_input.split()]
left = test_input_list[0::2]
right = test_input_list[1::2]
left.sort()
right.sort()
total = 0

for n_left, n_right in zip(left, right):
    total += n_left*right.count(n_left)

print(total)     