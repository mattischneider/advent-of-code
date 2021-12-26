from dataclasses import dataclass


@dataclass
class SeaCucumber:
    x_pos: int
    y_pos: int
    type: str

    def move_one_step(self, map_size_x: int, map_size_y: int) -> None:
        if self.type == ">":
            self.y_pos = (self.y_pos + 1) % map_size_x
        if self.type == "v":
            self.x_pos = (self.x_pos + 1) % map_size_y


class SeaFloor:
    def __init__(self, init_string):
        self.step: int = 0
        self.map_size_y = len(init_string)
        self.map_size_x = len(init_string[0].strip())
        self.sea_cucumbers: list[SeaCucumber] = []
        for idx, i in enumerate(init_string):
            for idy, t in enumerate(i.strip()):
                if t != ".":
                    self.sea_cucumbers.append(SeaCucumber(idx, idy, t))

    def get_movable_cucumbers(self) -> list[SeaCucumber]:
        cucumber_to_move: list[SeaCucumber] = []

        free_positions = set(
            (idx, idy)
            for idx in range(self.map_size_y + 1)
            for idy in range(self.map_size_x + 1)
        )
        for c in self.sea_cucumbers:
            free_positions.remove((c.x_pos, c.y_pos))

        for c in self.sea_cucumbers:
            if (
                c.type == ">"
                and (c.x_pos, (c.y_pos + 1) % self.map_size_x) in free_positions
            ):
                cucumber_to_move.append(c)

        for c in cucumber_to_move:
            free_positions.remove((c.x_pos, (c.y_pos + 1) % self.map_size_x))
            free_positions.add((c.x_pos, c.y_pos))

        for c in self.sea_cucumbers:
            if (
                c.type == "v"
                and ((c.x_pos + 1) % self.map_size_y, c.y_pos) in free_positions
            ):
                cucumber_to_move.append(c)

        return cucumber_to_move

    def next_step(self):
        self.step += 1

        cucumber_to_move = self.get_movable_cucumbers()
        if not cucumber_to_move:
            return 1

        for c in cucumber_to_move:
            c.move_one_step(self.map_size_x, self.map_size_y)
        return 0

    def print_map(self):
        print(f"\nAfter {self.step} steps:")
        out = [["."] * self.map_size_x for _ in range(self.map_size_y)]
        for c in self.sea_cucumbers:
            out[c.x_pos][c.y_pos] = c.type
        for o in out:
            print("".join(o))


if __name__ == "__main__":
    with open("2021/25.txt", "r") as f:
        init_string = f.readlines()
    sf = SeaFloor(init_string)
    while not sf.next_step():
        pass
    print("part1:", sf.step)
