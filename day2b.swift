import Foundation

var path = "input.day2.txt"

let filedata = try String(contentsOfFile: path)
let trimmed = filedata.trimmingCharacters(in: .whitespaces)
let text: [String] = trimmed.components(separatedBy: "\n")
let data = text.map { String($0) }

var movemap = ["A": 1,
               "B": 2,
               "C": 3,
               "X": 1,
               "Y": 2,
               "Z": 3]

var score = 0
data.forEach {
  let moves = $0.components(separatedBy: " ")
  if let elf = movemap[moves[0]], let me = movemap[moves[1]] {
    var move = 0
    if me == 2 {
      move = elf
    } else if me == 1 {
      move = elf - 1
    } else {
      move = elf + 1
    }
    if move == 0 {
      move = 3
    } else if move == 4 {
      move = 1
    }

    score += move
    if elf == move {
      score += 3
    } else if move - elf == 1 || elf - move == 2 {
      score += 6
    }
  }
}

print("Answer: \(score)")
