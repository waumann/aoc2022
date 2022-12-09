import Foundation

let puzzle = CommandLine.arguments[0].split(separator: ".")[0]
let day = puzzle.prefix(puzzle.count-1)

var path = "input.\(day).txt"

let filedata = try String(contentsOfFile: path)
let trimmed = filedata.trimmingCharacters(in: .whitespaces)
var data: [String] = trimmed.components(separatedBy: "\n")
data.remove(at: data.count-1)

var visited = Set<String>()

var h_x = 0
var h_y = 0
var t_x = 0
var t_y = 0

func move(dir: Substring) {
  if dir == "R" { h_x += 1 }
  if dir == "U" { h_y += 1 }
  if dir == "L" { h_x -= 1 }
  if dir == "D" { h_y -= 1 }

  let d_x = h_x - t_x
  let d_y = h_y - t_y
  if abs(d_x) >= 2 || abs(d_y) >= 2 {
    if d_x != 0 { t_x += d_x / abs(d_x) }
    if d_y != 0 { t_y += d_y / abs(d_y) }
  }
  visited.insert("\(t_x),\(t_y)")
}

func moveN(dir: Substring, steps: Int) {
  for i in 1...steps {
    move(dir: dir)
  } 
}

data.forEach {
  let dir = $0.prefix(1)
  let steps = Int($0.suffix($0.count - 2)) ?? 0
  assert(steps != 0)
  moveN(dir: dir, steps: steps)
}
print("Visited = \(visited.count)")
