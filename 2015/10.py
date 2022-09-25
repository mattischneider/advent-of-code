from itertools import groupby


def look_and_say(number: str) -> str:
    return "".join(f"{len(list(group))}{digit}" for digit, group in groupby(number))


def test_look_and_say():
    assert look_and_say("1") == "11"
    assert look_and_say("11") == "21"
    assert look_and_say("21") == "1211"
    assert look_and_say("1211") == "111221"
    assert look_and_say("111221") == "312211"


def main():
    current_num = "1113222113"
    for _ in range(40):
        current_num = look_and_say(current_num)
    print("part1:", len(current_num))
    for _ in range(10):
        current_num = look_and_say(current_num)
    print("part2:", len(current_num))


if __name__ == "__main__":
    main()
