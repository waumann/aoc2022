import Foundation

var path = "input.day4.txt"

let filedata = try String(contentsOfFile: path)
let trimmed = filedata.trimmingCharacters(in: .whitespaces)
var data: [String] = trimmed.components(separatedBy: "\n")
data.remove(at: data.count-1)

var contained = 0
data.forEach {
  print($0)
  let elves = $0.split(separator: ",")
  let e1 = elves[0].split(separator: "-")
  let e2 = elves[1].split(separator: "-")
  let e1lo = Int(e1[0]) ?? 0
  let e1hi = Int(e1[1]) ?? 0
  let e2lo = Int(e2[0]) ?? 0
  let e2hi = Int(e2[1]) ?? 0
  assert(e1lo != 0)
  assert(e2lo != 0)
  assert(e1hi != 0)
  assert(e2hi != 0)
  if (e1lo <= e2lo && e1hi >= e2hi) || (e2lo <= e1lo && e2hi >= e1hi) { 
    contained += 1
    print("Yes: \(e1lo)-\(e1hi) and \(e2lo)-\(e2hi)")
  } else {
    print("No: \(e1lo)-\(e1hi) and \(e2lo)-\(e2hi)")
  }
}
print(contained)
