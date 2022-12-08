trees = []
visible_trees = 0


def is_tree_visible(my_tree, y, x):
    visibility = True
    # Check up
    for y2 in range(y - 1, -1, -1):
        outer_tree = trees[y2][x]
        if my_tree > outer_tree:
            visibility = True
        else:
            visibility = False
            break

    if visibility:
        return True

    # Check down
    for y2 in range(y + 1, len(trees)):
        outer_tree = trees[y2][x]
        if my_tree > outer_tree:
            visibility = True
        else:
            visibility = False
            break

    if visibility:
        return True

    # Check left
    for x2 in range(x - 1, -1, -1):
        outer_tree = trees[y][x2]
        if my_tree > outer_tree:
            visibility = True
        else:
            visibility = False
            break

    if visibility:
        return True

    # Check right
    for x2 in range(x + 1, len(trees[y])):
        outer_tree = trees[y][x2]
        if my_tree > outer_tree:
            visibility = True
        else:
            visibility = False
            break

    if visibility:
        return True

    return False


while True:
    line = input()
    if line == "eof":
        break

    trees.append([int(s) for s in line])

# Adding edge visible trees
visible_trees += len(trees[0]) + len(trees[-1])
visible_trees += (len(trees) - 2) * 2

for i in range(1, len(trees) - 1):
    for j in range(1, len(trees[i]) - 1):
        if is_tree_visible(trees[i][j], i, j):
            visible_trees += 1

print(visible_trees)
