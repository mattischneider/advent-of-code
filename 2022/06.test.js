let aoc = require("./06.js");

test("test bvwbjplbgvbhsrlpgdmjqwftvncz", () => {
  expect(aoc.getFirstMarker("bvwbjplbgvbhsrlpgdmjqwftvncz", 4)).toBe(5);
});

test("test nppdvjthqldpwncqszvftbrmjlhg", () => {
  expect(aoc.getFirstMarker("nppdvjthqldpwncqszvftbrmjlhg", 4)).toBe(6);
});

test("test nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", () => {
  expect(aoc.getFirstMarker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4)).toBe(10);
});

test("test zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", () => {
  expect(aoc.getFirstMarker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4)).toBe(11);
});

test("test bvwbjplbgvbhsrlpgdmjqwftvncz", () => {
  expect(aoc.getFirstMarker("bvwbjplbgvbhsrlpgdmjqwftvncz", 14)).toBe(23);
});

test("test nppdvjthqldpwncqszvftbrmjlhg", () => {
  expect(aoc.getFirstMarker("nppdvjthqldpwncqszvftbrmjlhg", 14)).toBe(23);
});

test("test nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", () => {
  expect(aoc.getFirstMarker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14)).toBe(29);
});

test("test zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", () => {
  expect(aoc.getFirstMarker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14)).toBe(26);
});
