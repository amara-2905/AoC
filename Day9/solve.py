points = [] 
with open("input.txt","r") as f:
    for i in f:
        points.append(i.strip())
# print(points)

coordinates = [] 
for item in points:
    parts = item.split(",")
    x, y= map(int, parts)
    coordinates.append((x, y))
# print(coordinates)

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
