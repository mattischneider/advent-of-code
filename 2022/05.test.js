let aoc = require("./05.js");
let filename = "2022/05_testinput";

let testCrates = new aoc.StackOfCrates(aoc.getInitialCrateConfig(filename));
let testInstructions = aoc.getInstructions(filename);

test("test performInstructions", () => {
  testCrates.performInstructions(testInstructions, "9000");
  expect(testCrates.topOfStackMessage).toBe("CMZ");
});

let testCratesPart2 = new aoc.StackOfCrates(
  aoc.getInitialCrateConfig(filename)
);

test("test performInstructions", () => {
  testCratesPart2.performInstructions(testInstructions, "9001");
  expect(testCratesPart2.topOfStackMessage).toBe("MCD");
});
