class ImageEnhancer:
    def __init__(self, input_string):
        self.step = 0
        self.algo, self.image = input_string.split("\n\n")
        self.algo: list[str] = self.algo.replace("\n", "")
        assert len(self.algo) == 512
        self.image: list[list[str]] = self.image.splitlines()
        assert len(self.image) == len(self.image[0])
        self.image = self.pad_image(".")

    @property
    def image_size(self) -> int:
        return len(self.image)

    @property
    def lit_pixels(self) -> int:
        return sum(1 for p in self.image for i in p if i == "#")

    def print_image(self) -> None:
        print(f"\nAfter {self.step} steps:")
        for p in self.image:
            print("".join(p))

    def pad_image(self, infinity_symbol) -> list[list[str]]:
        return (
            [infinity_symbol * (self.image_size + 2)]
            + [infinity_symbol + j + infinity_symbol for j in self.image]
            + [infinity_symbol * (self.image_size + 2)]
        )

    def get_9_neighbour_mark(self, idx: int, idy: int, infinity_symbol: str) -> str:
        max_s = self.image_size - 1
        i_sym = infinity_symbol
        top_row = [
            i_sym if idy == 0 or idx == 0 else self.image[idx - 1][idy - 1],
            i_sym if idx == 0 else self.image[idx - 1][idy],
            i_sym if idx == 0 or idy == max_s else self.image[idx - 1][idy + 1],
        ]
        mid_row = [
            i_sym if idy == 0 else self.image[idx][idy - 1],
            self.image[idx][idy],
            i_sym if idy == max_s else self.image[idx][idy + 1],
        ]
        bottom_row = [
            i_sym if idx == max_s or idy == 0 else self.image[idx + 1][idy - 1],
            i_sym if idx == max_s else self.image[idx + 1][idy],
            i_sym if idx == max_s or idy == max_s else self.image[idx + 1][idy + 1],
        ]
        return "".join(top_row + mid_row + bottom_row)

    def apply_algo(self, mark: str) -> str:
        mark_int = int(mark.replace(".", "0").replace("#", "1"), 2)
        return self.algo[mark_int]

    def enhance(self) -> None:
        infinity_symbol = self.image[0][0]
        self.image = self.pad_image(infinity_symbol)
        self.step += 1
        self.image = [
            "".join(
                self.apply_algo(self.get_9_neighbour_mark(idx, idy, infinity_symbol))
                for idy in range(self.image_size)
            )
            for idx in range(self.image_size)
        ]


if __name__ == "__main__":
    with open("2021/20.txt", "r") as f:
        img_enh = ImageEnhancer(f.read())

    for i in range(50):
        img_enh.enhance()
        if i == 1:
            print("part1:", img_enh.lit_pixels)
        if i == 49:
            print("part2:", img_enh.lit_pixels)
