import Foundation

var path = "input.day6.txt"

let filedata = try String(contentsOfFile: path)
let trimmed = filedata.trimmingCharacters(in: .whitespaces)
var data: [String] = trimmed.components(separatedBy: "\n")
data.remove(at: data.count-1)

let packet = Array(data[0])

for index in 4..<packet.count {
  let i = index - 1
  if packet[i] != packet[i-1] &&
     packet[i] != packet[i-2] &&
     packet[i] != packet[i-3] &&
     packet[i-1] != packet[i-2] &&
     packet[i-1] != packet[i-3] &&
     packet[i-2] != packet[i-3] {
    print("At \(index): \(packet[i-3...i])")
    break
  }
}
