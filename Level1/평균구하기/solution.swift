func solution(_ arr:[Int]) -> Double {

    var sum = 0

    for a in arr {
        sum += a
    }

    return Double(sum) / Double(arr.count)
}