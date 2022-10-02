from itertools import product


class StarGrid:
    def __init__(self, grid: list[str], corners_on: bool = False):
        self.grid: list[str] = grid
        self.step: int = 0
        self.corners_on: bool = corners_on

    def __repr__(self) -> str:
        return f"\nafter step: {self.step}\n" + "\n".join("".join(j for j in i) for i in self.grid)

    def num_of_lit_neighbors(self, i: int, j: int) -> int:
        output = 0
        for dx, dy in product(range(-1, 2), repeat=2):
            if (
                (dx == dy == 0)
                or i + dx < 0
                or i + dx >= len(self.grid)
                or j + dy < 0
                or j + dy >= len(self.grid)
            ):
                continue
            if self.grid[i + dx][j + dy] == "#":
                output += 1
        return output

    def _new_state(self, i: int, j: int) -> str:
        if self.corners_on and {i, j} <= {0, len(self.grid) - 1}:
            return "#"
        if self.grid[i][j] == "#" and self.num_of_lit_neighbors(i, j) in (2, 3):
            return "#"
        if self.grid[i][j] == "." and self.num_of_lit_neighbors(i, j) == 3:
            return "#"
        return "."

    def take_a_step(self):
        self.step += 1
        new_grid = self.grid[::]
        for idx, i in enumerate(self.grid):
            new_grid[idx] = "".join(self._new_state(idx, idy) for idy in range(len(self.grid)))
        self.grid = new_grid

    @property
    def lights_on(self) -> int:
        return sum(1 for i in self.grid for j in i if j == "#")


def test_grid():
    filename = "2015/18_test"
    with open(filename, "r") as f:
        grid_raw = f.read().splitlines()
    star_grid = StarGrid(grid_raw)
    assert star_grid.lights_on == 15
    assert star_grid.num_of_lit_neighbors(0, 0) == 1
    assert star_grid.num_of_lit_neighbors(0, 1) == 0
    assert star_grid.num_of_lit_neighbors(1, 1) == 2
    assert star_grid.num_of_lit_neighbors(0, 6) == 1
    assert star_grid.num_of_lit_neighbors(6, 0) == 2
    for _ in range(4):
        star_grid.take_a_step()
    assert star_grid.lights_on == 4


def test_grid_with_corners_on():
    filename = "2015/18_test_corners_on"
    with open(filename, "r") as f:
        grid_raw = f.read().splitlines()
    star_grid_with_corners = StarGrid(grid_raw, True)
    for _ in range(5):
        star_grid_with_corners.take_a_step()
    assert star_grid_with_corners.lights_on == 17


def main():
    filename = "2015/18_input"
    with open(filename, "r") as f:
        grid_raw = f.read().splitlines()
    star_grid = StarGrid(grid_raw)
    for _ in range(100):
        star_grid.take_a_step()
    print("part1:", star_grid.lights_on)
    star_grid_with_corners = StarGrid(grid_raw, True)
    for _ in range(100):
        star_grid_with_corners.take_a_step()
    print("part2:", star_grid_with_corners.lights_on)


if __name__ == "__main__":
    main()
