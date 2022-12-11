var fs = require("fs");

function getInitialCrateConfig(filename) {
  let data = fs.readFileSync(filename, "utf8");
  let crateConfig = data.split("\n\n")[0];
  let numberOfStacks = Math.ceil(
    crateConfig.split("\n").slice(-1)[0].length / 4
  );
  var output = [...Array(numberOfStacks)].map((e) => Array(0));
  crateConfig
    .split("\n")
    .slice(0, -1)
    .forEach((element) => {
      for (let index = 0; index < Math.ceil(element.length / 4); index++) {
        let value = element[1 + index * 4];
        if (value != " ") {
          output[index].push(value);
        }
      }
    });
  return output;
}

function getInstructions(filename) {
  let data = fs.readFileSync(filename, "utf8");
  let moves = data.split("\n\n")[1];
  return moves.split("\n");
}

class StackOfCrates {
  constructor(stacks) {
    this.stacks = stacks;
  }

  get numberOfStacks() {
    return this.stacks.length;
  }

  get topOfStackMessage() {
    return this.stacks.map((i) => i[0]).join("");
  }

  moveSingleCrate(from_stack, to_stack) {
    let value = this.stacks[from_stack - 1].shift();
    this.stacks[to_stack - 1].unshift(value);
  }

  moveMultipleCrates(number_of_moves, from_stack, to_stack) {
    for (var i = 0; i < number_of_moves; i++) {
      this.moveSingleCrate(from_stack, to_stack);
    }
  }

  moveMultipleCratesAtOnce(number_of_moves, from_stack, to_stack) {
    let values = Array(number_of_moves);
    for (var i = 0; i < number_of_moves; i++) {
      values[number_of_moves - i - 1] = this.stacks[from_stack - 1].shift();
    }
    values.forEach((element) => {
      this.stacks[to_stack - 1].unshift(element);
    });
  }

  performInstructions(instructions, crateMoverVersion) {
    const regex = /move ([0-9]*) from ([0-9]*) to ([0-9]*)/;
    instructions.forEach((instruction) => {
      let match = instruction.match(regex);

      if (crateMoverVersion == "9000") {
        this.moveMultipleCrates(
          parseInt(match[1]),
          parseInt(match[2]),
          parseInt(match[3])
        );
      }

      if (crateMoverVersion == "9001") {
        this.moveMultipleCratesAtOnce(
          parseInt(match[1]),
          parseInt(match[2]),
          parseInt(match[3])
        );
      }
    });
  }
}

module.exports = {
  getInitialCrateConfig,
  getInstructions,
  StackOfCrates,
};

let filename = "2022/05_input";
let crates = new StackOfCrates(getInitialCrateConfig(filename));
let instructions = getInstructions(filename);
crates.performInstructions(instructions, "9000");
console.log("part1:", crates.topOfStackMessage);

let cratesPart2 = new StackOfCrates(getInitialCrateConfig(filename));
cratesPart2.performInstructions(instructions, "9001");
console.log("part2:", cratesPart2.topOfStackMessage);
