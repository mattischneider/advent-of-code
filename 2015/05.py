from collections import defaultdict


def has_double_letters(input_string: str) -> bool:
    prev_char = None
    for i in input_string:
        if i == prev_char:
            return True
        prev_char = i
    return False


def test_has_double_letters():
    assert has_double_letters("ugknbfddgicrmopn") is True
    assert has_double_letters("aaa") is True
    assert has_double_letters("jchzalrnumimnmhp") is False
    assert has_double_letters("haegwjzuvuyypxyu") is True
    assert has_double_letters("dvszwmarrgswjxmb") is True


def contains_no_bad_string(input_string: str) -> bool:
    bad_strings = ("ab", "cd", "pq", "xy")
    return all(b not in input_string for b in bad_strings)


def test_contains_no_bad_string():
    assert contains_no_bad_string("ugknbfddgicrmopn") is True
    assert contains_no_bad_string("aaa") is True
    assert contains_no_bad_string("haegwjzuvuyypxyu") is False
    assert contains_no_bad_string("dvszwmarrgswjxmb") is True


def is_nice_string(input_string: str) -> bool:
    vowels = ("a", "e", "i", "o", "u")
    number_of_vowels = sum(1 for i in input_string if i in vowels)

    return (
        number_of_vowels >= 3
        and has_double_letters(input_string)
        and contains_no_bad_string(input_string)
    )


def test_is_nice_string():
    assert is_nice_string("ugknbfddgicrmopn") is True
    assert is_nice_string("aaa") is True
    assert is_nice_string("jchzalrnumimnmhp") is False
    assert is_nice_string("haegwjzuvuyypxyu") is False
    assert is_nice_string("dvszwmarrgswjxmb") is False


def contains_double_pair_with_no_overlap(input_string: str) -> bool:
    pairs = defaultdict(list)
    for idx in range(len(input_string) - 1):
        p = input_string[idx : (idx + 2)]
        if any(d != idx - 1 for d in pairs[p]):
            return True
        pairs[p].append(idx)
    return False


def test_contains_double_pair_with_no_overlap():
    assert contains_double_pair_with_no_overlap("xxy") is False
    assert contains_double_pair_with_no_overlap("aaa") is False
    assert contains_double_pair_with_no_overlap("aaaa") is True
    assert contains_double_pair_with_no_overlap("xyxy") is True
    assert contains_double_pair_with_no_overlap("aabcdefgaa") is True
    assert contains_double_pair_with_no_overlap("aaaxxxx") is True


def contains_one_repeating_letter_with_one_letter_in_betweens(input_string: str) -> bool:
    return any(input_string[idx] == input_string[idx + 2] for idx in range(len(input_string) - 2))


def test_contains_one_repeating_letter_with_one_letter_in_betweens():
    assert contains_one_repeating_letter_with_one_letter_in_betweens("xyx") is True
    assert contains_one_repeating_letter_with_one_letter_in_betweens("abcdefeghi") is True
    assert contains_one_repeating_letter_with_one_letter_in_betweens("aaa") is True
    assert contains_one_repeating_letter_with_one_letter_in_betweens("aax") is False
    assert contains_one_repeating_letter_with_one_letter_in_betweens("fganrbnplymqbzjx") is False


def is_nice_string_with_new_rules(input_string: str) -> bool:
    return contains_double_pair_with_no_overlap(
        input_string
    ) and contains_one_repeating_letter_with_one_letter_in_betweens(input_string)


def test_is_nice_string_with_new_rules():
    assert is_nice_string_with_new_rules("qjhvhtzxzqqjkmpb") is True
    assert is_nice_string_with_new_rules("xxyxx") is True
    assert is_nice_string_with_new_rules("uurcxstgmygtbstg") is False
    assert is_nice_string_with_new_rules("ieodomkazucvgmuy") is False


def main():
    with open("2015/05_input", "r") as f:
        input_strings = f.readlines()
        assert len(input_strings) == 1000
    total_nice_strings = sum(1 for d in input_strings if is_nice_string(d.strip()) is True)
    print("part1:", total_nice_strings)
    total_nice_strings_new_rules = sum(
        1 for d in input_strings if is_nice_string_with_new_rules(d.strip()) is True
    )
    print("part2:", total_nice_strings_new_rules)


if __name__ == "__main__":
    main()
