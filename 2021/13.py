import parse


def fold(dots: list[list[int]], along_axis: str, coord: int) -> list[list[int]]:
    out = []
    if along_axis == "y":
        for x, y in dots:
            if y > coord:
                out.append((x, coord - (y - coord)))
            if y == coord:
                continue
            if y < coord:
                out.append((x, y))
    if along_axis == "x":
        for x, y in dots:
            if x > coord:
                out.append((coord - (x - coord), y))
            if x == coord:
                continue
            if x < coord:
                out.append((x, y))
    return out


def fold_all_instructions(
    dots: list[list[int]], fold_instructions: list[tuple[str, int]]
) -> list[list[int]]:
    out = dots
    first_fold = True
    for a, c in fold_instructions:
        out = fold(out, a, c)
        if first_fold:
            print("part1:", len(set(out)))
            first_fold = False
    return out


def print_dots(dots: list[list[int]]) -> None:
    size = max(x for x, _ in dots)
    print("part2:")
    for y in range(size):
        line = ["#" if (x, y) in dots else " " for x in range(size)]
        if "#" in line:
            print("".join(line))


if __name__ == "__main__":
    with open("2021/13.txt", "r") as f:
        dots_raw, fold_raw = f.read().split("\n\n")
        dot_positions = [[int(x) for x in t.split(",")] for t in dots_raw.split("\n")]
        fold_instructions = [
            (d["fold_direction"], d["fold_coord"])
            for d in parse.findall("fold along {fold_direction}={fold_coord:d}", fold_raw)
        ]

    fold_result = fold_all_instructions(dot_positions, fold_instructions)
    print_dots(fold_result)
