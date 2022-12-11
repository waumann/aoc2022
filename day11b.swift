import Foundation

let puzzle = CommandLine.arguments[0].split(separator: ".")[0]
let day = puzzle.prefix(puzzle.count-1)

var path = "input.\(day).txt"

let filedata = try String(contentsOfFile: path)
let trimmed = filedata.trimmingCharacters(in: .whitespaces)
var data: [String] = trimmed.components(separatedBy: "\n")
data.remove(at: data.count-1)

var monkeys: [Monkey] = []
public var common_factor = 1

class Monkey: CustomStringConvertible {
  var id: Int
  var items = [Int]()
  var divisor: Int
  var iftrue: Int
  var iffalse: Int
  var operation: Substring
  var number: Int
  var objects = 0
  var description:String {
    return """
Monkey \(id):
  Starting items: \(self.items.map { String($0) }.joined(separator: ", "))
  Operation: new = old \(self.operation) \(self.number)
  Test: divisible by \(divisor)
    if true: throw to monkey \(iftrue)
    if false: throw to monkey \(iffalse)


"""
  }

  init(id: Int, items itemList: [Int], op operation: Substring,
    div divisor: Int, iftrue ifTrue: Int, iffalse ifFalse: Int) {
    self.id = id
    self.items = itemList
    let op_list = operation.split(separator: " ")
    self.operation = op_list[0]
    let arg = Int(op_list[1])
    if arg == nil {
      self.operation = Substring("^")
      self.number = 2
    } else {
      self.number = arg!
    }
    self.divisor = divisor
    common_factor *= self.divisor
    self.iftrue = ifTrue
    self.iffalse = ifFalse
    self.objects = 0
  }
    
  func do_throws() {
    //print("Monkey \(self.id):")
    self.items.forEach {
      self.objects += 1
      var worry = $0
      //print("  Monkey inspects an item wtih a worry level of \(worry).")
      if operation == "+" {
        worry += self.number
        //print("    Worry level increases by \(self.number) to \(worry).")
      } else if operation == "*" {
        worry *= self.number
        //print("    Worry level is multiplied by \(self.number) to \(worry).")
      } else {
        worry *= $0
        //print("    Worry level is multiplied by itself to \(worry).")
      }
      worry %= common_factor

      var target = -1
      if worry % self.divisor > 0 {
        //print("    Current worry level is not divisible by \(self.divisor).")
        target = self.iffalse
      } else {
        target = self.iftrue
      }
      //print("Item with worry level \(worry) is thrown to monkey \(target).")
      monkeys[target].do_catch(worry)
    }
    self.items = []
  }

  func do_catch(_ worry: Int) {
    self.items.append(worry)
  }
}

var id = -1
var items: [Int] = []
var operation: Substring = ""
var divisor = 0
var iftrue = -1
var iffalse = -1

data.forEach {
  if $0.starts(with: "Monkey") {
    let pos = $0.index($0.startIndex, offsetBy: 7)
    let id_char = $0[pos]
    id = Int(id_char.wholeNumberValue!)
  } else if $0.starts(with: "  Start") {
    let start = $0.index($0.startIndex, offsetBy: 18)
    let range = start...
    let item_str = $0[range]
    let str_items = item_str.split(separator: ", ")
    items = str_items.map { Int($0)! }
  } else if $0.starts(with: "  Operation") {
    let start = $0.index($0.startIndex, offsetBy: 23)
    let range = start...
    operation = $0[range]
  } else if $0.starts(with: "  Test") {
    let start = $0.index($0.startIndex, offsetBy: 21)
    let range = start...
    divisor = Int($0[range]) ?? 0
    assert(divisor != 0)
  } else if $0.starts(with: "    If true") {
    let pos = $0.index($0.startIndex, offsetBy: 29)
    let id_char = $0[pos]
    iftrue = Int(id_char.wholeNumberValue!)
  } else if $0.starts(with: "    If false") {
    let pos = $0.index($0.startIndex, offsetBy: 30)
    let id_char = $0[pos]
    iffalse = Int(id_char.wholeNumberValue!)
  } else {
    monkeys.append(Monkey(id: id, items: items, op: operation, div: divisor,
      iftrue: iftrue, iffalse: iffalse))
  }
}
monkeys.append(Monkey(id: id, items: items, op: operation, div: divisor,
  iftrue: iftrue, iffalse: iffalse))

for _ in 1...10000 {
  for m in 0..<monkeys.count {
    monkeys[m].do_throws()
  }
}

var vals = monkeys.map { $0.objects }
vals.sort()
print(vals)
print("Answer: \(vals[vals.count-1] * vals[vals.count-2])")
