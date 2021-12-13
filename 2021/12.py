class Cave:
    def __init__(self, name: str):
        self.name: str = name
        self.neighbours: list[Cave] = []

    def add_neighbour_cave(self, neighbour_cave: 'Cave'):
        if not neighbour_cave in self.neighbours:
            self.neighbours.append(neighbour_cave)

    @property
    def is_small(self) -> bool:
        return self.name.islower()


def get_paths(caves: dict[str, Cave], start: str = 'start', end: str = 'end', max_small_visits_allowed: int = 1) -> list[list[Cave]]:
    paths_found: list[list[Cave]] = []
    current_search_paths: list[list[Cave]] = [[caves[start]]]
    while current_search_paths:
        current_path = current_search_paths.pop()
        current_cave = current_path[-1]
        for nc in current_cave.neighbours:
            if nc.name == end:
                paths_found.append(current_path + [nc])
                continue
            if nc.name == start:
                continue
            times_nc_is_visited = sum(1 for x in current_path if x == nc)
            other_small_visits = max(sum(1 for x in current_path if x == y)
                                     for y in current_path if y.is_small and y != nc)
            if nc.is_small and times_nc_is_visited == max_small_visits_allowed:
                continue
            if max_small_visits_allowed > 1 and nc.is_small and times_nc_is_visited == max_small_visits_allowed - 1 and other_small_visits == max_small_visits_allowed:
                continue
            current_search_paths.append(current_path + [nc])
    return paths_found


if __name__ == '__main__':
    caves: dict[str, Cave] = {}
    with open("2021/12.txt", 'r') as f:
        cave_data = [t.strip().split('-') for t in f.readlines()]
        for c1, c2 in cave_data:
            if c1 not in caves:
                caves[c1] = Cave(c1)
            if c2 not in caves:
                caves[c2] = Cave(c2)
            caves[c1].add_neighbour_cave(caves[c2])
            caves[c2].add_neighbour_cave(caves[c1])

    print('part1:', len(get_paths(caves)))
    print('part2:', len(get_paths(caves, max_small_visits_allowed=2)))
