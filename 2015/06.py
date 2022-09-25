from collections import defaultdict

import parse


class HouseDecoration:
    def __init__(self):
        self.lights = defaultdict(bool)
        self.brightness = defaultdict(int)

    def perform_instruction(self, instruction: str) -> None:
        p = parse.parse("{command} {xx:d},{yx:d} through {xy:d},{yy:d}", instruction)

        for x in range(p["xx"], p["xy"] + 1):
            for y in range(p["yx"], p["yy"] + 1):
                if p["command"] == "turn on":
                    self.lights[(x, y)] = True
                    self.brightness[(x, y)] += 1
                if p["command"] == "turn off":
                    self.lights[(x, y)] = False
                    self.brightness[(x, y)] = max(0, self.brightness[(x, y)] - 1)
                if p["command"] == "toggle":
                    self.lights[(x, y)] = not self.lights[(x, y)]
                    self.brightness[(x, y)] += 2

    @property
    def lights_on(self):
        return sum(1 for d in self.lights if self.lights[d] is True)

    @property
    def total_brightness(self):
        return sum(self.brightness[d] for d in self.brightness)


def test_house():
    hd = HouseDecoration()
    hd.perform_instruction("turn off 0,0 through 2,2")
    assert hd.lights_on == 0
    assert hd.total_brightness == 0
    hd.perform_instruction("turn on 0,0 through 999,999")
    assert hd.lights_on == 1000 * 1000
    assert hd.total_brightness == 1000 * 1000
    hd.perform_instruction("toggle 0,0 through 999,0")
    assert hd.lights_on == 1000 * 1000 - 1000
    assert hd.total_brightness == 1000 * 1000 + 2 * 1000
    hd.perform_instruction("turn off 499,499 through 500,500")
    assert hd.lights_on == 1000 * 1000 - 1000 - 4
    assert hd.total_brightness == 1000 * 1000 + 2 * 1000 - 4


def main():
    with open("2015/06_input", "r") as f:
        instructions = f.read().splitlines()
        assert len(instructions) == 300
    hd = HouseDecoration()
    for instr in instructions:
        hd.perform_instruction(instr)
    print("part1:", hd.lights_on)
    print("part2:", hd.total_brightness)


if __name__ == "__main__":
    main()
