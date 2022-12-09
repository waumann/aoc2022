import Foundation

let puzzle = CommandLine.arguments[0].split(separator: ".")[0]
let day = puzzle.prefix(puzzle.count-1)

var path = "input.\(day).txt"

let filedata = try String(contentsOfFile: path)
let trimmed = filedata.trimmingCharacters(in: .whitespaces)
var data: [String] = trimmed.components(separatedBy: "\n")
data.remove(at: data.count-1)

var visited = Set<String>()

var x: [Int] = [Int](repeating: 0, count: 10)
var y: [Int] = [Int](repeating: 0, count: 10)

func follow(n: Int) {
  let d_x = x[n-1] - x[n]
  let d_y = y[n-1] - y[n]
  if abs(d_x) >= 2 || abs(d_y) >= 2 {
    if d_x != 0 { x[n] += d_x / abs(d_x) }
    if d_y != 0 { y[n] += d_y / abs(d_y) }
  }
  if n == 9 {
    visited.insert("\(x[9]),\(y[9])")
  } else {
    follow(n: n+1)
  }
}

func move(dir: Substring) {
  if dir == "R" { x[0] += 1 }
  if dir == "U" { y[0] += 1 }
  if dir == "L" { x[0] -= 1 }
  if dir == "D" { y[0] -= 1 }
  follow(n: 1)
}

func moveN(dir: Substring, steps: Int) {
  for _ in 1...steps {
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
