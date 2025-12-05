grid = []
with open("input.txt","r") as f:
    for line in f:
        grid.append(line)

# part 1
def count(grid):
    rows = len(grid)
    cols = len(grid[0])
    accessible = 0
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue
            adj = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        adj += 1
            if adj < 4:
                accessible += 1
    return accessible

print(count(grid))

# part 2
def total_removed(grid):
    grid = [list(row) for row in grid]
    rows = len(grid)
    cols = len(grid[0])
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    total_removed = 0
    while True:
        to_remove = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '@':
                    continue
                adj = 0
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == '@':
                            adj += 1
                if adj < 4:
                    to_remove.append((r, c))
        if not to_remove:
            break
        for r, c in to_remove:
            grid[r][c] = '.'
        total_removed += len(to_remove)
    return total_removed

print(total_removed(grid))