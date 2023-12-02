import parse
from dataclasses import dataclass
from collections import Counter
from functools import reduce


@dataclass()
class Game:
    game_number: int
    cubes: list[Counter]

    def is_valid(self) -> bool:
        for c in self.cubes:
            if c["red"] > 12 or c["green"] > 13 or c["blue"] > 14:
                return False
        return True

    def get_minimal_set(self) -> Counter:
        out = Counter()
        for g in self.cubes:
            for c in g:
                if out[c] < g[c]:
                    out[c] = g[c]
        return out

    def power_of_cubes(self) -> int:
        return reduce(lambda x, y: x * y, self.get_minimal_set().values())


def get_games(file_name) -> list[Game]:
    with open(file_name, "r") as f:
        data = [line.strip() for line in f.readlines()]
    out = []
    for d in data:
        game_parse = parse.parse("Game {game_number:d}: {cubes}", d)
        cubes = []
        for cube_str in game_parse["cubes"].split(";"):
            counter_temp = Counter()
            for cube_set in cube_str.split(","):
                cube_parse = parse.parse(
                    "{num_of_cubes:d} {cube_color}", cube_set.strip()
                )
                cube_dict = {cube_parse["cube_color"]: cube_parse["num_of_cubes"]}
                counter_temp += Counter(cube_dict)
            cubes.append(counter_temp)
        out.append(Game(game_number=game_parse["game_number"], cubes=cubes))
    return out


def get_sum_of_valid_games(games: list[Game]) -> int:
    return sum(g.game_number for g in games if g.is_valid())


def get_sum_of_power_cubes_from_games(games: list[Game]) -> int:
    return sum(g.power_of_cubes() for g in games)


def main():
    games = get_games("2023/02_test_input")
    part_1 = get_sum_of_valid_games(games)
    part_2 = get_sum_of_power_cubes_from_games(games)
    print(f"test part1: {part_1}")
    print(f"test part2: {part_2}")

    games = get_games("2023/02_input")
    part_1 = get_sum_of_valid_games(games)
    part_2 = get_sum_of_power_cubes_from_games(games)
    print(f"part1: {part_1}")
    print(f"part2: {part_2}")


if __name__ == "__main__":
    main()
