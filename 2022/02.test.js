let aoc = require("./02.js");

let testGames = aoc.getGames("2022/02_test");

test("test getScore", () => {
  expect(aoc.getScore(testGames[0])).toBe(8);
  expect(aoc.getScore(testGames[1])).toBe(1);
  expect(aoc.getScore(testGames[2])).toBe(6);
});
test("test getTotalScore", () => {
  expect(aoc.getTotalScore(testGames)).toBe(15);
});

test("test adjustGameScore", () => {
  expect(aoc.adjustGameScore(testGames[0])).toBe(4);
  expect(aoc.adjustGameScore(testGames[1])).toBe(1);
  expect(aoc.adjustGameScore(testGames[2])).toBe(7);
});
test("test getTotalScorePart2", () => {
  expect(aoc.getTotalScorePart2(testGames)).toBe(12);
});
