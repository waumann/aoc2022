import Foundation

var path = "input.day1.txt"

let filedata = try String(contentsOfFile: path)
let trimmed = filedata.trimmingCharacters(in: .whitespaces)
let text: [String] = trimmed.components(separatedBy: "\n")
let data = text.map { Int($0) }

var cals = 0
var elves = [Int]()
data.forEach {
  let check0:Int? = $0
  if let check = check0 {
    cals += check
  } else {
    elves.append(cals)
    cals = 0
  }
}

elves.sort(by: >)

let sum = elves[0] + elves[1] + elves[2]
print("Answer: \(sum)")
