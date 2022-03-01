func solution(_ arr:[Int], _ divisor:Int) -> [Int] {

    var answer: [Int] = []

    for a in arr.sorted() {
        if a % divisor == 0 {
            answer.append(a)
        }
    }

    if answer.count == 0 {
        answer = [-1]
    }

    return answer
}