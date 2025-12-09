from pathlib import Path


def is_invalid_id_part1(i: str) -> bool:
    if len(i) % 2 == 1:
        return False
    return i[0 : int(len(i) / 2)] == i[int(len(i) / 2) : (len(i) + 1)]


with Path("2025/02.txt").open() as f:
    ids = [i.strip().split("-") for i in f.readline().split(",")]

invalid_ids_part1 = [
    i
    for left, right in ids
    for i in range(int(left), int(right) + 1)
    if is_invalid_id_part1(str(i))
]
print("part1:", sum(invalid_ids_part1))


def is_invalid_id_part2(i: str) -> bool:
    for lenght_pattern in range(1, len(i) // 2 + 1):
        pattern = i[0:lenght_pattern]
        times = len(i) // lenght_pattern
        if i == pattern * times:
            return True
    return False


invalid_ids_part2 = [
    i
    for left, right in ids
    for i in range(int(left), int(right) + 1)
    if is_invalid_id_part2(str(i))
]
print("part2:", sum(invalid_ids_part2))
