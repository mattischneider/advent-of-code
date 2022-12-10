let aoc = require("./01.js");

let testElves = aoc.getSortedElvCalories("2022/01_test");

test("test getSortedElvCalories", () => {
  let expected = Int32Array.from([24000, 11000, 10000, 6000, 4000]);
  expect(testElves).toEqual(expected);
});

test("test getSortedElvCalories", () => {
  expect(aoc.getMaxCalories(testElves)).toBe(24000);
});

test("test getTop3CaloriesSum", () => {
  expect(aoc.getTop3CaloriesSum(testElves)).toBe(45000);
});
