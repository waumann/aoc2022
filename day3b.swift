import Foundation

var path = "input.day3.txt"

let filedata = try String(contentsOfFile: path)
var data: [String] = filedata.components(separatedBy: "\n")
data.remove(at: data.count-1)

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
var lineptr = 0
print("Line count = \(data.count)")
while lineptr < data.count {
  let a = Set(Array(data[lineptr]))
  let b = Set(Array(data[lineptr+1]))
  let c = Set(Array(data[lineptr+2]))
  let candidates = a.intersection(b)
  let badge = c.intersection(candidates)
  var score = 0
  if let item = badge.first {
    score = c_to_i[item] ?? 0
  } else {
    print("Got unexpected nil value")
  }
  assert(score != 0)
  priorities += score
  lineptr += 3
}
print("Sum of priorities is \(priorities)")
