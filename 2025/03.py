from pathlib import Path


with Path("2025/03.txt").open() as f:
    ratings = [r.strip() for r in f.readlines()]


def get_max_jolts(rating: str, num_of_batteries: int) -> int:
    rating_int = [int(r) for r in rating]
    output = [0 for _ in range(num_of_batteries)]
    positions = [0 for _ in range(num_of_batteries)]
    for p in range(len(output)):
        _tmp = rating_int[positions[p] : len(rating) - num_of_batteries + 1 + p]
        output[p] = max(_tmp)
        if p < len(output) - 1:
            positions[p + 1] = 1 + rating_int.index(output[p], positions[p])
    return sum(output[i] * 10 ** (num_of_batteries - i - 1) for i in range(len(output)))


print("part1:", sum(get_max_jolts(r, num_of_batteries=2) for r in ratings))
print("part2:", sum(get_max_jolts(r, num_of_batteries=12) for r in ratings))
