var fs = require('fs')
const alphabet = ['_', "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

function getRucksackItems(filename) {
    var data = fs.readFileSync(filename, 'utf8')
    return data.split("\n")
}

function getCommonRucksackItem(rucksack) {
    firstItems = rucksack.substring(0, rucksack.length/2)
    secondItems = rucksack.substring(rucksack.length/2,rucksack.length)
    for (i in firstItems) {
        if (secondItems.indexOf(firstItems[i]) > -1) {
            return firstItems[i]
        }
    }
}
function getTotalPriority(rucksack) {
    return rucksack.map(getCommonRucksackItem).map(i => alphabet.indexOf(i)).reduce((a, b) => a + b)
}

function findGroupBadge(rucksack_group) {
    for (i in alphabet) {
        if (rucksack_group[0].indexOf(alphabet[i]) > -1
            && rucksack_group[1].indexOf(alphabet[i]) > -1
            && rucksack_group[2].indexOf(alphabet[i]) > -1) {
            return alphabet[i]
        }
    }
}

function getRucksackGroups(rucksack) {
    return Array.from({length: rucksack.length/3}, (_, index) => index * 3).map(i => rucksack.slice(i, i + 3));
}

function getSumOfPriorities(rucksack) {
    return getRucksackGroups(rucksack).map(findGroupBadge).map(i => alphabet.indexOf(i)).reduce((a, b) => a + b)
}

testRucksackItems = getRucksackItems('2022/03_test')
console.assert(getCommonRucksackItem('vJrwpWtwJgWrhcsFMMfFFhFp') == 'p')
console.assert(getTotalPriority(testRucksackItems) == 157)

rucksackItems = getRucksackItems('2022/03_input')
console.log('part1:', getTotalPriority(rucksackItems))

testRucksackGroups = getRucksackGroups(testRucksackItems)
console.assert(findGroupBadge(testRucksackGroups[0]) == 'r')
console.assert(findGroupBadge(testRucksackGroups[1]) == 'Z')
console.assert(getSumOfPriorities(testRucksackItems) == 70)

console.log('part2:', getSumOfPriorities(rucksackItems))
