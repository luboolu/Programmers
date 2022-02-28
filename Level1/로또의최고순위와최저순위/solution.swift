import Foundation

func solution(_ lottos:[Int], _ win_nums:[Int]) -> [Int] {

    let rank = [6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6]
    let sortedLotto = lottos.sorted()
    let sortedWin = win_nums.sorted()
    var result = 0
    var unkown = 0

    for lotto in sortedLotto {
        if lotto == 0 {
            unkown += 1
            continue
        }
        if sortedWin.contains(lotto) {
            result += 1
        }
    }

    let minRank = rank[result + unkown]!
    let maxRank = rank[result]!


    return [minRank, maxRank]
}