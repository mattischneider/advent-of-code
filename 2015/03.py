def get_visited_houses(directions: str):
    current_pos = (0, 0)
    visited_houses = {current_pos}
    for d in directions:
        x, y = current_pos
        if d == "^":
            current_pos = (x, y + 1)
        if d == "v":
            current_pos = (x, y - 1)
        if d == ">":
            current_pos = (x + 1, y)
        if d == "<":
            current_pos = (x - 1, y)
        visited_houses.add(current_pos)
    return visited_houses


def test_get_visited_houses():
    assert get_visited_houses(">v") == {(0, 0), (1, 0), (1, -1)}


def get_number_of_visited_houses(directions: str) -> int:
    return len(get_visited_houses(directions))


def test_get_number_of_visited_houses():
    assert get_number_of_visited_houses(">") == 2
    assert get_number_of_visited_houses("^>v<") == 4
    assert get_number_of_visited_houses("^v^v^v^v^v") == 2


def get_santa_and_robo_directions(directions: str) -> tuple[str, str]:
    robo_instr = "".join(d for idx, d in enumerate(directions) if idx % 2 == 1)
    santa_instr = "".join(d for idx, d in enumerate(directions) if idx % 2 == 0)
    return (santa_instr, robo_instr)


def test_get_santa_and_robo_directions():
    assert get_santa_and_robo_directions(">v") == (">", "v")
    assert get_santa_and_robo_directions("^>v<") == ("^v", "><")
    assert get_santa_and_robo_directions("^v^v^v^v^v") == ("^^^^^", "vvvvv")


def get_combined_houses(directions: str):
    santa_instr, robo_instr = get_santa_and_robo_directions(directions)
    return get_visited_houses(santa_instr) | get_visited_houses(robo_instr)


def test_get_combined_houses():
    assert get_combined_houses(">v") == {(0, 0), (1, 0), (0, -1)}


def get_combined_number_of_houses(directions: str):
    return len(get_combined_houses(directions))


def test_get_combined_number_of_houses():
    assert get_combined_number_of_houses("^v") == 3
    assert get_combined_number_of_houses("^>v<") == 3
    assert get_combined_number_of_houses("^v^v^v^v^v") == 11


def main():
    with open("2015/03_input", "r") as f:
        input_directions = f.readline()
    print("part1:", get_number_of_visited_houses(input_directions))
    print("part2:", get_combined_number_of_houses(input_directions))


if __name__ == "__main__":
    main()
