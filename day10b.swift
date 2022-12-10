import Foundation

let puzzle = CommandLine.arguments[0].split(separator: ".")[0]
let day = puzzle.prefix(puzzle.count-1)

var path = "input.\(day).txt"

let filedata = try String(contentsOfFile: path)
let trimmed = filedata.trimmingCharacters(in: .whitespaces)
var data: [String] = trimmed.components(separatedBy: "\n")
data.remove(at: data.count-1)

var t = 1
var r = 1
var r_hist = [1]

data.forEach {
  r_hist.append(r)
  if $0.prefix(4) != "noop" {
    r_hist.append(r)
    let delta = Int($0.split(separator: " ")[1]) ?? 0
    assert(delta != 0)
    r += delta
  }
}

var msg = ""
for y in 0...5 {
  for x in 0...39 {
    let t = x + y * 40 + 1
    msg += abs(x - r_hist[t]) <= 1 ? "#" : " "
  }
  print(msg)
  msg = ""
}
