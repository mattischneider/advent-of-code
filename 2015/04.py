import hashlib


def find_lowest_number(hash: str, number_with_zeros: int = 5) -> int:
    i = 1
    while True:
        result = hashlib.md5(f"{hash}{i}".encode("utf-8"))
        if result.hexdigest().startswith("0" * number_with_zeros):
            return i
        i += 1


def test_find_lowest_number():
    assert find_lowest_number("abcdef") == 609043
    assert find_lowest_number("abcdef", 6) == 6742839
    assert find_lowest_number("pqrstuv") == 1048970


def main():
    print("part1:", find_lowest_number("yzbqklnj"))
    print("part2:", find_lowest_number("yzbqklnj", 6))


if __name__ == "__main__":
    main()
