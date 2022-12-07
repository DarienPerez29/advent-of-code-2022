dir_size = 0
final_dir_size = 0
full_path = []
full_path_string = ""

dir_tree = {
    "/": {
        "size": 0,
        "sub_dirs": []
    }
}

while True:
    content_line = input().split()
    if content_line[0] == "eof":
        break

    # Command identified
    if content_line[0] == "$":
        command = content_line[1]

        # Save dir names
        if command == "cd":
            if content_line[2] != "..":
                full_path.append(content_line[2])
                full_path_string = '/'.join(full_path)
                dir_tree[full_path_string] = {"size": 0, "sub_dirs": []}
            else:
                full_path.pop()

    # Read files
    if content_line[0] == "dir":
        # Add sub_dir to parent dir
        dir_tree[full_path_string]["sub_dirs"].append(
            full_path_string + "/" + content_line[1]
        )
    elif content_line[0].isdigit():
        # Sum size to parent dir
        dir_tree[full_path_string]["size"] += int(content_line[0])

# Sum sub_dir to dir
for dir_name in reversed(dir_tree):
    for sub_dir in dir_tree[dir_name]["sub_dirs"]:
        dir_tree[dir_name]["size"] += dir_tree[sub_dir]["size"]

# Print dir tree
for dir_name in dir_tree:
    print(dir_name, dir_tree[dir_name])

# Final sum
for dir_name in dir_tree:
    dir_size = dir_tree[dir_name]["size"]
    if dir_size <= 100000:
        final_dir_size += dir_size

print(final_dir_size)
