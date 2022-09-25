def get_floor(directions: str) -> int:
    ups = sum(1 for d in directions if d == "(")
    downs = sum(1 for d in directions if d == ")")
    return ups - downs


def test_get_floor():
    assert get_floor("(())") == 0
    assert get_floor("(()(()(") == 3


def get_first_basement_entry(directions: str) -> int | None:
    current_floor = 0
    for idx, d in enumerate(directions):
        if d == "(":
            current_floor += 1
        if d == ")":
            current_floor -= 1
            if current_floor < 0:
                return idx + 1


def test_get_first_basement_entry():
    assert get_first_basement_entry(")") == 1
    assert get_first_basement_entry("()((") is None
    assert get_first_basement_entry("()())") == 5


def main():
    with open("2015/01_input", "r") as f:
        input_directions = f.readline()
    print("part1", get_floor(input_directions))
    print("part2", get_first_basement_entry(input_directions))


if __name__ == "__main__":
    main()
