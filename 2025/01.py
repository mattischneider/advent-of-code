from pathlib import Path

with Path("2025/01.txt").open() as f:
    instructions = f.readlines()

current_position = 50
num_of_0 = 0
num_of_clicks_at_0 = 0

for instruction in instructions:
    num_of_dials = int(instruction[1:])
    prev_position = current_position
    if instruction[0] == "R":
        raw_new_position = current_position + num_of_dials
        current_position = raw_new_position % 100
        num_of_clicks_at_0 += raw_new_position // 100
    if instruction[0] == "L":
        raw_new_position = current_position - num_of_dials
        current_position = raw_new_position % 100
        if prev_position == 0:
            num_of_clicks_at_0 += -raw_new_position // 100
        if prev_position > 0 and raw_new_position <= 0:
            num_of_clicks_at_0 += 1 + -raw_new_position // 100
    if current_position == 0:
        num_of_0 += 1

print(f"part1: {num_of_0}")
print(f"part2: {num_of_clicks_at_0}")
