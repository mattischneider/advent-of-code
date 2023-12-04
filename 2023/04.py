from dataclasses import dataclass
import parse


@dataclass()
class CardGame:
    card_number: int
    my_numbers: list[int]
    winning_numbers: list[int]

    def get_my_winning_numbers(self) -> list[int]:
        return [i for i in self.my_numbers if i in self.winning_numbers]

    def get_count_of_winning_numbers(self) -> int:
        return len(self.get_my_winning_numbers())

    def get_number_of_points(self) -> int:
        num_of_winning_cards = len(self.get_my_winning_numbers())
        return 2 ** (num_of_winning_cards - 1) if num_of_winning_cards else 0


def get_card_games(file_name) -> list[CardGame]:
    with open(file_name, "r") as f:
        data = [line.strip() for line in f.readlines()]
    out = []
    for d in data:
        parsed = parse.parse(
            "Card{blanks}{card_number:d}: {winning_numbers_str} | {my_numbers_str}", d
        )
        winning_numbers = [
            int(d) for d in parsed["winning_numbers_str"].split(" ") if d != ""
        ]
        my_numbers = [int(d) for d in parsed["my_numbers_str"].split(" ") if d != ""]
        out.append(
            CardGame(
                card_number=parsed["card_number"],
                my_numbers=my_numbers,
                winning_numbers=winning_numbers,
            )
        )
    return out


def get_part1(card_games: list[CardGame]) -> int:
    return sum(c.get_number_of_points() for c in card_games)


def get_part2(card_games: list[CardGame]):
    out = [1 for _ in card_games]
    for idx, c in enumerate(card_games):
        for i in range(1, c.get_count_of_winning_numbers() + 1):
            out[idx + i] += out[idx]
    return sum(_ for _ in out)


def main():
    card_games = get_card_games("2023/04_test_input")
    part_1 = get_part1(card_games)
    part_2 = get_part2(card_games)
    print(f"test part1: {part_1} (should be 13)")
    print(f"test part2: {part_2} (should be 30)")

    card_games = get_card_games("2023/04_input")
    part_1 = get_part1(card_games)
    part_2 = get_part2(card_games)
    print(f"part1: {part_1} (should be 26218)")
    print(f"part2: {part_2} (should be 9997537)")


if __name__ == "__main__":
    main()
