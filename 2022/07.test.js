let aoc = require("./07.js");
let filename = "2022/07_input_test";

let tree = aoc.parseTerminalOutput(filename);

test("test part1", () => {
  expect(tree.part1(100000)).toBe(95437);
});

test("test totalSpace", () => {
  expect(tree.totalSpace).toBe(48381165);
});

test("test dirs", () => {
  for (let i = 0; i < tree.length; i++) {
    const element = tree[i];

    if ((element.name = "d")) {
      expect(element.totalSizeOfFolder).toBe(24933642);
    }
    if ((element.name = "e")) {
      expect(element.totalSizeOfFolder).toBe(584);
    }
    if ((element.name = "/")) {
      expect(element.totalSizeOfFolder).toBe(48381165);
    }
    if ((element.name = "a")) {
      expect(element.totalSizeOfFolder).toBe(94853);
    }
  }
});

test("test findSmallestDirToDelete", () => {
  expect(tree.findSmallestDirToDelete(70000000, 30000000)).toBe(24933642);
});
