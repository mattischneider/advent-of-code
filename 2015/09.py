from itertools import permutations

import parse


class Graph:
    def __init__(self, filename: str):
        self.vertices = []
        self.weights = []
        with open(filename, "r") as f:
            distance_raw = f.read().splitlines()
        for d in distance_raw:
            parse_dist = parse.parse("{from} to {to} = {distance:d}", d)
            self.vertices.append(parse_dist["from"])
            self.vertices.append(parse_dist["to"])
            self.weights.append(
                {
                    "cities": {parse_dist["from"], parse_dist["to"]},
                    "distance": parse_dist["distance"],
                }
            )
        self.vertices = list(set(self.vertices))

    def get_weight(self, from_city: str, to_city: str) -> int:
        for w in self.weights:
            if w["cities"] == {from_city, to_city}:
                return w["distance"]

    def get_trip_length(self, list_of_cities: list[str]) -> int:
        return sum(
            self.get_weight(list_of_cities[i], list_of_cities[i + 1])
            for i in range(len(list_of_cities) - 1)
        )

    def get_shortest_path(self):
        return min(self.get_trip_length(list(p)) for p in permutations(self.vertices))

    def get_longest_path(self):
        return max(self.get_trip_length(list(p)) for p in permutations(self.vertices))


def test_graph():
    file_name = "2015/09_test"
    graph = Graph(file_name)
    assert graph.get_shortest_path() == 605
    assert graph.get_longest_path() == 982


def main():
    file_name = "2015/09_input"
    graph = Graph(file_name)
    print("part1", graph.get_shortest_path())
    print("part2", graph.get_longest_path())


if __name__ == "__main__":
    main()
