import Foundation

func solution(_ clothes:[[String]]) -> Int {

    var answer: Int = 1
    var closet: [String : Int] = [:]

    for c in clothes {
        if closet[c[1]] == nil {
            closet[c[1]] = 1
        } else {
            closet[c[1]] = closet[c[1]]! + 1
        }
    }

    for c in closet {
        answer *= (c.value + 1)
    }

    return answer - 1
}