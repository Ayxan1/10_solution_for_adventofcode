inputs = list(open("day9.txt", "r").read().strip())

# Step 1: Parse the input into a disk representation
process_1_output = []
fileId = 0
item_type = 1  # file: 1, space: -1

for input in inputs:
    if item_type == 1:
        for _ in range(int(input)):
            process_1_output.append(fileId)
        fileId += 1
    if item_type == -1:
        for _ in range(int(input)):
            process_1_output.append('.')
    item_type *= -1

# Step 2: Identify files and free space
n = len(process_1_output)
file_spans = {}  # {fileId: (start, length)}
free_spans = []  # [(start, length)]

i = 0
while i < n:
    if process_1_output[i] == '.':
        start = i
        while i < n and process_1_output[i] == '.':
            i += 1
        free_spans.append((start, i - start))
    else:
        file_id = process_1_output[i]
        start = i
        while i < n and process_1_output[i] == file_id:
            i += 1
        file_spans[file_id] = (start, i - start)

# Step 3: Move files in descending order of file ID
sorted_files = sorted(file_spans.keys(), reverse=True)

for file_id in sorted_files:
    start, length = file_spans[file_id]
    for j, (free_start, free_length) in enumerate(free_spans):
        if free_length >= length and free_start < start:  # Fit available, left of file
            # Move the whole file
            process_1_output[free_start:free_start + length] = [file_id] * length
            process_1_output[start:start + length] = ['.'] * length
            # Update the free span
            free_spans[j] = (free_start + length, free_length - length)
            # If the free span is used up, remove it
            if free_spans[j][1] == 0:
                free_spans.pop(j)
            # Add the new free space left behind by the file
            free_spans.append((start, length))
            free_spans.sort()  # Keep free spans sorted by start position
            break

# Step 4: Calculate the checksum
total = 0
for i, block in enumerate(process_1_output):
    if block != '.':
        total += int(block) * i

print(total)
