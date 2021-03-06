with open("2020/Day11/input.txt") as f:
    data = [list(row) for row in f.read().split('\n')]

def state(grid):
    r, c = len(grid), len(grid[0])
    newGrid = [[grid[i][j] for j in range(c)] for i in range(r)]
    changeHappen = False
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '.':
                continue

            adj = 0
            adj += i and j and grid[i-1][j-1] == '#'
            adj += i and grid[i-1][j] == '#'
            adj += i and j + 1 < c and grid[i-1][j+1] == '#'
            adj += j and grid[i][j-1] == '#'
            adj += j + 1 < c and grid[i][j+1] == '#'
            adj += i + 1 < r and j and grid[i+1][j-1] == '#'
            adj += i + 1 < r and grid[i+1][j] == '#'
            adj += i + 1 < r and j + 1 < c and grid[i+1][j+1] == '#'
            
            if grid[i][j] == 'L' and adj == 0:
                changeHappen = True
                newGrid[i][j] = '#'
            elif grid[i][j] == '#' and adj >= 4:
                changeHappen = True
                newGrid[i][j] = 'L'
    return newGrid, changeHappen

changeHappen = True
while changeHappen:
    data, changeHappen = state(data)

total = 0
for row in data:
    total += row.count('#')
print("Part 1:", total)

def canSee(grid, r, c, dr, dc):
    if r < 0 or r == len(grid) or c < 0 or c == len(grid[0]) or grid[r][c] == 'L':
        return False
    if grid[r][c] == '#':
        return True
    return canSee(grid, r+dr, c+dc, dr, dc)

def state(grid):
    r, c = len(grid), len(grid[0])
    newGrid = [[grid[i][j] for j in range(c)] for i in range(r)]
    changeHappen = False
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '.':
                continue

            adj = 0
            adj += canSee(grid, i-1, j-1, -1, -1)
            adj += canSee(grid, i-1, j  , -1,  0)
            adj += canSee(grid, i-1, j+1, -1,  1)
            adj += canSee(grid, i  , j-1,  0, -1)
            adj += canSee(grid, i  , j+1,  0,  1)
            adj += canSee(grid, i+1, j-1,  1, -1)
            adj += canSee(grid, i+1, j  ,  1,  0)
            adj += canSee(grid, i+1, j+1,  1,  1)
            
            if grid[i][j] == 'L' and adj == 0:
                changeHappen = True
                newGrid[i][j] = '#'
            elif grid[i][j] == '#' and adj >= 5:
                changeHappen = True
                newGrid[i][j] = 'L'
    
    return newGrid, changeHappen

changeHappen = True
while changeHappen:
    data, changeHappen = state(data)

total = 0
for row in data:
    total += row.count('#')
print("Part 2:", total)