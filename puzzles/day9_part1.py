visited = ["[0, 0]"]
head = [0, 0]
tail = [0, 0]

dir_dic = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (1, 1),
    "D": (1, -1)
}

while True:
    line = input()
    if line == "eof":
        break

    move = line.split()
    command = move[0]
    steps = int(move[1])

    axis = dir_dic[command][0]
    jump = dir_dic[command][1]

    for _ in range(steps):
        head[axis] += jump

        if abs(head[axis] - tail[axis]) > 1:
            tail[axis] += jump
            tail[abs(axis - 1)] = head[abs(axis - 1)]

        tail_coor = str(tail)
        if tail_coor not in visited:
            visited.append(tail_coor)

print()
print(len(visited))
