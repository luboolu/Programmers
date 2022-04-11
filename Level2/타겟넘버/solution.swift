import Foundation

func dfs(_ numbers: [Int], _ target: Int, _ i: Int, _ sum: Int) -> Int {
    if i == numbers.count {
        return sum == target ? 1 : 0
    }

    let a = dfs(numbers, target, i + 1, sum - numbers[i])
    let b = dfs(numbers, target, i + 1, sum + numbers[i])

    return a + b
}

func solution(_ numbers:[Int], _ target:Int) -> Int {
    return dfs(numbers, target, 0, 0)
}