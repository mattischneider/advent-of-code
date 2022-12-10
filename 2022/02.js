var fs = require("fs");

function getGames(filename) {
  var data = fs.readFileSync(filename, "utf8");
  return data.split("\n");
}

function getScore(game) {
  let score = 0;

  if (game[2] == "X") {
    score += 1;
  }
  if (game[2] == "Y") {
    score += 2;
  }
  if (game[2] == "Z") {
    score += 3;
  }

  if (game[0] == "A" && game[2] == "X") {
    score += 3;
  }
  if (game[0] == "B" && game[2] == "Y") {
    score += 3;
  }
  if (game[0] == "C" && game[2] == "Z") {
    score += 3;
  }

  if (game[0] == "A" && game[2] == "Y") {
    score += 6;
  }
  if (game[0] == "B" && game[2] == "Z") {
    score += 6;
  }
  if (game[0] == "C" && game[2] == "X") {
    score += 6;
  }

  return score;
}

function adjustGameScore(game) {
  if (game[0] == "A" && game[2] == "X") {
    return getScore(game.replace("X", "Z"));
  }
  if (game[0] == "A" && game[2] == "Y") {
    return getScore(game.replace("Y", "X"));
  }
  if (game[0] == "A" && game[2] == "Z") {
    return getScore(game.replace("Z", "Y"));
  }
  if (game[0] == "B") {
    return getScore(game);
  }
  if (game[0] == "C" && game[2] == "X") {
    return getScore(game.replace("X", "Y"));
  }
  if (game[0] == "C" && game[2] == "Y") {
    return getScore(game.replace("Y", "Z"));
  }
  if (game[0] == "C" && game[2] == "Z") {
    return getScore(game.replace("Z", "X"));
  }

  return score;
}

function getTotalScore(games) {
  return games.map(getScore).reduce((a, b) => a + b);
}
function getTotalScorePart2(games) {
  return games.map(adjustGameScore).reduce((a, b) => a + b);
}

module.exports = {
  getGames,
  getScore,
  adjustGameScore,
  getTotalScore,
  getTotalScorePart2,
};

let games = getGames("2022/02_input");
console.log("part1:", getTotalScore(games));
console.log("part2:", getTotalScorePart2(games));
