import string
from itertools import groupby


def is_valid_password(password: str) -> bool:
    invalid_chars = ["i", "o", "l"]
    if any(c in password for c in invalid_chars):
        return False
    increasing_letters = [string.ascii_lowercase[i : i + 3] for i in range(24)]
    if not any(c in password for c in increasing_letters):
        return False
    number_of_required_pairs = 2
    if sum(1 for _, group in groupby(password) if len(list(group)) >= 2) < number_of_required_pairs:
        return False
    return True


def test_is_valid_password():
    assert is_valid_password("hijklmmn") is False
    assert is_valid_password("abbceffg") is False
    assert is_valid_password("abbcegjk") is False
    assert is_valid_password("abcdffaa") is True
    assert is_valid_password("ghjaabcc") is True


def increase_password(password: str) -> str:
    reversed_pass = password[::-1]
    try:
        first_not_z = [c for c in reversed_pass if c != "z"][0]
    except IndexError:
        return "a" * len(password)
    inc_letter = string.ascii_lowercase[string.ascii_lowercase.index(first_not_z) + 1]

    g = groupby(reversed_pass)
    char, group = next(g)
    if char == "z":
        wrap_around = len(list(group))
    else:
        wrap_around = 0

    next_pass_rev = (
        "a" * wrap_around + inc_letter + reversed_pass[reversed_pass.index(first_not_z) + 1 :]
    )
    return next_pass_rev[::-1]


def test_increase_password():
    assert increase_password("xx") == "xy"
    assert increase_password("xz") == "ya"
    assert increase_password("ya") == "yb"
    assert increase_password("zz") == "aa"


def next_valid_password(password: str) -> str:
    while not is_valid_password(next_pass := increase_password(password)):
        password = next_pass
    return next_pass


def test_next_valid_password():
    assert next_valid_password("abcdefgh") == "abcdffaa"
    assert next_valid_password("ghijklmn") == "ghjaabcc"


def main():
    print("part1:", next_pass := next_valid_password("vzbxkghb"))
    print("part2:", next_valid_password(next_pass))


if __name__ == "__main__":
    main()
