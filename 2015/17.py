from itertools import chain, combinations


def powerset(iterable):  # https://docs.python.org/3/library/itertools.html#itertools-recipes
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s) + 1))


def get_num_of_bucket_combinations(target: int, bucket_sizes: list[int]) -> int:
    return sum(1 for p in powerset(bucket_sizes) if sum(p) == target)


def test_get_num_of_bucket_combinations():
    assert get_num_of_bucket_combinations(25, [20, 15, 10, 5, 5]) == 4


def get_min_bucket_combinations(target: int, bucket_sizes: list[int]) -> int:
    return min(len(p) for p in powerset(bucket_sizes) if sum(p) == target)


def test_get_min_bucket_combinations():
    assert get_min_bucket_combinations(25, [20, 15, 10, 5, 5]) == 2


def get_num_of_bucket_combinations_with_min_config(target: int, bucket_sizes: list[int]) -> int:
    min_num_of_buckets = get_min_bucket_combinations(target, bucket_sizes)
    return sum(
        1 for p in powerset(bucket_sizes) if sum(p) == target and len(p) == min_num_of_buckets
    )


def test_get_num_of_bucket_combinations_with_min_configs():
    assert get_num_of_bucket_combinations_with_min_config(25, [20, 15, 10, 5, 5]) == 3


def main():
    target = 150
    bucket_sizes = [33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13, 50, 44, 48, 6, 24, 41, 30, 42]
    print("part1:", get_num_of_bucket_combinations(target, bucket_sizes))
    print("part2:", get_num_of_bucket_combinations_with_min_config(target, bucket_sizes))


if __name__ == "__main__":
    main()
