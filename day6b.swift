import Foundation

var path = "input.day6.txt"

let filedata = try String(contentsOfFile: path)
let trimmed = filedata.trimmingCharacters(in: .whitespaces)
var data: [String] = trimmed.components(separatedBy: "\n")
data.remove(at: data.count-1)

let packet = Array(data[0])

for index in 14..<packet.count {
  let i = index - 1
  let msgstart = Set(packet[i-13...i])
  if msgstart.count == 14 {
    print("At \(index): \(packet[i-13...i])")
    break
  }
}
