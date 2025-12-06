with open("input.txt", "r") as f:
    data = f.read()

lines = data.split("\n")
if lines and lines[-1] == "":
    lines = lines[:-1]

rows = [line.split() for line in lines]
columns = list(zip(*rows))

# part 1
result = 0 
for i in columns:
    if i[len(i)-1] == "*":
        result = result + (int(i[0]) * int(i[1]) * int(i[2]) * int(i[3]))
    else:
        result = result + (int(i[0]) + int(i[1]) + int(i[2]) + int(i[3]))
print(result)

# part 2
operation_line = lines[-1]
operators = []
operator_column_starts = []

for column_index, char in enumerate(operation_line):
    if char != " ":
        operators.append(char)
        operator_column_starts.append(column_index)

operator_column_starts.append(len(operation_line))

data_rows_count = len(lines) - 1
total = 0

if data_rows_count > 0:
    for operator_index in range(len(operators)):
        current_operator = operators[operator_index]
        value = 0

        if current_operator == "*":
            value = 1

        group_start_column = operator_column_starts[operator_index]
        group_end_column = operator_column_starts[operator_index + 1]

        if operator_index < len(operators) - 1:
            group_end_column -= 1

        for c in range(group_start_column, group_end_column):
            number = 0

            for r in range(data_rows_count):
                if c < len(lines[r]):
                    character = lines[r][c]
                    if character != " ":
                        number = number * 10 + int(character)

            if current_operator == "*":
                value *= number
            else:
                value += number

        total += value
print(total)