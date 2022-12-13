import Foundation

let puzzle = CommandLine.arguments[0].split(separator: ".")[0]
let day = puzzle.prefix(puzzle.count-1)

let path = "input.\(day).txt"

let filedata = try String(contentsOfFile: path)
let trimmed = filedata.trimmingCharacters(in: .whitespaces)
public var data: [String] = trimmed.components(separatedBy: "\n")
data.remove(at: data.count-1)

public var moved: Set<Int> = []

func getHeight(x: Int, y: Int) -> Int {
  var val = 0
  if mm[y][x] == "S" {
    val = 1
  } else if mm[y][x] == "E" {
    val = 26
  } else { 
    val = Int(mm[y][x].asciiValue! - Character("a").asciiValue! + 1)
    assert(val != 3000)
  }
  return Int(val)
}

class Route: CustomStringConvertible {
  var x: Int
  var y: Int
  var steps: Int
  var description:String { return "(\(self.x), \(self.y))" }

  init(x: Int, y: Int, steps: Int) {
    self.x = x
    self.y = y
    self.steps = steps
  }

  func doMove() -> [Route] {
    print("In doMove()")
    var rtnlist = [Route]()
    print("Made rtnlist")
    print("At x=\(self.x), y=\(self.y)")
    let height = getHeight(x: self.x, y: self.y)
    print("Now at height \(height)")
    for delta in [(-1, 0), (1, 0), (0, -1), (0, 1)] {
      let nx = x + delta.0
      let ny = y + delta.1
      if nx < 0 { continue }
      if ny < 0 { continue }
      if nx >= mm[0].count { continue }
      if ny >= mm.count { continue }
      let key = nx * 1000 + ny
      if !moved.contains(key) {
        let rise = height - getHeight(x: nx, y: ny)
        if rise <= 1 {
          moved.insert(key)
          let new = Route(x: nx, y: ny, steps: self.steps + 1)
          rtnlist.append(new)
        }
      }
    }
    return rtnlist
  }
}

var s_x = -1
var s_y = -1

var mm = [[Character]]()
var row = 0
data.forEach {
  let chars = Array($0)
  mm.append(chars)
  for i in 0..<chars.count {
    if chars[i] == "E" {
      s_x = i
      s_y = row
    }
  }
  row += 1
}

let start = Route(x: s_x, y: s_y, steps: 0)
let key = s_x * 1000 + s_y
moved.insert(key)
print(moved)

var workq: [Route] = [start]

while true {
  let next = workq.remove(at: 0)
  let newmoves = next.doMove()
  for move in newmoves {
    if getHeight(x: move.x, y: move.y) == 1 {
      print("Total moves: \(move.steps)")
      exit(0)
    }
  }
  workq.append(contentsOf: newmoves)
}
