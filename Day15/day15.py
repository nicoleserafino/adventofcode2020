def memory_game(numbers, n_th):
    spoken = {numbers[i]: i for i in range(len(numbers)-1)}
    current = numbers[-1]
    for i in range(len(numbers)-1, n_th-1):
        spoken[current], current = i, i - spoken[current] if current in spoken else 0
    return current

numbers = list(map(int, open('2020\Day15\input.txt').read().split(',')))

part1 = memory_game(numbers, 2020)
part2 = memory_game(numbers, 30000000)

print(f'Part 1: {part1}, Part 2: {part2}')