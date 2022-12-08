import Foundation

let puzzle = CommandLine.arguments[0].split(separator: ".")[0]
let day = puzzle.prefix(puzzle.count-1)

let path = "input.\(day).txt"

let filedata = try String(contentsOfFile: path)
let trimmed = filedata.trimmingCharacters(in: .whitespaces)
var data: [String] = trimmed.components(separatedBy: "\n")
data.remove(at: data.count-1)

var mm = [[Character]]()
data.forEach {
  let chars = Array($0)
  mm.append(chars)
}

func isVisible(x: Int, y: Int) -> Bool {
  if x == 0 || y == 0 || x == mm[0].count - 1 || y == mm.count - 1 {
    return true
  }
  let height = mm[y][x]
  print("Checking (\(x), \(y)): \(height)")
  var vis = true
  for lf in 0..<x { if mm[y][lf] >= height { vis = false } }   
  if vis == true { return true }
  vis = true
  for rt in x+1..<mm[0].count { if mm[y][rt] >= height { vis = false } }   
  if vis == true { return true }
  vis = true
  for up in 0..<y { if mm[up][x] >= height { vis = false } }   
  if vis == true { return true }
  vis = true
  for dn in y+1..<mm.count { if mm[dn][x] >= height { vis = false } }   
  if vis == true { return true }
  return false
}

var visible = 0

for y in 0..<mm.count {
  for x in 0..<mm[0].count {
    if isVisible(x: x, y: y) {
      visible += 1
    } 
  }
}
print("Visible = \(visible)")
