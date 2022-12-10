let aoc = require("./03.js");

let testRucksackItems = aoc.getRucksackItems("2022/03_test");
let testRucksackGroups = aoc.getRucksackGroups(testRucksackItems);

test("test getCommonRucksackItem", () => {
  expect(aoc.getCommonRucksackItem("vJrwpWtwJgWrhcsFMMfFFhFp")).toBe("p");
});

test("test getTotalPriority", () => {
  expect(aoc.getTotalPriority(testRucksackItems)).toBe(157);
});

test("test findGroupBadge", () => {
  expect(aoc.findGroupBadge(testRucksackGroups[0])).toBe("r");
  expect(aoc.findGroupBadge(testRucksackGroups[1])).toBe("Z");
});

test("test getSumOfPriorities", () => {
  expect(aoc.getSumOfPriorities(testRucksackItems)).toBe(70);
});
