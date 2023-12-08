from collections import namedtuple
from dataclasses import dataclass

NetworkPoint = namedtuple("NetworkPoint", ["node_name", "directions"])


@dataclass()
class Network:
    points: list[NetworkPoint]
    directions: str  # e.g. 'LLLRLRLR'

    def get_network_point_by_node_name(self, search_node_name: str) -> NetworkPoint:
        for p in self.points:
            if p.node_name == search_node_name:
                return p
        print(f"{search_node_name} not found in network.")
        raise KeyError

    def get_number_of_steps(self) -> int:
        num_of_steps = 0
        current_point = self.get_network_point_by_node_name("AAA")
        current_instruction_idx = 0
        current_direction = self.directions[current_instruction_idx]
        while current_point.node_name != "ZZZ":
            num_of_steps += 1
            current_point = self.get_network_point_by_node_name(
                current_point.directions[current_direction]
            )
            current_instruction_idx = (current_instruction_idx + 1) % len(
                self.directions
            )
            current_direction = self.directions[current_instruction_idx]
        return num_of_steps


def parse_input(file_name) -> Network:
    with open(file_name, "r") as f:
        data = [line.strip() for line in f.readlines()]
    points = []
    for d in data[2:]:
        points.append(
            NetworkPoint(node_name=d[0:3], directions={"L": d[7:10], "R": d[12:15]})
        )
    return Network(directions=data[0], points=points)


def main():
    network = parse_input("2023/08_test_input")
    part_1 = network.get_number_of_steps()
    print(f"test part1: {part_1} (should be 2)")

    network = parse_input("2023/08_input")
    part_1 = network.get_number_of_steps()
    print(f"part1: {part_1} (should be 19631)")


if __name__ == "__main__":
    main()
