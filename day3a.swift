import Foundation

var path = "input.day3.txt"

let filedata = try String(contentsOfFile: path)
let trimmed = filedata.trimmingCharacters(in: .whitespaces)
var data: [String] = trimmed.components(separatedBy: "\n")
data.remove(at: data.count - 1)

var c_to_i: [Character: Int] = [:]

for i in 65...90 { // Upper case
  if let c = UnicodeScalar(i) {
    let cc = Character(c)
    c_to_i[cc] = i - 64 + 26
  }
}

for i in 97...122 { // Lower case
  if let c = UnicodeScalar(i) {
    let cc = Character(c)
    c_to_i[cc] = i - 96
  }
}

var priorities = 0
data.forEach {
  let allItems = Array($0)
  let midpoint = allItems.count / 2
  if midpoint != 1 {
    let A = Set(allItems[..<midpoint])
    let B = Set(allItems[midpoint...])
    let common = A.intersection(B)
    var score = 0
    if let item = common.first {
      score = c_to_i[item] ?? 0
    } else {
      print("Got unexpected nil value")
    }
    assert(score != 0)
    priorities += score
  }
}
print("Sum of priorities is \(priorities)")
