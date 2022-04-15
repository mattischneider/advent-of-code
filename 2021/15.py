def get_lowest_risk_path(cave: list[str]) -> int:
    risk_levels = [[{"node_risk": int(c), "path_risk": None} for c in t.strip()] for t in cave]

    cave_size = len(risk_levels)
    start_node = (0, 0)
    target_node = (cave_size - 1, cave_size - 1)

    risk_levels[0][0]["path_risk"] = 0
    reachabled_nodes = {start_node}

    neighbours = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    # see https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    while target_node not in reachabled_nodes:

        current_min_path_risk = float("inf")
        for idx, idy in reachabled_nodes:
            if (pr := risk_levels[idx][idy]["path_risk"]) < current_min_path_risk:
                curren_min_path_pos = (idx, idy)
                current_min_path_risk = pr

        reachabled_nodes.remove(curren_min_path_pos)
        for idx, idy in neighbours:
            if not 0 <= curren_min_path_pos[0] + idx < cave_size:
                continue
            if not 0 <= curren_min_path_pos[1] + idy < cave_size:
                continue

            neighbour_x = curren_min_path_pos[0] + idx
            neighbour_y = curren_min_path_pos[1] + idy
            risk_to_neighbour_from_current = (
                risk_levels[neighbour_x][neighbour_y]["node_risk"] + current_min_path_risk
            )
            curren_neighbour_path_risk = risk_levels[neighbour_x][neighbour_y]["path_risk"]

            if curren_neighbour_path_risk is None:
                reachabled_nodes.add((neighbour_x, neighbour_y))

            if (
                curren_neighbour_path_risk is None
                or curren_neighbour_path_risk > risk_to_neighbour_from_current
            ):
                risk_levels[neighbour_x][neighbour_y]["path_risk"] = risk_to_neighbour_from_current
    return risk_levels[target_node[0]][target_node[1]]["path_risk"]


def extend_cave(cave: list[str], times=5) -> list[str]:
    cave_size = len(cave)
    cave_risks = [[int(c) for c in t.strip()] for t in cave]
    new_cave = [[float("inf") for _ in range(times * cave_size)] for _ in range(times * cave_size)]

    for idx in range(times * cave_size):
        for idy in range(times * cave_size):
            if idx < cave_size and idy < cave_size:  # original cave
                new_cave[idx][idy] = cave_risks[idx][idy]
                continue
            extended_node_risk = (
                cave_risks[idx % cave_size][idy % cave_size] + idx // cave_size + idy // cave_size
            )
            if extended_node_risk > 9:
                new_cave[idx][idy] = 1 + extended_node_risk % 10
            else:
                new_cave[idx][idy] = extended_node_risk

    return ["".join(str(d) for d in c) for c in new_cave]


if __name__ == "__main__":
    with open("2021/15.txt", "r") as f:
        cave = f.readlines()

    print("part1:", get_lowest_risk_path(cave))
    print("part2:", get_lowest_risk_path(extend_cave(cave)))
