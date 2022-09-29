import parse


class Reindeer:
    def __init__(self, name: str, kms: int, how_long: int, rest_time: int):
        self.name = name
        self.kms = kms
        self.how_long = how_long
        self.rest_time = rest_time

    def fly_distance(self, travel_time: int) -> int:
        to_go = travel_time
        is_resting = False
        traveled_distance = 0
        while True:
            if not is_resting:
                traveled_distance += min(self.how_long, to_go) * self.kms
                to_go -= min(self.how_long, to_go)
                is_resting = True
            else:
                to_go -= self.rest_time
                is_resting = False

            if to_go <= 0:
                return traveled_distance


def test_reindeer():
    comet = Reindeer(name="Comet", kms=14, how_long=10, rest_time=127)
    assert comet.fly_distance(1) == 14
    assert comet.fly_distance(10) == 140
    assert comet.fly_distance(1000) == 1120
    dancer = Reindeer(name="Dancer", kms=16, how_long=11, rest_time=162)
    assert dancer.fly_distance(1) == 16
    assert dancer.fly_distance(10) == 160
    assert dancer.fly_distance(1000) == 1056


class ReindeerRace:
    def __init__(self, racers: list[Reindeer]):
        self.racers = racers

    def start_race(self, distance: int) -> tuple[int, int]:
        n = len(self.racers)
        race_points = [0 for _ in range(n)]
        for i in range(1, distance + 1):
            current_race_distances = [r.fly_distance(i) for r in self.racers]
            current_max_dist = max(current_race_distances)
            for j in range(n):
                race_points[j] += 1 if current_race_distances[j] == current_max_dist else 0
        return current_max_dist, max(race_points)


def test_race():
    comet = Reindeer(name="Comet", kms=14, how_long=10, rest_time=127)
    dancer = Reindeer(name="Dancer", kms=16, how_long=11, rest_time=162)
    race = ReindeerRace([comet, dancer])
    assert race.start_race(1000) == (1120, 689)


def main():
    with open("2015/14_input", "r") as f:
        deers_raw = f.read().splitlines()
    parsed_reindeer_vars = [
        parse.parse(
            "{name} can fly {kms:d} km/s for {how_long:d} seconds, but then must rest for {rest_time:d} seconds.",  # noqa: E501
            d,
        )
        for d in deers_raw
    ]
    reindeers = [
        Reindeer(name=d["name"], kms=d["kms"], how_long=d["how_long"], rest_time=d["rest_time"])
        for d in parsed_reindeer_vars
    ]
    race = ReindeerRace(reindeers)
    distance = 2503
    winning_dist, winning_score = race.start_race(distance)
    print("part1:", winning_dist)
    print("part2:", winning_score)


if __name__ == "__main__":
    main()
