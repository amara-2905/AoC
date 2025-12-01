current = 50 
count = 0
with open("input.txt","r") as f: 
    directions = [line.strip() for line in f]

# part 1
for direction in directions:
    if not direction:
        continue

    move = direction[0]
    steps = int(direction[1:])

    if move == 'L':
        current = (current - steps) % 100
    else:
        current = (current + steps) % 100
    if current == 0: 
        count = count + 1
print(count)

# part 2
def count_clicks(start_pos, steps, direction):
    count = 0
    total = 100
    if direction == 'L':
        for i in range(1, steps + 1):
            if (start_pos - i) % total == 0:
                count += 1
    else: 
        for i in range(1, steps + 1):
            if (start_pos + i) % total == 0:
                count += 1
    return count

current = 50
total_clicks = 0

for direction in directions:
    move = direction[0]
    steps = int(direction[1:])
    clicks_during = count_clicks(current, steps, move)
    total_clicks += clicks_during
    if move == 'L':
        current = (current - steps) % 100
    else:
        current = (current + steps) % 100
print(total_clicks)