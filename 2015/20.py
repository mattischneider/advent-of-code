def get_lowest_house(target: int, max_50_houses: bool = False) -> int:
    factor = 11 if max_50_houses else 10
    upper_bound = target // factor
    presents = [0] * upper_bound
    for i in range(1, upper_bound):
        tmp = i - 1
        count_to_50 = 1
        while tmp < upper_bound and not (max_50_houses and count_to_50 > 50):
            presents[tmp] += factor * i
            tmp += i
            count_to_50 += 1
        if presents[i - 1] >= target:
            return i
    return -1


def test_get_lowest_house():
    def _get_presents(house_number: int, factor: int = 10) -> int:
        return sum(factor * i for i in range(1, house_number + 1) if house_number % i == 0)

    assert _get_presents(1) == 10
    assert _get_presents(2) == 30
    assert _get_presents(3) == 40
    assert _get_presents(4) == 70
    assert _get_presents(5) == 60
    assert _get_presents(6) == 120
    assert _get_presents(7) == 80
    assert _get_presents(8) == 150
    assert _get_presents(9) == 130

    assert get_lowest_house(120) == 6
    assert get_lowest_house(119) == 6
    assert get_lowest_house(121) == 8

    assert _get_presents(1, 11) == 11
    assert _get_presents(2, 11) == 33
    assert _get_presents(3, 11) == 44
    assert _get_presents(4, 11) == 77
    assert _get_presents(5, 11) == 66
    assert _get_presents(6, 11) == 132
    assert _get_presents(7, 11) == 88
    assert _get_presents(8, 11) == 165
    assert _get_presents(9, 11) == 143

    assert get_lowest_house(132, True) == 6
    assert get_lowest_house(131, True) == 6
    assert get_lowest_house(133, True) == 8
    assert get_lowest_house(1000, True) == 36


def main():
    print("part1:", get_lowest_house(29_000_000))
    print("part2:", get_lowest_house(29_000_000, True))


if __name__ == "__main__":
    main()
