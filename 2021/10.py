OPEN_CLOSE_MAPPING = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}
ILLEGAL_POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
OPEN_BRACKETS_POINTS = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}


class Line:
    def __init__(self, text: str):
        self.text = text

    def get_first_illegal_char_point(self) -> int:
        char_stack = []
        for c in self.text:
            if c in OPEN_BRACKETS_POINTS.keys():
                char_stack.append(c)
            else:
                if len(char_stack) > 0 and char_stack[-1] == OPEN_CLOSE_MAPPING[c]:
                    char_stack.pop()
                else:
                    return ILLEGAL_POINTS[c]
        return 0

    @property
    def is_corrupted(self) -> bool:
        return self.get_first_illegal_char_point() > 0

    def get_score_for_incomplete_lines(self):
        char_stack = []
        for c in self.text:
            if c in OPEN_BRACKETS_POINTS.keys():
                char_stack.append(c)
            else:
                if len(char_stack) > 0 and char_stack[-1] == OPEN_CLOSE_MAPPING[c]:
                    char_stack.pop()
        score = 0
        char_stack.reverse()
        for c in char_stack:
            score *= 5
            score += OPEN_BRACKETS_POINTS[c]
        return score


if __name__ == "__main__":
    with open("2021/10.txt", "r") as f:
        lines = [Line(line.strip()) for line in f.readlines()]

    print("part1:", sum(line.get_first_illegal_char_point() for line in lines))

    scores = [line.get_score_for_incomplete_lines() for line in lines if not line.is_corrupted]
    scores.sort()
    print("part2:", scores[len(scores) // 2])
