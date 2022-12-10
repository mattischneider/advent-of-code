var fs = require("fs");

function getSortedElvCalories(filename) {
  var data = fs.readFileSync(filename, "utf8");
  let elvFoods = data.split("\n\n");
  let elvCalories = elvFoods.map((i) =>
    i
      .split("\n")
      .map((numStr) => parseInt(numStr))
      .reduce((a, b) => a + b)
  );
  let typedElvCalories = Int32Array.from(elvCalories);
  return typedElvCalories.sort().reverse();
}

function getMaxCalories(sorted_elvCalories) {
  return sorted_elvCalories[0];
}

function getTop3CaloriesSum(sorted_elvCalories) {
  return sorted_elvCalories[0] + sorted_elvCalories[1] + sorted_elvCalories[2];
}

module.exports = {
  getSortedElvCalories,
  getMaxCalories,
  getTop3CaloriesSum,
};

let sorted_elves_calories = getSortedElvCalories("2022/01_input");
let part1 = getMaxCalories(sorted_elves_calories);
console.log("part1:", part1);
let part2 = getTop3CaloriesSum(sorted_elves_calories);
console.log("part2:", part2);
