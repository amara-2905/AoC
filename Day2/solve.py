with open("input.txt","r") as f:
    for line in f:
        parts = line.strip().split(",")
        parts = [p for p in parts if p] 
        ranges = [tuple(p.split("-")) for p in parts]

print(ranges)

array = []

for i in ranges:
    for j in range(int(i[0]), int(i[1]) + 1):
        s = str(j)
        length = len(s)
        if length % 2 != 0:
            continue   
        mid = length // 2
        left = s[0:mid]
        right = s[mid:length]

        if left == right:
            array.append(j)
print(sum(array))

array = [] 
for i in ranges:
    for j in range(int(i[0]), int(i[1]) + 1):
        s = str(j)
        length = len(s)
        found = False
        for L in range(1, length):
            if length % L != 0:
                continue
            c = s[0:L]
            repeat_count = length // L
            if repeat_count >= 2 and c * repeat_count == s:
                found = True
                break
        if found:
            array.append(j)
print(sum(array))
