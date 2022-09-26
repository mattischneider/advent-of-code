from itertools import permutations

import parse


class DinnerTable:
    def __init__(self, filename: str):
        self.persons = set()
        self.weights = []
        with open(filename, "r") as f:
            raw = f.read().splitlines()
        for d in raw:
            p = parse.parse(
                "{person} would {gain_or_lose} {units:d} happiness units by sitting next to {neighbor}.",  # noqa: E501
                d,
            )
            self.persons.add(p["person"])
            units_sign = 1 if p["gain_or_lose"] == "gain" else -1
            self.weights.append(
                {
                    "neighbors": {p["person"], p["neighbor"]},
                    "units": units_sign * p["units"],
                }
            )

    def get_neighbor_happiness(self, neighbor_config: set[str]) -> int:
        return sum(w["units"] for w in self.weights if w["neighbors"] == neighbor_config)

    def get_total_happiness(self, sitting_config: list[str]) -> int:
        n = len(self.persons)
        return sum(
            self.get_neighbor_happiness({sitting_config[i], sitting_config[(i + 1) % n]})
            for i in range(n)
        )

    def get_max_happiness(self):
        return max(self.get_total_happiness(list(p)) for p in permutations(self.persons))

    def add_yourself_to_table(self):
        self.persons.add("mattipopatti")


def test_dinner_table():
    filename = "2015/13_test"
    dinner_table = DinnerTable(filename)
    assert dinner_table.get_neighbor_happiness({"Alice", "Bob"}) == 137
    assert dinner_table.get_max_happiness() == 330
    dinner_table.add_yourself_to_table()
    assert dinner_table.get_neighbor_happiness({"Alice", "mattipopatti"}) == 0
    assert dinner_table.get_max_happiness() == 286


def main():
    filename = "2015/13_input"
    dinner_table = DinnerTable(filename)
    print("part1:", dinner_table.get_max_happiness())
    dinner_table.add_yourself_to_table()
    print("part2:", dinner_table.get_max_happiness())


if __name__ == "__main__":
    main()
