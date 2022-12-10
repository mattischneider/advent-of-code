let aoc = require("./04.js");

let testAssignments = aoc.getAssignmentPairs("2022/04_test");

test("test getNumberOfContainments", () => {
  expect(aoc.getNumberOfContainments(testAssignments)).toBe(2);
});

test("test getNumberOfOverlapSections", () => {
  expect(aoc.getNumberOfOverlapSections(testAssignments)).toBe(4);
});
