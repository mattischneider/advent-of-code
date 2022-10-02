import parse

TICKER_TAPE = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def sue_confirms_to_ticker_tape(about_sue: str, version: int = 1) -> bool:
    version_2_attrs_gt = ["cats", "trees"]
    version_2_attrs_lt = ["pomeranians", "goldfish"]
    v2_attrs = version_2_attrs_gt + version_2_attrs_lt
    for a in about_sue.split(", "):
        attr, val = a.split(":")
        if (version == 1 or attr not in v2_attrs) and TICKER_TAPE[attr] != int(val):
            return False
        if version == 2 and attr in version_2_attrs_gt and TICKER_TAPE[attr] >= int(val):
            return False
        if version == 2 and attr in version_2_attrs_lt and TICKER_TAPE[attr] <= int(val):
            return False
    return True


def main():
    with open("2015/16_input", "r") as f:
        aunts_raw = f.read().splitlines()
    aunts_parsed = [parse.parse("Sue {sue_number:d}: {about_sue}", d) for d in aunts_raw]
    for aunt in aunts_parsed:
        if sue_confirms_to_ticker_tape(aunt["about_sue"]):
            print("part1:", aunt["sue_number"])
        if sue_confirms_to_ticker_tape(aunt["about_sue"], version=2):
            print("part2:", aunt["sue_number"])


if __name__ == "__main__":
    main()
