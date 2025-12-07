with open("input.txt","r") as f:
    data=f.read()

grid=[list(line) for line in data.splitlines()]
h=len(grid)
w=len(grid[0])

# part 1
q=[]
seen=set()
splits=0
for i in range(h):
    for j in range(w):
        if grid[i][j]=="S":
            q.append((i,j))
while q:
    r,c=q.pop()
    if (r,c) in seen:
        continue
    seen.add((r,c))
    if r<0 or r>=h or c<0 or c>=w:
        continue
    if grid[r][c]=="^":
        splits+=1
        q.append((r,c-1))
        q.append((r,c+1))
        continue
    q.append((r+1,c))
print(splits)

# part 2
for i in range(h):
    for j in range(w):
        if grid[i][j] == "S":
            start = (i, j)
            break
memo = {}
def count_timelines(r, c):
    if r < 0 or r >= h or c < 0 or c >= w:
        return 1
    if (r, c) in memo:
        return memo[(r, c)]
    cell = grid[r][c]
    if cell == "^":
        total = count_timelines(r, c - 1) + count_timelines(r, c + 1)
    else:
        total = count_timelines(r + 1, c)
    memo[(r, c)] = total
    return total
answer = count_timelines(*start)
print(answer)