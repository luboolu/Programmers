import Foundation

func solution(_ begin:String, _ target:String, _ words:[String]) -> Int {

    func dfs(_ now: String, _ index: Int, _ dict: [String], _ path: [String]) {

        if now == target {
            answer = path.count
            return
        }

        for word in dict {
            let my = now.map({$0})
            let w = word.map({$0})
            var same = 0
            var dif = 0

            for i in 0..<word.count {
                if my[i] == w[i] {
                    same += 1
                } else {
                    dif += 1
                }
            }

            if dif == 1 {
                var newDict = dict
                var newPath = path
                newDict.remove(at: newDict.firstIndex(of: word)!)
                newPath.append(word)
                dfs(word, index + 1, newDict, newPath)
            }

        }
    }


    var answer: Int = 0

    dfs(begin, 0, words, [])

    return answer
}