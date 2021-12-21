from dataclasses import dataclass


@dataclass
class Player:
    position: int
    score: int = 0


def play_game1(start_pos1: int, start_pos2: int) -> int:
    players = [Player(start_pos1), Player(start_pos2)]
    current_dice = 1
    round = 1
    current_player = 0

    while True:
        other_player = (current_player + 1) % 2
        tmp_sum = sum((current_dice + i) % 100 or 100 for i in range(3))
        players[current_player].position = (
            players[current_player].position + tmp_sum) % 10 or 10
        players[current_player].score += players[current_player].position

        if players[current_player].score >= 1000:
            return (3*round) * players[other_player].score

        # next round
        current_dice = (current_dice + 3) % 100 or 100
        round += 1
        current_player = other_player


if __name__ == '__main__':
    print('part1:', play_game1(3, 5))
