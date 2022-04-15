import math

import parse


class Probe:
    def __init__(
        self,
        start_x_velocity: int,
        start_y_velocity: int,
        target_x_from: int,
        target_x_to: int,
        target_y_from: int,
        target_y_to: int,
    ):
        self.location = [0, 0]
        self.x_velocity = start_x_velocity
        self.y_velocity = start_y_velocity

        self.target_x_from = target_x_from
        self.target_x_to = target_x_to
        self.target_y_from = target_y_from
        self.target_y_to = target_y_to

        self.max_y = 0
        self.target_hit = False

    def next_step(self) -> None:
        self.location[0] += self.x_velocity
        self.location[1] += self.y_velocity

        if self.x_velocity > 0:
            self.x_velocity -= 1
        self.y_velocity -= 1

        if self.location[1] > self.max_y:
            self.max_y = self.location[1]

        if (
            self.target_x_from <= self.location[0] <= self.target_x_to
            and self.target_y_from <= self.location[1] <= self.target_y_to
        ):
            self.target_hit = True

    def shoot(self) -> None:
        while self.location[0] <= self.target_x_to and self.location[1] >= self.target_y_from:
            self.next_step()


if __name__ == "__main__":
    with open("2021/17.txt", "r") as f:
        input = parse.parse(
            "target area: x={x_from:d}..{x_to:d}, y={y_from:d}..{y_to:d}",
            f.readline().strip(),
        )

    current_max_y = 0
    target_hits = 0

    x_range_start = int(1 / 2 * (1 + math.sqrt(8 * input["x_from"] + 1)))
    x_range_end = input["x_to"] + 1
    y_range_start = input["y_from"]
    y_range_end = -(input["y_to"] + input["y_from"]) + 1

    for x_velo in range(x_range_start, x_range_end):
        for y_velo in range(y_range_start, y_range_end):
            t = Probe(
                x_velo,
                y_velo,
                input["x_from"],
                input["x_to"],
                input["y_from"],
                input["y_to"],
            )
            t.shoot()
            if t.target_hit is True:
                target_hits += 1
                if t.max_y > current_max_y:
                    current_max_y = t.max_y

    print("part1:", current_max_y)
    print("part2:", target_hits)
