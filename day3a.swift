import Foundation

var path = "input.day3.txt"

let filedata = try String(contentsOfFile: path)
let trimmed = filedata.trimmingCharacters(in: .whitespaces)
let text: [String] = trimmed.components(separatedBy: "\n")
let data = text.map { String($0) }

var c_to_i: [Character: Int] = [:]

// a - z map to 1 - 26. A - Z map to 27 - 52.
// For lower case, I wanted to say
//      score = item.asciiValue() - Character('a').asciiValue() + 1
// ... and something similar for upper case, plus 26, but just could
// not find an answer for converting Uint8 to Int that didn't seem to
// involve dealing with int size and endianness of my system along with
// the unwrapping.

let item = Character("q")
let test = item.asciiValue() - Character("a").asciiValue() + 1
print(test)

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

c_to_i.forEach { key, value in
  // $0 here comes from the dict keys, so how can the signature not match?
  print("Map \(key) to \(value)")
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
      score = c_to_i[item] ?? 0
    } else {
      print("Got unexpected nil value")
    }
    assert(score != 0)
    priorities += score
  }
}
print("Sum of priorities is \(priorities)")
