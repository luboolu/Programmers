import Foundation

func solution(_ genres:[String], _ plays:[Int]) -> [Int] {

    var answer: [Int] = []
    var music: [Int : Int] = [:] //노래 고유 번호: 재생횟수
    var genre: [Int : String] = [:]//노래 고유 번호: 장르
    var genreCount: [String : Int] = [:] //장르 : 전체 재생횟수

    for i in 0..<genres.count {
        music[i] = plays[i]
        genre[i] = genres[i]
        if genreCount[genres[i]] == nil {
            genreCount[genres[i]] = plays[i]
        } else {
            genreCount[genres[i]] = genreCount[genres[i]]! + plays[i]
        }
    }

    //장르별로 재생횟수 내림차순으로 정렬
    let genreCountSorted = genreCount.sorted(by: {$0.value > $1.value})

    for data in genreCountSorted {
        let genreData = genre.filter({$1 == data.key})
        let musicID = Array(genreData.keys).sorted(by: <)

        let musicData = music.filter({key, value in
                          if musicID.contains(key) {
                              return true
                          } else {
                              return false
                          }
                          })

        let musicSorted1 = musicData.sorted(by: {$0.key < $1.key})
        let musicSorted2 = musicData.sorted(by: {$0.value > $1.value})

        if musicSorted2.count == 1 {
            answer.append(musicSorted2[0].key)
        } else {
            answer.append(musicSorted2[0].key)
            answer.append(musicSorted2[1].key)
        }
    }

    return answer
}