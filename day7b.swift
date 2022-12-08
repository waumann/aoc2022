import Foundation

let puzzle = CommandLine.arguments[0].split(separator: ".")[0]
let day = puzzle.prefix(puzzle.count-1)

var path = "input.\(day).txt"

let filedata = try String(contentsOfFile: path)
let trimmed = filedata.trimmingCharacters(in: .whitespaces)
var data: [String] = trimmed.components(separatedBy: "\n")
data.remove(at: data.count-1)

var sizes = [Int]()

class Directory {
  var size: Int
  var subdirs = [Substring: Directory]()

  init() {
    size = 0
  }

  func add(_ ss: Int) {
    size += ss
  }

  func totalSize() -> Int {
    var total = size
    subdirs.forEach {
      total += $1.totalSize()
    }
    sizes.append(total)
    return total
  }

  func adddir(_ str: Substring) {
    subdirs[str] = Directory()
    for k in subdirs.keys {
      print("  has \(k)")
    }
  }

  func getdir(_ str: Substring) -> Directory {
    let rtnval = subdirs[str]
    if rtnval != nil {
      return rtnval!
    } else {
      print("Did not find \(str) in \(subdirs)!")
      return Directory()
    }
  }

  func mySubdirs() {
    print("---open---")
    for k in subdirs.keys {
      print("  reporting \(k)")
    }
    print("---exit---")
  }

}

var hier = Directory()
var cwd = [String]()
var pwd = hier

data.forEach {
  print($0)
  print("Checking root:")
  hier.mySubdirs()
  if $0.starts(with: "$ cd") {
    let path = $0.split(separator: " ")[2]
    assert(path.count > 0)
    if path == "/" {
      cwd.removeAll()
      pwd = hier
      pwd.mySubdirs()
      print("cwd = \(cwd)")
    } else if path == ".." {
      cwd.removeLast(1)
      print("Path reset")
      print("Pointer dump:")
      pwd = hier
      pwd.mySubdirs()
      print("Parent dump:")
      hier.mySubdirs()
      
      for p in cwd {
        print("Appending \(p) to path")
        pwd = pwd.getdir(Substring(p))
      }
      print("cwd = \(cwd)")
    } else {
      print("Changing to \(path)")
      cwd.append(String(path))
      print("cwd = \(cwd)")
      pwd = pwd.getdir(path)
    }
  } else if $0.starts(with: "$ ls") {
    // don't do anything
  } else { 
    let items = $0.split(separator: " ", maxSplits: 1)
    if items[0] == "dir" {
      print("Adding \(items[1]) to \(cwd)")
      pwd.adddir(items[1])
    } else {
      let size = Int(items[0]) ?? -1
      assert(size != -1)
      pwd.add(size)
    }
  }
}

let root_size = hier.totalSize()
print("Total used = \(root_size)")
let target_size = root_size - 40000000
print("Need to free up \(target_size)")
sizes.sort()
for size in sizes {
  if size > target_size {
    print("Smallest dir is \(size)")
    break
  }
}
