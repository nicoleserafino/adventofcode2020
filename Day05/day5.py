import collections, math, re

lines = [l.rstrip('\n') for l in open("2020/Day05/input.txt")]

mm = 0
allst = set()
for line in lines:
    line = line.replace('F', '0')
    line = line.replace('B', '1')
    line = line.replace('L', '0')
    line = line.replace('R', '1')
    num = int(line, 2)
    mm = max(num, mm)
    allst.add(num)

print("Part 1:", mm)
for i in allst:
    if i+1 not in allst and i+2 in allst:
        print("Part 2:", i+1)