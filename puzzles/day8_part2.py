trees = []
visible_trees = 0


def get_scenic_score(my_tree, y, x):
    up = 0
    down = 0
    left = 0
    right = 0

    # Check up
    for y2 in range(y - 1, -1, -1):
        outer_tree = trees[y2][x]
        up += 1
        if my_tree <= outer_tree:
            break

    # Check down
    for y2 in range(y + 1, len(trees)):
        outer_tree = trees[y2][x]
        down += 1
        if my_tree <= outer_tree:
            break

    # Check left
    for x2 in range(x - 1, -1, -1):
        outer_tree = trees[y][x2]
        left += 1
        if my_tree <= outer_tree:
            break

    # Check right
    for x2 in range(x + 1, len(trees[y])):
        outer_tree = trees[y][x2]
        right += 1
        if my_tree <= outer_tree:
            break

    return up * down * left * right


while True:
    line = input()
    if line == "eof":
        break

    trees.append([int(s) for s in line])

max_score = 0
for i in range(0, len(trees)):
    for j in range(0, len(trees[i])):
        tree_score = get_scenic_score(trees[i][j], i, j)
        if tree_score > max_score:
            max_score = tree_score

print(max_score)
