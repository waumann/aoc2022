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
    score += me
    if elf == me {
      score += 3
    } else if me - elf == 1 || elf - me == 2 {
      score += 6
    }
  }
}

print("Answer: \(score)")
