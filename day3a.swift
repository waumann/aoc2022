import Foundation

var path = "input.day3.txt"

let filedata = try String(contentsOfFile: path)
let trimmed = filedata.trimmingCharacters(in: .whitespaces)
let text: [String] = trimmed.components(separatedBy: "\n")
let data = text.map { String($0) }

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

c_to_i.forEach {
  let v = c_to_i[$0]
  print("Map \($0) to \(v)")
}

var priorities = 0
data.forEach {
  let allItems = Array($0)
  let midpoint = allItems.count / 2
  if midpoint != 0 {
    let A = Set(allItems[..<midpoint])
    let B = Set(allItems[midpoint...])
    let common = A.intersection(B)
    var score = 0
    if let item = common.first {
      print("Looking up \(item)")
      score = c_to_i[!item]
    }
    print(score)
  }
}
