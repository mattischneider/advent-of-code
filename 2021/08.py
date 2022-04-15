NUMBERS_MAPPING = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}


def get_decode_dict(signals: list[str]) -> dict[str, str]:
    for s in signals:
        if len(s) == 2:
            cf = {char for char in s}
        if len(s) == 3:
            acf = {char for char in s}
        if len(s) == 4:
            bcdf = {char for char in s}
        if len(s) == 7:
            abcdefg = {char for char in s}
    a = acf - cf
    zero_six_nine: list[set[str]] = [set(s) for s in signals if len(s) == 6]
    for possible_c in [cf - x for x in zero_six_nine]:
        if possible_c:
            c = possible_c
            break
    f = cf - c
    bd = bcdf - c - f
    for possible_d in [bd - x for x in zero_six_nine]:
        if possible_d:
            d = possible_d
            break
    b = bd - d
    eg = abcdefg - a - b - c - d - f
    for possible_e in [eg - x for x in zero_six_nine]:
        if possible_e:
            e = possible_e
            break
    g = eg - e
    return {
        list(a)[0]: "a",
        list(b)[0]: "b",
        list(c)[0]: "c",
        list(d)[0]: "d",
        list(e)[0]: "e",
        list(f)[0]: "f",
        list(g)[0]: "g",
    }


def decode_value(signal_value: str, decode_dict: dict[str, str]) -> int:
    decoded = [decode_dict[c] for c in signal_value]
    decoded.sort()
    return NUMBERS_MAPPING["".join(decoded)]


if __name__ == "__main__":
    with open("2021/08.txt", "r") as f:
        all_signals = [[s.strip().split(" ") for s in line.split(" | ")] for line in f.readlines()]
    print(
        "part1:",
        sum(sum(1 for a in x[1] if len(a) in [2, 3, 4, 7]) for x in all_signals),
    )

    final = 0
    for s in all_signals:
        decode_dict = get_decode_dict(s[0] + s[1])
        final += int("".join(decode_value(output, decode_dict) for output in s[1]))
    print("part2:", final)
