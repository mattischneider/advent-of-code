def get_fuel_cost(
    crab_positions: list[int], target_position: int, constant_rate: bool = True
) -> int:
    steps = list(map(lambda x: abs(x - target_position), crab_positions))
    if constant_rate:
        return sum(steps)
    else:
        return int(sum(n * (n + 1) / 2 for n in steps))


with open("2021/07.txt", "r") as file:
    crab_positions = list(map(int, file.read().split(",")))

print(
    "part1:",
    min(
        get_fuel_cost(crab_positions, tp)
        for tp in range(min(crab_positions) + 1, max(crab_positions))
    ),
)
print(
    "part2:",
    min(
        get_fuel_cost(crab_positions, tp, False)
        for tp in range(min(crab_positions) + 1, max(crab_positions))
    ),
)
