from functools import cached_property


class LocationPoint:
    def __init__(self, height: int, x_pos: int, y_pos: int, map_size: list[int]):
        self.height = height
        self.x_pos: int = x_pos
        self.y_pos: int = y_pos
        self.map_size: list[int] = map_size

    def get_neighbour_positions(self) -> list[list[int]]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        return [[self.x_pos + x, self.y_pos + y]
                for x, y in directions
                if 0 <= self.x_pos + x < self.map_size[0] and 0 <= self.y_pos + y < self.map_size[1]]


class HeightMap:
    def __init__(self, levels: list[list[int]]):
        self.map_size = [len(levels), len(levels[0])]
        self.all_location_points: list[LocationPoint] = [
            LocationPoint(levels[idx][idy], idx, idy, self.map_size)
            for idx in range(self.map_size[0]) for idy in range(self.map_size[1])
        ]

    def get_location_point_by_position(self, search_x_pos: int, search_y_pos: int) -> LocationPoint:
        for p in self.all_location_points:
            if p.x_pos == search_x_pos and p.y_pos == search_y_pos:
                return p

    @cached_property
    def low_points(self) -> list[LocationPoint]:
        output = []
        for p in self.all_location_points:
            neighbours = [self.get_location_point_by_position(
                x, y) for x, y in p.get_neighbour_positions()]
            if p.height < min(n.height for n in neighbours):
                output.append(p)
        return output

    def risk_level(self) -> int:
        return sum(1+p.height for p in self.low_points)

    def get_basin_size(self, low_point: LocationPoint) -> int:
        basin_points: list[LocationPoint] = []
        points_to_explore: list[LocationPoint] = [self.get_location_point_by_position(
            x, y) for x, y in low_point.get_neighbour_positions()]
        already_explored: list[LocationPoint] = []

        while points_to_explore:
            next_point = points_to_explore.pop()
            already_explored.append(next_point)
            if next_point.height < 9:
                basin_points.append(next_point)
                for neighbour in [self.get_location_point_by_position(
                        x, y) for x, y in next_point.get_neighbour_positions()]:
                    if neighbour not in already_explored and neighbour not in points_to_explore:
                        points_to_explore.append(neighbour)
        return len(basin_points)


if __name__ == '__main__':
    with open("2021/09.txt", 'r') as f:
        levels = [[int(c) for c in t.strip()] for t in f.readlines()]

    map = HeightMap(levels)
    print('part1:', map.risk_level())

    basin_sizes = [map.get_basin_size(l) for l in map.low_points]
    basin_sizes.sort()
    print('part2:', basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])
