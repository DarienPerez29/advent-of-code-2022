stacks = {
    1: ["Z", "J", "N", "W", "P", "S"],
    2: ["G", "S", "T"],
    3: ["V", "Q", "R", "L", "H"],
    4: ["V", "S", "T", "D"],
    5: ["Q", "Z", "T", "D", "B", "M", "J"],
    6: ["M", "W", "T", "J", "D", "C", "Z", "L"],
    7: ["L", "P", "M", "W", "G", "T", "J"],
    8: ["N", "G", "M", "T", "B", "F", "Q", "H"],
    9: ["R", "D", "G", "C", "P", "B", "Q", "W"]
}

while True:
    line = input()
    if line == "eof":
        break

    data = line.split()
    move_val = int(data[1])
    from_stack_val = int(data[3])
    to_stack_val = int(data[5])

    moving_stack = stacks[from_stack_val][-(move_val):]
    stacks[to_stack_val].extend(moving_stack)

    for _ in range(move_val):
        stacks[from_stack_val].pop()

for key in stacks:
    print(f"{key}: {stacks[key]}")

for key in stacks:
    print(stacks[key][-1], end="")
