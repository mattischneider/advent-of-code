def get_input(file_name) -> list[str]:
    with open(file_name, "r") as f:
        data = [line.strip() for line in f.readlines()]
    return data


def get_first_int(data_line: str, part: int = 1) -> int:
    for idx, d in enumerate(data_line):
        if part == 2 and data_line[idx:].startswith("one"):
            return 1
        if part == 2 and data_line[idx:].startswith("two"):
            return 2
        if part == 2 and data_line[idx:].startswith("three"):
            return 3
        if part == 2 and data_line[idx:].startswith("four"):
            return 4
        if part == 2 and data_line[idx:].startswith("five"):
            return 5
        if part == 2 and data_line[idx:].startswith("six"):
            return 6
        if part == 2 and data_line[idx:].startswith("seven"):
            return 7
        if part == 2 and data_line[idx:].startswith("eight"):
            return 8
        if part == 2 and data_line[idx:].startswith("nine"):
            return 9
        try:
            return int(d)
        except ValueError:
            continue


def get_last_int(data_line: str, part: int = 1) -> int:
    data_rev = data_line[::-1]
    for idx, d in enumerate(data_rev):
        if part == 2 and data_rev[idx:].startswith("one"[::-1]):
            return 1
        if part == 2 and data_rev[idx:].startswith("two"[::-1]):
            return 2
        if part == 2 and data_rev[idx:].startswith("three"[::-1]):
            return 3
        if part == 2 and data_rev[idx:].startswith("four"[::-1]):
            return 4
        if part == 2 and data_rev[idx:].startswith("five"[::-1]):
            return 5
        if part == 2 and data_rev[idx:].startswith("six"[::-1]):
            return 6
        if part == 2 and data_rev[idx:].startswith("seven"[::-1]):
            return 7
        if part == 2 and data_rev[idx:].startswith("eight"[::-1]):
            return 8
        if part == 2 and data_rev[idx:].startswith("nine"[::-1]):
            return 9
        try:
            return int(d)
        except ValueError:
            continue


def get_calibration_value(data_line: list[int], part: int = 1) -> int:
    first = get_first_int(data_line, part=part)
    last = get_last_int(data_line, part=part)
    return first * 10 + last


def get_sum_of_calibration_values(data, part: int = 1) -> int:
    return sum(get_calibration_value(data_line, part=part) for data_line in data)


def main():
    print(f"part1: {get_sum_of_calibration_values(get_input("2023/01_input"))}")
    print(f"part2: {get_sum_of_calibration_values(get_input("2023/01_input"), part=2)}")
    print(
        f"test part1: {get_sum_of_calibration_values(get_input("2023/01_test_input"))}"
    )
    print(
        f"test part2: {get_sum_of_calibration_values(get_input("2023/01_test_input2"), part=2)}"
    )


if __name__ == "__main__":
    main()
