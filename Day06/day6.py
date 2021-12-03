from functools import reduce 

with open('2020/Day06/input.txt') as f:
    input = f.read().split('\n\n')

# part 1
print("Part 1:", sum([len(set("".join(group).replace('\n', ''))) for group in input]))

# part 2
print("Part 2:", sum([len(reduce(lambda x, y: set(x) & set(y), group.split())) for group in input]))