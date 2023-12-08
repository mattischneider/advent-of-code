from dataclasses import dataclass
import math


@dataclass()
class Network:
    points: dict[
        str, dict[str, str]
    ]  # key values of the form 'name': {'L': leftnode}, {'R': rightnode}
    directions: str  # e.g. 'LLLRLRLR'

    def get_network_point_by_node_name(self, search_node_name: str) -> dict[str, str]:
        return self.points[search_node_name]

    def get_number_of_steps(self, start_point="AAA", end_point="ZZZ") -> int:
        num_of_steps = 0
        current_point = start_point
        current_instruction_idx = 0
        current_direction = self.directions[current_instruction_idx]
        while (len(end_point) == 3 and current_point != end_point) or (
            len(end_point) == 1 and current_point[2] != end_point
        ):
            num_of_steps += 1
            current_point = self.points[current_point][current_direction]
            current_instruction_idx = (current_instruction_idx + 1) % len(
                self.directions
            )
            current_direction = self.directions[current_instruction_idx]
        return num_of_steps

    def get_number_of_ghost_steps(self) -> int:
        current_points = [c for c in self.points if c[2] == "A"]
        num_steps_of_each_path = [
            self.get_number_of_steps(start_point=c, end_point="Z")
            for c in current_points
        ]
        return math.lcm(*num_steps_of_each_path)


def parse_input(file_name) -> Network:
    with open(file_name, "r") as f:
        data = [line.strip() for line in f.readlines()]
    points = {d[0:3]: {"L": d[7:10], "R": d[12:15]} for d in data[2:]}
    return Network(directions=data[0], points=points)


def main():
    network = parse_input("2023/08_test_input")
    part_1 = network.get_number_of_steps()
    print(f"test part1: {part_1} (should be 2)")

    network = parse_input("2023/08_test_input2")
    part_2 = network.get_number_of_ghost_steps()
    print(f"test part2: {part_2} (should be 6)")

    network = parse_input("2023/08_input")
    part_1 = network.get_number_of_steps()
    print(f"part1: {part_1} (should be 19631)")
    part_2 = network.get_number_of_ghost_steps()
    print(f"part2: {part_2} (should be )")


if __name__ == "__main__":
    main()
