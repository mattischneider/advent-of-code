from dataclasses import dataclass
from itertools import product

import parse


@dataclass
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


class CookieRecipe:
    def __init__(self, ingredients: list[Ingredient]):
        self.ingredients = ingredients

    def get_score(self, ingredients_distribution: list[int]) -> int:
        capacity = max(
            sum(
                ingredient.capacity * ingredients_distribution[idx]
                for idx, ingredient in enumerate(self.ingredients)
            ),
            0,
        )
        durability = max(
            sum(
                ingredient.durability * ingredients_distribution[idx]
                for idx, ingredient in enumerate(self.ingredients)
            ),
            0,
        )
        flavor = max(
            sum(
                ingredient.flavor * ingredients_distribution[idx]
                for idx, ingredient in enumerate(self.ingredients)
            ),
            0,
        )
        texture = max(
            sum(
                ingredient.texture * ingredients_distribution[idx]
                for idx, ingredient in enumerate(self.ingredients)
            ),
            0,
        )
        return capacity * durability * flavor * texture

    def get_calories(self, ingredients_distribution: list[int]) -> int:
        return sum(
            ingredient.calories * ingredients_distribution[idx]
            for idx, ingredient in enumerate(self.ingredients)
        )

    def get_best_score(self, target_calories: int | None = None) -> int:
        sum_ingredients = 100
        num_ingredients = len(self.ingredients)
        current_max_score = 0
        for ingredients_distribution in product(
            range(0, sum_ingredients + 1), repeat=num_ingredients
        ):
            if sum(ingredients_distribution) != sum_ingredients:
                continue
            if (
                target_calories
                and self.get_calories(list(ingredients_distribution)) != target_calories
            ):
                continue
            if (n := self.get_score(list(ingredients_distribution))) > current_max_score:
                current_max_score = n
        return current_max_score


def test_cookies():
    butterscotch = Ingredient(
        name="Butterscotch", capacity=-1, durability=-2, flavor=6, texture=3, calories=8
    )
    cinnamon = Ingredient(
        name="Cinnamon", capacity=2, durability=3, flavor=-2, texture=-1, calories=3
    )
    recipe = CookieRecipe([butterscotch, cinnamon])
    assert recipe.get_score([44, 56]) == 62842880
    assert recipe.get_score([100, 0]) == 0
    assert recipe.get_best_score() == 62842880
    assert recipe.get_best_score(500) == 57600000


def main():
    with open("2015/15_input", "r") as f:
        ingredients_raw = f.read().splitlines()
    ingredients_parsed = [
        parse.parse(
            "{name}: capacity {capacity:d}, durability {durability:d}, flavor {flavor:d}, texture {texture:d}, calories {calories:d}",  # noqa: E501
            d,
        )
        for d in ingredients_raw
    ]
    ingredients = [
        Ingredient(
            name=d["name"],
            capacity=d["capacity"],
            durability=d["durability"],
            flavor=d["flavor"],
            texture=d["texture"],
            calories=d["calories"],
        )
        for d in ingredients_parsed
    ]
    cookie_recipe = CookieRecipe(ingredients)
    print("part1:", cookie_recipe.get_best_score())
    print("part2:", cookie_recipe.get_best_score(500))


if __name__ == "__main__":
    main()
