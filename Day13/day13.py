from functools import reduce

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def chinese_remainder(n, a):
    sum_ = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum_ += a_i * mul_inv(p, n_i) * p
    return sum_ % prod
def part1(timestamp, buses):
    wait = busid = float('inf')
    for _, bus in buses:
        next_stop = (timestamp // bus + 1) * bus
        bus_wait = next_stop - timestamp
        if bus_wait < wait:
            wait, busid = bus_wait, bus
    return wait * busid

def part2(buses):
    dividers = [bus for _, bus in buses]
    remainders = [bus - i for i, bus in buses]
    return chinese_remainder(dividers, remainders)


timestamp, buses = open('2020\Day13\input.txt', "r").readlines()
timestamp, buses = int(timestamp), [(i, int(bus)) for i, bus in enumerate(buses.split(',')) if bus != 'x']

print(f'Part 1: {part1(timestamp, buses)}')
print(f'Part 2: {part2(buses)}')