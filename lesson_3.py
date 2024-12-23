test_input = open("day3.txt", "r").read()

part1 = 0
do = True
dont = False

for start in range(len(test_input)):
    for shift in range(500):
        cmd = test_input[start: start + shift]
        
        if(cmd.startswith("do()")):
            do = True
            dont = False
        if(cmd.startswith("don't()")):
            do = False
            dont = True

        if do and (not dont) and cmd.startswith("mul(") and cmd.endswith(")"):
            args = cmd[4:-1]

            try:
                a, b = args.split(",")
                part1 += (int(a) * int(b))
            except:
                pass
print(part1)            

