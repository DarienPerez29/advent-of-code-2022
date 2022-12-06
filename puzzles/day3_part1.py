items_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
items_shared = ""
priority_sum = 0

while True:
    rucksack_items = input()
    if rucksack_items == "eof":
        break

    compartment1 = rucksack_items[:len(rucksack_items) // 2]
    compartment2 = rucksack_items[len(rucksack_items) // 2:]

    for item in compartment1:
        if item in compartment2:
            items_shared += item
            break

for item in items_shared:
    priority_sum += items_list.find(item) + 1

print(priority_sum)
