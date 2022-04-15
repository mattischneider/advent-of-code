with open("2021/06.txt", "r") as file:
    fish_raw_list = list(map(int, file.read().split(",")))
    fishs = {i: sum(1 for r in fish_raw_list if r == i) for i in range(9)}

for i in range(256):
    number_of_dead_fish = fishs[0]
    for j in range(1, 9):
        fishs[j - 1] = fishs[j]
    fishs[6] += number_of_dead_fish
    fishs[8] = number_of_dead_fish
    if i == 79:
        print("part1", sum(fishs.values()))
    if i == 255:
        print("part2", sum(fishs.values()))
