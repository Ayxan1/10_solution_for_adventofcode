def generate_combinations(n):
    combinations = []
    num_combinations = 3 ** (n - 1)

    for i in range(num_combinations):
        combination = []
        for j in range(n - 1):
            if (i % 3) == 0:
                combination.append('+')
            elif (i % 3) == 1:
                combination.append('*')
            else:
                combination.append('||')
            i //= 3
        combinations.append(combination)
    return combinations

def calculate_possible_combinations(operands):
    all_operation_combinations = generate_combinations(len(operands))
    results = []

    for operation_combination in all_operation_combinations:
        result = operands[0]  # Start with the first operand

        # Apply each operator between operands
        for i in range(1, len(operands)):
            if operation_combination[i - 1] == '+':
                result += operands[i]
            elif operation_combination[i - 1] == '*':
                result *= operands[i]
            elif operation_combination[i - 1] == '||':
                result = int(str(result) + str(operands[i]))  # Concatenate the results and convert to int

        results.append(result)

    return results

# Read data from the file
data = open("day7.txt", "r").read()
left = []
right = []

# Parse the data into left and right lists
for line in data.strip().split("\n"):
    left_part, right_part = line.split(":")
    left.append(int(left_part.strip()))
    right.append([int(x) for x in right_part.strip().split()])

# Process each set of operands and compare results
total = 0
for i in range(len(left)):
    given_result = left[i]
    possible_results = calculate_possible_combinations(right[i])
    if given_result in possible_results:
        total += given_result

print(total)
