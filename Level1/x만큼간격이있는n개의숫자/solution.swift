func solution(_ x:Int, _ n:Int) -> [Int64] {

    var answer = [Int64]()

    for _ in 1...n {
        if answer.last != nil {
            answer.append(answer.last! + Int64(x))
        } else {
            answer.append(Int64(x))
        }

    }

    return answer
}