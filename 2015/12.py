import json


def get_sum_of_all_values(dat: int | list | dict, ignore_red=False) -> int:
    if isinstance(dat, int):
        return dat
    if isinstance(dat, list):
        return sum(get_sum_of_all_values(d, ignore_red) for d in dat)
    if isinstance(dat, dict):
        if ignore_red and "red" in dat.values():
            return 0
        return sum(get_sum_of_all_values(d, ignore_red) for d in dat.values())
    return 0


def test_get_sum_of_all_values():
    assert get_sum_of_all_values([1, 2, 3]) == 6
    assert get_sum_of_all_values([1, 2, 3], ignore_red=True) == 6
    assert get_sum_of_all_values([1, {"c": "red", "b": 2}, 3], ignore_red=True) == 4
    assert get_sum_of_all_values({"d": "red", "e": [1, 2, 3, 4], "f": 5}, ignore_red=True) == 0
    assert get_sum_of_all_values({"a": 2, "b": 4}) == 6
    assert get_sum_of_all_values([[[3]]]) == 3
    assert get_sum_of_all_values({"a": {"b": 4}, "c": -1}) == 3
    assert get_sum_of_all_values({"a": [-1, 1]}) == 0
    assert get_sum_of_all_values([-1, {"a": 1}]) == 0
    assert get_sum_of_all_values([]) == 0
    assert get_sum_of_all_values({}) == 0


def main():
    with open("2015/12_input", "r") as f:
        dat = json.load(f)
    print("part1:", get_sum_of_all_values(dat))
    print("part2:", get_sum_of_all_values(dat, ignore_red=True))


if __name__ == "__main__":
    main()
