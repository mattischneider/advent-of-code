class BingoBoard:
    def __init__(self, raw_board: str):
        _splitted = raw_board.split('\n')
        self.board = [[int(i) for i in j.split(' ') if i != '']
                      for j in _splitted if j != '']
        self.size = len(self.board)
        self.drawn_numbers = [
            [0 for _ in range(self.size)] for _ in range(self.size)]
        self.currently_drawn = None

    def draw(self, number: int):
        self.currently_drawn = number
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == number:
                    self.drawn_numbers[i][j] = 1

    @property
    def is_solved(self):
        hor = [sum(j) for j in self.drawn_numbers]
        vert = [sum(i[j] for i in self.drawn_numbers)
                for j in range(self.size)]
        return (
            any(j == self.size for j in hor) or
            any(j == self.size for j in vert)
        )

    @property
    def score(self):
        unmarked = sum(self.board[i][j] for i in range(self.size)
                       for j in range(self.size) if self.drawn_numbers[i][j] == 0)
        return unmarked * self.currently_drawn


if __name__ == '__main__':
    with open("04.txt", 'r') as f:
        input_numbers = [int(n) for n in f.readline().split(',')]
        raw_bingo_boards = f.read().split('\n\n')

    boards = [BingoBoard(r) for r in raw_bingo_boards]
    winner_boards = []
    winner_board_scores = []
    for number in input_numbers:
        #print(f'draw number: {number}')
        for board in boards:
            board.draw(number)
            if board.is_solved and board not in winner_boards:
                winner_boards.append(board)
                winner_board_scores.append(board.score)

    print('part1:', winner_board_scores[0])
    print('part2:', winner_board_scores[-1])
