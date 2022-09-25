def get_number_of_code_chars(filename: str):
    with open(filename, "r") as f:
        instructions = f.read().splitlines()
    return sum(len(i) for i in instructions)


def test_get_number_of_code_chars():
    assert get_number_of_code_chars("2015/08_test") == 23


def get_number_of_chars_in_memory(filename: str):
    with open(filename, "r") as f:
        instructions = f.read().splitlines()
    return sum(len(eval(i)) for i in instructions)


def test_get_number_of_chars_in_memory():
    assert get_number_of_chars_in_memory("2015/08_test") == 11


def get_number_of_new_encoding(filename: str) -> int:
    with open(filename, "r") as f:
        instructions = f.read().splitlines()
    return sum(len(i) + 2 + i.count('"') + i.count("\\") for i in instructions)


def test_get_number_of_new_encoding():
    assert get_number_of_new_encoding("2015/08_test") == 42


def main():
    file_name = "2015/08_input"
    print("part1:", get_number_of_code_chars(file_name) - get_number_of_chars_in_memory(file_name))
    print("part2:", get_number_of_new_encoding(file_name) - get_number_of_code_chars(file_name))


if __name__ == "__main__":
    main()
