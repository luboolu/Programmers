import Foundation

func solution(_ clothes:[[String]]) -> Int {

    var answer: Int = 0
    var items: [String] = []
    var closet: [String : Int] = [:]

    for c in clothes {
        print(c)
        if closet[c[1]] == nil {
            closet[c[1]] = 1
            items.append(c[1])
        } else {
            closet[c[1]] = closet[c[1]]! + 1
        }
    }

    //옷을 하나만 입는 경우
    if closet.count == 1 {
        return closet[items[0]] ?? 0
    } else {
        answer += closet.count
    }

    //옷을 두개 이상 입는 경우


    return answer
}