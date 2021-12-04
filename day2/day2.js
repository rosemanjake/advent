const fs = require('fs')

const input = fs.readFileSync('day2\\day2.txt', 'utf8').split("\n")
var hpos = 0
var depth = 0
var aim = 0

input.forEach((direction) => {
    let splits = direction.split(" ")
    var direction = splits[0]
    var degree = parseInt(splits[1])

    switch(direction){
        case "forward":
            hpos = hpos + degree
            depth = depth + (aim * degree) // part 2 only
            break
        case "up":
            //depth = depth - degree // part 1 only
            aim = aim - degree // part 2 only
            break
        case "down":
            //depth = depth + degree // part 1 only
            aim = aim + degree // part 2 only
            break
    }
})

console.log(`Solution = ${hpos * depth}`)
