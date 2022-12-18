var fs = require("fs");

class Directory {
  constructor(name, files, parentDirectory) {
    this.name = name;
    this.files = files;
    this.parentDirectory = parentDirectory;
    this.subdirectories = Array(0);
  }

  get totalFileSizeOfFolder() {
    if (this.files.length == 0) {
      return 0;
    }
    return this.files.map((e) => parseInt(e[0])).reduce((a, b) => a + b);
  }

  get totalSizeOfFolder() {
    let output = this.totalFileSizeOfFolder;
    if (this.subdirectories.length == 0) {
      return output;
    }
    return (
      output +
      this.subdirectories
        .map((e) => e.totalSizeOfFolder)
        .reduce((a, b) => a + b)
    );
  }

  addSubdirectory(subdirectory) {
    this.subdirectories.push(subdirectory);
  }
}

class Tree {
  constructor(directories) {
    this.directories = directories;
  }

  get totalSpace() {
    return this.directories[0].totalSizeOfFolder;
  }

  part1(limit) {
    let output = 0;
    for (let i = 0; i < this.directories.length; i++) {
      let dirSize = this.directories[i].totalSizeOfFolder;
      if (dirSize <= limit) {
        output += dirSize;
      }
    }
    return output;
  }

  findSmallestDirToDelete(totalDiskSize, freeSpaceNeeded) {
    let unusedSpace = totalDiskSize - this.totalSpace;
    let currentMin = totalDiskSize;
    for (let i = 0; i < this.directories.length; i++) {
      const element = this.directories[i];
      let tempMin = unusedSpace + element.totalSizeOfFolder;
      if (
        tempMin >= freeSpaceNeeded &&
        element.totalSizeOfFolder <= currentMin
      ) {
        currentMin = element.totalSizeOfFolder;
      }
    }
    return currentMin;
  }
}

function parseTerminalOutput(filename) {
  let data = fs.readFileSync(filename, "utf8").split("\n");
  let directories = Array(0);
  let directoryStack = Array(0);
  for (let i = 1; i < data.length; i++) {
    if (data[i].startsWith("dir ")) {
      continue;
    }
    if (data[i] == "$ ls") {
      directoryName = data[i - 1].substring(5);
      files = Array(0);
      continue;
    }
    if (
      data[i].startsWith("$ cd") &&
      typeof directoryName !== "undefined" &&
      directoryName == "none"
    ) {
      if (data[i] == "$ cd ..") {
        directoryStack.pop();
      }
      continue;
    }
    if (
      (data[i] == "" || data[i].startsWith("$ cd")) &&
      typeof directoryName !== "undefined" &&
      directoryName != "none"
    ) {
      if (directoryStack.length > 0) {
        parent = directoryStack[directoryStack.length - 1];
      } else {
        parent = "none";
      }
      let d = new Directory(directoryName, files, parent);
      if (parent != "none") {
        parent.addSubdirectory(d);
      }
      directories.push(d);
      directoryName = "none";
      if (data[i] != "$ cd ..") {
        directoryStack.push(d);
      }
      continue;
    }
    files.push(data[i].split(" "));
  }
  return new Tree(directories);
}

module.exports = {
  Tree,
  Directory,
  parseTerminalOutput,
};

let tree = parseTerminalOutput("2022/07_input");
console.log("part1:", tree.part1(100000));
console.log("part2:", tree.findSmallestDirToDelete(70000000, 30000000));
