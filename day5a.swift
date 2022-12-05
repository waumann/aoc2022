import Foundation

var path = "input.day5.txt"

let filedata = try String(contentsOfFile: path)
let trimmed = filedata.trimmingCharacters(in: .whitespaces)
var data: [String] = trimmed.components(separatedBy: "\n")
//data.remove(at: data.count-1)

var stacks = Array(
               repeating: Array(repeating: "", count: 80),
               count: 10
             )

stacks[1] = ["D", "H", "R", "Z", "S", "P", "W", "Q"]
stacks[2] = ["F", "H", "Q", "W", "R", "B", "V"]
stacks[3] = ["H", "S", "V", "C"]
stacks[4] = ["G", "F", "H"]
stacks[5] = ["Z", "B", "J", "G", "P"]
stacks[6] = ["L", "F", "W", "H", "J", "T", "Q"]
stacks[7] = ["N", "J", "V", "L", "D", "W", "T", "Z"]
stacks[8] = ["F", "H", "G", "J", "C", "Z", "T", "D"]
stacks[9] = ["H", "B", "M", "V", "P", "W"]

data.forEach {
  let words = $0.split(separator: " ")
  if words.first == "move" {
    let number = Int(words[1]) ?? 0
    assert(number != 0)
    let src = Int(words[3]) ?? 0
    assert(src != 0)
    let dst = Int(words[5]) ?? 0
    assert(dst != 0)
    var moving = stacks[src][..<number]
    print("Moving \(number) (\(moving)) from \(src) to \(dst)")
    moving.reverse()
    print("src was \(stacks[src])")
    print("dst was \(stacks[dst])")
    stacks[dst] = moving + stacks[dst]
    stacks[src].removeSubrange(..<number)
    print("dst now is \(stacks[dst])")
    print("src now is \(stacks[src])")
  }
}

for i in 1...9 {
  print("\(stacks[i][0])")
}
