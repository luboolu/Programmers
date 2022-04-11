import Foundation


func dfs(_ n: Int, _ computers: [[Int]], _ visited: inout [Bool], _ i: Int) {

    if i == n {
        return
    }

    visited[i] = true

    for (s, value) in computers[i].enumerated() {
        if !visited[s] && value == 1 {
            dfs(n, computers, &visited, s)
        }
    }

    return
}


func solution(_ n:Int, _ computers:[[Int]]) -> Int {

    var answer = 0
    var visited = Array(repeating: false, count: n)

    for i in 0..<n {
        if visited[i] == false {
            dfs(n, computers, &visited, i)
            answer += 1
        }
    }

    return answer
}