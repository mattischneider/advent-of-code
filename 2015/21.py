from dataclasses import dataclass
from itertools import combinations, product


@dataclass
class Player:
    hit_points: int
    damage: int
    armor: int


def simulate_game(you: Player, boss: Player) -> Player:
    attacker, defender = you, boss
    while True:
        defender.hit_points -= max(1, attacker.damage - defender.armor)
        if defender.hit_points <= 0:
            return attacker
        attacker, defender = defender, attacker


@dataclass
class Equipment:
    type: str
    name: str
    cost: int
    damage: int
    armor: int


def test_simulate_game():
    boss = Player(hit_points=12, damage=7, armor=2)
    you = Player(hit_points=8, damage=5, armor=5)
    assert simulate_game(you, boss) == you


def main():
    weapons_equipment = [
        Equipment(type="Weapon", name="Dagger", cost=8, damage=4, armor=0),
        Equipment(type="Weapon", name="Shortsword", cost=10, damage=5, armor=0),
        Equipment(type="Weapon", name="Warhammer", cost=25, damage=6, armor=0),
        Equipment(type="Weapon", name="Longsword", cost=40, damage=7, armor=0),
        Equipment(type="Weapon", name="Greataxe", cost=74, damage=8, armor=0),
    ]
    armor_equipment = [
        Equipment(type="Armor", name="Leather", cost=13, damage=0, armor=1),
        Equipment(type="Armor", name="Chainmail", cost=31, damage=0, armor=2),
        Equipment(type="Armor", name="Splintmail", cost=53, damage=0, armor=3),
        Equipment(type="Armor", name="Bandedmail", cost=75, damage=0, armor=4),
        Equipment(type="Armor", name="Platemail", cost=102, damage=0, armor=5),
        Equipment(type="Armor", name="nothing", cost=0, damage=0, armor=0),
    ]
    ring_equipment = [
        Equipment(type="Ring", name="Damage +1", cost=25, damage=1, armor=0),
        Equipment(type="Ring", name="Damage +2", cost=50, damage=2, armor=0),
        Equipment(type="Ring", name="Damage +3", cost=100, damage=3, armor=0),
        Equipment(type="Ring", name="Defense +1", cost=20, damage=0, armor=1),
        Equipment(type="Ring", name="Defense +2", cost=40, damage=0, armor=2),
        Equipment(type="Ring", name="Defense +3", cost=80, damage=0, armor=3),
        Equipment(type="Ring", name="no ring 1", cost=0, damage=0, armor=0),
        Equipment(type="Ring", name="no ring 2", cost=0, damage=0, armor=0),
    ]
    current_min_cost = (
        max(w.cost for w in weapons_equipment)
        + max(a.cost for a in armor_equipment)
        + 2 * max(r.cost for r in ring_equipment)
    )  # upper bound
    current_max_cost = 0
    for weapon, armor, rings in product(
        weapons_equipment, armor_equipment, combinations(ring_equipment, 2)
    ):
        # part 1
        costs = weapon.cost + armor.cost + sum(r.cost for r in rings)
        boss = Player(hit_points=104, damage=8, armor=1)
        you = Player(
            hit_points=100,
            damage=weapon.damage + sum(r.damage for r in rings),
            armor=armor.armor + sum(r.armor for r in rings),
        )
        if simulate_game(you, boss) == you and costs < current_min_cost:
            current_min_cost = costs

        # part 2
        boss = Player(hit_points=104, damage=8, armor=1)
        you = Player(
            hit_points=100,
            damage=weapon.damage + sum(r.damage for r in rings),
            armor=armor.armor + sum(r.armor for r in rings),
        )
        if simulate_game(you, boss) == boss and costs > current_max_cost:
            current_max_cost = costs

    print("part1:", current_min_cost)
    print("part2:", current_max_cost)


if __name__ == "__main__":
    main()
