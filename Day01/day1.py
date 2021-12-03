input = '2020\Day01\input.txt'

with open(input, 'r') as file:
    data = {int(number) for number in file}

print("Part 1:", {entry * (2020-entry) for entry in data if (2020-entry) in data})

print("Part 2:", {entry1 * entry2 * (2020 - entry1 - entry2)
    for entry1 in data for entry2 in data
    if (2020 - entry1 - entry2) in data})