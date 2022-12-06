items_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
badges_list = ""
priority_sum = 0

while True:
    elves_rucksacks = []
    for _ in range(3):
        elves_rucksacks.append(input())

    if "eof" in elves_rucksacks:
        break

    for item in elves_rucksacks[0]:
        if item in elves_rucksacks[1] and item in elves_rucksacks[2]:
            badges_list += item
            break


for badge in badges_list:
    priority_sum += items_list.find(badge) + 1

print(priority_sum)
