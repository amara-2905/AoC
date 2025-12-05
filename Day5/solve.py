ranges = []
values = [] 

with open("input.txt","r") as f:
    for line in f:
        line = line.strip() 
        if not line:
            continue
        if "-" in line:
            ranges.append(line)
        else:
            values.append(line)

# print(ranges)
# print(values)

range_tuples = []

for r in ranges:
    left, right = r.split("-")
    range_tuples.append((int(left), int(right)))

# print(range_tuples)

# part 1 
count = 0 
def value_in_range(value,ranges):
    for low,high in ranges:
        if low <= int(value) <= high:
            return True 
    return False

for i in values:
    if value_in_range(i,range_tuples):
        count = count + 1
print(count) 

# part 2 
range_tuples.sort()

merged = []
low, high = range_tuples[0]

for l, h in range_tuples[1:]:
    if l <= high + 1:
        high = max(high, h)
    else:
        merged.append((low, high))
        low, high = l, h

merged.append((low, high))

count = sum(high - low + 1 for low, high in merged)
print(count)