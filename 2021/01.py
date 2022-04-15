with open("2021/01.txt", "r") as f:
    data = [int(line) for line in f.readlines()]

print("part 1:", sum(1 for i in range(1, len(data)) if data[i] > data[i - 1]))
print(
    "part 2:",
    sum(1 for i in range(1, len(data)) if sum(data[i : i + 3]) > sum(data[i - 1 : i + 2])),
)
