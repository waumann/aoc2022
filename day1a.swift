import Foundation

var path = "input.day1.txt"

let filedata = try String(contentsOfFile: path)
let trimmed = filedata.trimmingCharacters(in: .whitespaces)
let text: [String] = trimmed.components(separatedBy: "\n")
let data = text.map { Int($0) }

var cals = 0
var max_cals = 0
data.forEach {
  let check0:Int? = $0
  if let check = check0 {
    cals += check
  } else {
    if cals > max_cals {
      max_cals = cals
    }
    cals = 0
  }
}
print("Answer: \(max_cals)")
