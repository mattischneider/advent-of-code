var fs = require("fs");

function getAssignmentPairs(filename) {
  var data = fs.readFileSync(filename, "utf8");
  return data.split("\n").map((i) => i.split(","));
}

function hasContainments(assignment) {
  first_left = parseInt(assignment[0].split("-")[0]);
  first_right = parseInt(assignment[0].split("-")[1]);
  second_left = parseInt(assignment[1].split("-")[0]);
  second_right = parseInt(assignment[1].split("-")[1]);
  if (first_left <= second_left && first_right >= second_right) {
    return 1;
  }
  if (second_left <= first_left && second_right >= first_right) {
    return 1;
  }
  return 0;
}

function hasOverlap(assignment) {
  let first_left = parseInt(assignment[0].split("-")[0]);
  let first_right = parseInt(assignment[0].split("-")[1]);
  let second_left = parseInt(assignment[1].split("-")[0]);
  let second_right = parseInt(assignment[1].split("-")[1]);
  if (first_left <= second_left && first_right >= second_left) {
    return 1;
  }
  if (second_left <= first_left && second_right >= first_left) {
    return 1;
  }
  return 0;
}

function getNumberOfContainments(assignments) {
  return assignments.map(hasContainments).reduce((a, b) => a + b);
}
function getNumberOfOverlapSections(assignments) {
  return assignments.map(hasOverlap).reduce((a, b) => a + b);
}

module.exports = {
  getAssignmentPairs,
  hasContainments,
  hasOverlap,
  getNumberOfContainments,
  getNumberOfOverlapSections,
};

let assignments = getAssignmentPairs("2022/04_input");
console.log("part1:", getNumberOfContainments(assignments));
console.log("part2:", getNumberOfOverlapSections(assignments));
