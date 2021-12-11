class Octopus:
    def __init__(self, start_level: int, x_pos: int, y_pos: int, grid_size: int):
        self.energy_level: int = start_level
        self.x_pos: int = x_pos
        self.y_pos: int = y_pos
        self.grid_size: int = grid_size

    def get_neighbour_positions(self) -> list[list[int]]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0],
                      [1, 1], [1, -1], [-1, 1], [-1, -1]]
        return [[self.x_pos + x, self.y_pos + y]
                for x, y in directions
                if 0 <= self.x_pos + x < self.grid_size and 0 <= self.y_pos + y < self.grid_size]


class OctopusGrid:

    def __init__(self, start_levels: list[list[int]]):
        self.step = 0
        self.flashes = 0
        self.grid_size = len(start_levels)
        self.octopusses: list[Octopus] = [Octopus(start_levels[idx][idy], idx, idy, self.grid_size)
                                          for idx in range(self.grid_size) for idy in range(self.grid_size)]

    def get_octopus_by_position(self, search_x_pos: int, search_y_pos: int) -> Octopus:
        for o in self.octopusses:
            if o.x_pos == search_x_pos and o.y_pos == search_y_pos:
                return o

    def print_energy_levels(self):
        print(f'{self.step=}')
        print(f'{self.flashes=}')
        for x in range(self.grid_size):
            oline = [self.get_octopus_by_position(
                x, y) for y in range(self.grid_size)]
            print(''.join(str(o.energy_level) for o in oline))
        print('\n')

    def run_step(self) -> list[Octopus]:
        self.step += 1
        for o in self.octopusses:
            o.energy_level += 1
        current_flashes: list[Octopus] = []
        while any(o.energy_level > 9 for o in self.octopusses):
            for o in self.octopusses:
                if o.energy_level <= 9:
                    continue
                for sx, sy in o.get_neighbour_positions():
                    on = self.get_octopus_by_position(sx, sy)
                    if on not in current_flashes:
                        on.energy_level += 1
                o.energy_level = 0
                current_flashes.append(o)
        self.flashes += len(current_flashes)
        self.print_energy_levels()
        return current_flashes

    def get_next_all_flashes_step(self) -> int:
        while True:
            run = self.run_step()
            if len(run) == len(self.octopusses):
                return self.step


if __name__ == '__main__':
    with open("11.txt", 'r') as f:
        start_levels = [[int(c) for c in t.strip()] for t in f.readlines()]

    grid = OctopusGrid(start_levels)
    for _ in range(100):
        grid.run_step()

    print('part1:', grid.flashes)
    print('part2:', grid.get_next_all_flashes_step())
