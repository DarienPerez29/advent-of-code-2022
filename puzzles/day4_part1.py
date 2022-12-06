pairs = 0

while True:
    line = input()

    if line == "eof":
        break

    elf1, elf2 = line.split(",")

    elf1_lower, elf1_higher = elf1.split("-")
    elf2_lower, elf2_higher = elf2.split("-")

    elf1_lower, elf1_higher = int(elf1_lower), int(elf1_higher)
    elf2_lower, elf2_higher = int(elf2_lower), int(elf2_higher)

    if (
        elf1_lower >= elf2_lower
        and elf1_higher <= elf2_higher
        or
        elf2_lower >= elf1_lower
        and elf2_higher <= elf1_higher
    ):
        pairs += 1

print(pairs)
