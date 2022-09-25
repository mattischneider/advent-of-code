def get_wrapping_paper_size(package_dimension: str) -> int:
    l, w, h = (int(d) for d in package_dimension.strip().split("x"))
    smallest_side_area = min(l * w, w * h, h * l)
    surface_area = 2 * l * w + 2 * w * h + 2 * h * l
    return surface_area + smallest_side_area


def test_get_wrapping_paper_size():
    assert get_wrapping_paper_size("2x3x4") == 58
    assert get_wrapping_paper_size("1x1x10") == 43


def get_package_ribbon(package_dimension: str) -> int:
    s1, s2, _ = sorted(int(d) for d in package_dimension.strip().split("x"))
    return 2 * s1 + 2 * s2


def test_get_package_ribbon():
    assert get_package_ribbon("2x3x4") == 10
    assert get_package_ribbon("1x1x10") == 4


def get_bow_ribbon(package_dimension: str) -> int:
    l, w, h = (int(d) for d in package_dimension.strip().split("x"))
    return l * w * h


def test_get_bow_ribbon():
    assert get_bow_ribbon("2x3x4") == 24
    assert get_bow_ribbon("1x1x10") == 10


def get_total_ribbon(package_dimension: str) -> int:
    return get_package_ribbon(package_dimension) + get_bow_ribbon(package_dimension)


def test_get_total_ribbon():
    assert get_total_ribbon("2x3x4") == 34
    assert get_total_ribbon("1x1x10") == 14


def main():
    with open("2015/02_input", "r") as f:
        package_sizes = f.readlines()
        assert len(package_sizes) == 1000
    total_packages_size = sum(get_wrapping_paper_size(p) for p in package_sizes)
    print("part1", total_packages_size)
    total_ribbon = sum(get_total_ribbon(p) for p in package_sizes)
    print("part2", total_ribbon)


if __name__ == "__main__":
    main()
