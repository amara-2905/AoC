import re
from itertools import product

machines = [] 
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        indicator_light_pattern = re.search(r"\[(.*?)\]", line).group(1)
        buttons = re.findall(r"\((.*?)\)", line)
        button_lists = []
        for g in buttons:
            nums = [int(x) for x in g.split(",") if x.strip() != ""]
            button_lists.append(nums)
        machines.append((indicator_light_pattern, button_lists))
        joltage = re.search(r"\{(.*?)\}", line).group(1)
        joltage_list = [int(x) for x in joltage.split(",")]

# part 1 
def toggle(pattern,buttons):
    pattern = list(pattern)
    for b in buttons:
        if pattern[b] == "#":
            pattern[b] = "."
        else:
            pattern[b] = "#"
    return "".join(pattern)

def solve_machine(pattern, button_lists):
    n = len(button_lists)
    best = float("inf")
    for choice in product([0,1], repeat=n):
        presses = sum(choice)
        if presses >= best:
            continue
        state = "." * len(pattern)
        for i, press in enumerate(choice):
            if press == 1:
                state = toggle(state, button_lists[i])
        if state == pattern:
            best = presses
    return best

count = 0 
for i, (pattern,buttons) in enumerate(machines):
    best = solve_machine(pattern,buttons)
    count = count + best 
print(count)

# part 2 
