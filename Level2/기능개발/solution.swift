import Foundation

func solution(_ progresses:[Int], _ speeds:[Int]) -> [Int] {

    var answer: [Int] = []
    var dailyRecord = progresses
    var completed = false
    var comp: [Int] = [] {
        didSet(old) {
            if old.count != 0 {
                answer.append(comp.count - old.count)
            } else {
                answer.append(comp.count)
            }
        }
    }

    while completed == false {
        for (i, task) in dailyRecord.enumerated() {
            if task < 100 {
                dailyRecord[i] += speeds[i]
            }

            if dailyRecord[i] >= 100 {
                dailyRecord[i] = 100
            }
        }

        //배포 가능한 기능 확인
        var tmp: [Int] = []
        for (i, task) in dailyRecord.enumerated() {
            if i != dailyRecord.count - 1 {
                if dailyRecord[0] == 100 && dailyRecord[i] == 100 {
                    if comp.contains(i) == false && tmp.contains(i) == false {
                        tmp.append(i)
                    }

                    if dailyRecord[i + 1] == 100 {
                        if comp.contains(i + 1) == false && tmp.contains(i + 1) == false {
                            tmp.append(i + 1)
                        }
                    } else {
                        break
                    }
                }
            }
        }

        if tmp.count != 0 {
            comp.append(contentsOf: tmp)
        }
        //모든 작업이 완료됐는지 확인
        for task in dailyRecord {
            if task == 100 {
                completed = true
            } else {
                completed = false
                break
            }
        }

    }

    return answer
}