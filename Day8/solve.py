coordinates = []
data = [] 
with open("input.txt","r") as f:
    for line in f:
        data.append(line.strip())

for item in data:
    parts = item.split(",")
    while len(parts) < 3:
        parts.append("0")
    x, y, z = map(int, parts)
    coordinates.append((x, y, z))

# part 1
edges = []
n = len(coordinates)
for i in range(n):
    x1, y1, z1 = coordinates[i]
    for j in range(i + 1, n):
        x2, y2, z2 = coordinates[j]
        dx = x1 - x2
        dy = y1 - y2
        dz = z1 - z2
        dist2 = dx*dx + dy*dy + dz*dz  
        edges.append((dist2, i, j))
edges.sort()
closest_1000 = edges[:1000]

parent = list(range(n))
size = [1] * n

for _, a, b in closest_1000:
    x = a
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    ra = x
    x = b
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    rb = x
    if ra != rb:
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]

component_sizes = {}
for i in range(n):
    x = i
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    r = x
    if r not in component_sizes:
        component_sizes[r] = 0
    component_sizes[r] += 1

sizes = sorted(component_sizes.values(), reverse=True)
answer = sizes[0] * sizes[1] * sizes[2]

print(answer)

# part 2
answer = 0
parent = list(range(n))
size = [1] * n
components = n  
last_a = None
last_b = None

for dist2, a, b in edges:
    x = a
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    ra = x
    x = b
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    rb = x

    if ra != rb:
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]

        components -= 1    
        last_a = a
        last_b = b
        if components == 1:
            break

x1 = coordinates[last_a][0]
x2 = coordinates[last_b][0]

answer = x1 * x2
print(answer)