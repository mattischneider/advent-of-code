var fs = require("fs");

function getFirstMarker(data, packageLength) {
  for (let i = 0; i < data.length - packageLength; i++) {
    if (new Set(data.substring(i, i + packageLength)).size == packageLength) {
      return i + packageLength;
    }
  }
}

module.exports = {
  getFirstMarker,
};

function getInput(filename) {
  return fs.readFileSync(filename, "utf8");
}

let dataStream = getInput("2022/06_input");
console.log("part1:", getFirstMarker(dataStream, 4));
console.log("part2:", getFirstMarker(dataStream, 14));
