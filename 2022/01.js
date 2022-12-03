var fs = require('fs');

function get_sorted_elv_calories(filename) {
    var data = fs.readFileSync(filename, 'utf8');
    let elv_foods = data.split("\n\n")
    let elv_calories = new Int32Array(elv_foods.length)
    for (let i = 0; i < elv_foods.length; i++) {
        let sum = 0
        let calory_entries = elv_foods[i].split('\n')
        for (let j = 0; j < calory_entries.length; j++) {
            sum += parseInt(calory_entries[j]);
        }
        elv_calories[i] = sum
    }
    return elv_calories.sort().reverse()
}

function get_max_calories(sorted_elv_calories) {
    return sorted_elv_calories[0]
}

function get_top3_calories_sum(sorted_elv_calories) {
    return sorted_elv_calories[0] + sorted_elv_calories[1] + sorted_elv_calories[2]
}

let test_elves = get_sorted_elv_calories('2022/01_test')
let part1_test = get_max_calories(test_elves)
console.assert(part1_test == 24000)
let part2_test = get_top3_calories_sum(test_elves)
console.assert(part2_test == 45000)

let sorted_elves_calories = get_sorted_elv_calories('2022/01_input')
let part1 = get_max_calories(sorted_elves_calories)
console.log('part1:', part1);
let part2 = get_top3_calories_sum(sorted_elves_calories)
console.log('part2:', part2);
