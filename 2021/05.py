from collections import Counter


class Diagram:
    def __init__(self, lines: list[list[int, int]]):
        self.lines = lines

    def get_coords_counter(self, with_diagonals: bool = False):
        coords = []
        for (x1, y1), (x2, y2) in self.lines:
            if x1 == x2:
                for t in range(min(y1, y2), max(y1, y2) + 1):
                    coords.append((x1, t))
            if y1 == y2:
                for t in range(min(x1, x2), max(x1, x2) + 1):
                    coords.append((t, y1))
            if with_diagonals:
                if abs(x1 - x2) == abs(y1 - y2):
                    for t in range(abs(x1 - x2) + 1):
                        sign_x = (x2 - x1 > 0) - (x2 - x1 < 0)
                        sign_y = (y2 - y1 > 0) - (y2 - y1 < 0)
                        coords.append((x1 + sign_x * t, y1 + sign_y * t))
        return Counter(coords)


if __name__ == "__main__":
    with open("2021/05.txt", "r") as f:
        lines = [
            [list(map(lambda x: int(x), c.split(","))) for c in t.split(" -> ")]
            for t in f.readlines()
        ]

    diagram = Diagram(lines)
    counter = diagram.get_coords_counter()
    print("part1:", sum(1 for c in counter.values() if c > 1))
    counter_diags = diagram.get_coords_counter(with_diagonals=True)
    print("part2:", sum(1 for c in counter_diags.values() if c > 1))
