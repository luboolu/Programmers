import Foundation

func solution(_ numbers:[Int]) -> Int {

    let sortedNum = numbers.sorted()
    let ten = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    var sum = 45

    for num in sortedNum {
        if ten.contains(num) {
            sum -= num
        }
    }

    return sum
}