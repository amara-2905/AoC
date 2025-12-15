from collections import deque

points = [] 
with open("input.txt","r") as f:
    for i in f:
        points.append(i.strip())

coordinates = [] 
for item in points:
    parts = item.split(",")
    x, y= map(int, parts)
    coordinates.append((x, y))

# part 1 
def largest_rectangle(points):
    n = len(points)
    best = 0
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i+1, n):
            x2, y2 = points[j]
            if x1 == x2 or y1 == y2:
                continue
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if area > best:
                best = area
    return best
result = largest_rectangle(coordinates)
print(result)

# part 2
OUTSIDE = 0; INSIDE = 1; UNKNOWN = 2
def solve(points):
    n = len(points)
    def shrink(axis):
        values = sorted(set(axis + [0, 10**18]))
        return {v: i for i, v in enumerate(values)}
    shrink_x = shrink([x for x, y in points])
    shrink_y = shrink([y for x, y in points])
    shrunk = [(shrink_x[x], shrink_y[y]) for x, y in points]
    width = len(shrink_x)
    height = len(shrink_y)
    grid = [[UNKNOWN for _ in range(width)] for _ in range(height)]
    for i in range(n):
        x1, y1 = shrunk[i]
        x2, y2 = shrunk[(i + 1) % n]
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                grid[y][x] = INSIDE
    queue = deque([(0, 0)])
    grid[0][0] = OUTSIDE
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if grid[ny][nx] == UNKNOWN:
                    grid[ny][nx] = OUTSIDE
                    queue.append((nx, ny))
    ps = [[0] * (width + 1) for _ in range(height + 1)]
    for y in range(1, height + 1):
        for x in range(1, width + 1):
            value = 1 if grid[y-1][x-1] != OUTSIDE else 0
            ps[y][x] = (value + ps[y-1][x] + ps[y][x-1] - ps[y-1][x-1])
    best_area = 0
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = shrunk[i]
            x2, y2 = shrunk[j]
            min_x, max_x = min(x1, x2), max(x1, x2)
            min_y, max_y = min(y1, y2), max(y1, y2)
            expected = (max_x - min_x + 1) * (max_y - min_y + 1)
            actual = (ps[max_y + 1][max_x + 1] - ps[min_y][max_x + 1] - ps[max_y + 1][min_x] + ps[min_y][min_x])
            if expected == actual:
                ox1, oy1 = points[i]
                ox2, oy2 = points[j]
                area = (abs(ox1 - ox2) + 1) * (abs(oy1 - oy2) + 1)
                best_area = max(best_area, area)
    return best_area
print(solve(coordinates))