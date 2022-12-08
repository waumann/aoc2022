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

func treesVisible(x: Int, y: Int) -> Int {
  if x == 0 || y == 0 || x == mm[0].count - 1 || y == mm.count - 1 {
    return 0
  }
  let height = mm[y][x]

  var west = 0
  for i in stride(from: x-1, to: -1, by: -1) {
    west += 1
    if mm[y][i] >= height { break }
  }

  var north = 0
  for i in stride(from: y-1, to: -1, by: -1) {
    north += 1
    if mm[i][x] >= height { break }
  }

  var east = 0
  for i in x+1..<mm[0].count {
    east += 1
    if mm[y][i] >= height { break }
  }
  var south = 0
  for i in y+1..<mm.count {
    south += 1
    if mm[i][x] >= height { break }
  }
  return west * north * east * south
}

var max_visible = 0

for y in 1..<mm.count-1 {
  for x in 1..<mm[0].count-1 {
    let visible =  treesVisible(x: x, y: y)
    if visible > max_visible { max_visible = visible }
  }
}
print("Max Visible = \(max_visible)")
