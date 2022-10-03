from functools import reduce

import parse


def get_parsed_replacement_rules(rules: list[str]) -> list[dict[str, str]]:
    output = []
    for r in rules:
        parsed = parse.parse("{from} => {to}", r)
        output.append({"from": parsed["from"], "to": parsed["to"]})
    return output


def get_all_replacements_with_one_step(rules: list[dict[str, str]], start: str) -> set[str]:
    output = set()
    for idx in range(len(start)):
        for r in rules:
            if start[idx:].startswith(r["from"]):
                output.add("".join(start[:idx] + start[idx:].replace(r["from"], r["to"], 1)))
    return output


def read_file(filename) -> tuple[list[dict[str, str]], str]:
    with open(filename, "r") as f:
        rules, start = f.read().split("\n\n")
        rules = rules.splitlines()
        start = start.strip()
    get_rules = get_parsed_replacement_rules(rules)
    return get_rules, start


def min_replacements(from_molecule: str, to_molecule: str, rules: list[dict[str, str]]) -> int:
    reverse_rules = [{"from": r["to"], "to": r["from"]} for r in rules]
    next = get_all_replacements_with_one_step(reverse_rules, to_molecule)
    output = 1
    while from_molecule not in next:
        output += 1
        next = reduce(
            lambda a, b: a | b, [get_all_replacements_with_one_step(reverse_rules, s) for s in next]
        )
        next = set(list(next)[0:100])  # well.. meh. what can you do.
    return output


def test():
    filename = "2015/19_test"
    get_rules, start = read_file(filename)
    assert get_rules == [
        {"from": "H", "to": "HO"},
        {"from": "H", "to": "OH"},
        {"from": "O", "to": "HH"},
    ]
    assert get_all_replacements_with_one_step(get_rules, start) == {
        "HOOH",
        "HOHO",
        "OHOH",
        "HOOH",
        "HHHH",
    }
    assert len(get_all_replacements_with_one_step(get_rules, start)) == 4
    part2_rules = [
        {"from": "e", "to": "H"},
        {"from": "e", "to": "O"},
        {"from": "H", "to": "HO"},
        {"from": "H", "to": "OH"},
        {"from": "O", "to": "HH"},
    ]
    assert min_replacements("e", "HOH", part2_rules) == 3
    assert min_replacements("e", "HOHOHO", part2_rules) == 6


def main():
    filename = "2015/19_input"
    get_rules, start = read_file(filename)
    print("part1:", len(get_all_replacements_with_one_step(get_rules, start)))
    print("part2:", min_replacements("e", start, get_rules))


if __name__ == "__main__":
    main()
