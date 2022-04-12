import Foundation

func solution(_ numbers:[Int]) -> String {

    let strs = numbers.map({String($0)}).sorted(by: {$0 + $1 > $1 + $0})
    let answer = strs.joined(separator: "")

    //[0,0,0]인 경우
    if let first = answer.first {
        if first == "0" {
            return "0"
        }
    }

    return answer
}