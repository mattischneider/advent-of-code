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

    def print_image(self):
        print(f"\nAfter {self.step} steps:")
        for p in self.image:
            print("".join(p))

    def pad_image(self, infinity_symbol):
        return (
            [infinity_symbol * (self.image_size + 2)]
            + [infinity_symbol + j + infinity_symbol for j in self.image]
            + [infinity_symbol * (self.image_size + 2)]
        )

    def unpad_image(self):
        return [
            j[1 : (self.image_size - 1)] for j in self.image[1 : (self.image_size - 1)]
        ]

    def get_9_neighbour_mark(self, idx, idy):
        t1 = "." if idy == 0 or idx == 0 else self.image[idx - 1][idy - 1]
        t2 = "." if idx == 0 else self.image[idx - 1][idy]
        t3 = (
            "."
            if idx == 0 or idy == self.image_size - 1
            else self.image[idx - 1][idy + 1]
        )
        m1 = "." if idy == 0 else self.image[idx][idy - 1]
        m2 = self.image[idx][idy]
        m3 = "." if idy == self.image_size - 1 else self.image[idx][idy + 1]
        b1 = (
            "."
            if idx == self.image_size - 1 or idy == 0
            else self.image[idx + 1][idy - 1]
        )
        b2 = "." if idx == self.image_size - 1 else self.image[idx + 1][idy]
        b3 = (
            "."
            if idx == self.image_size - 1 or idy == self.image_size - 1
            else self.image[idx + 1][idy + 1]
        )
        return t1 + t2 + t3 + m1 + m2 + m3 + b1 + b2 + b3

    def apply_algo(self, mark) -> str:
        mark_int = int(mark.replace(".", "0").replace("#", "1"), 2)
        return self.algo[mark_int]

    def enhance(self):
        self.image = self.pad_image(self.image[0][0])
        self.image = self.pad_image(self.image[0][0])
        self.step += 1
        out = self.image.copy()
        for idx in range(self.image_size):
            tmp = ""
            for idy in range(self.image_size):
                mark = self.get_9_neighbour_mark(idx, idy)
                tmp += self.apply_algo(mark)
            out[idx] = tmp
        self.image = out
        self.image = self.unpad_image()
        pass

    @property
    def lit_pixels(self):
        return sum(1 for p in self.image for i in p if i == "#")


if __name__ == "__main__":
    with open("2021/20.txt", "r") as f:
        img_enh = ImageEnhancer(f.read())

    for i in range(50):
        img_enh.enhance()
        if i == 1:
            print("part1:", img_enh.lit_pixels)
        if i == 49:
            print("part2:", img_enh.lit_pixels)
