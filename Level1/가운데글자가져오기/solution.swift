func solution(_ s:String) -> String {

    let mid1 = s.count / 2
    let mid2 = s.count % 2

    if mid2 == 1 {
        return String(s[mid1])
    } else {
        return String(s[mid1 - 1]) + String(s[mid1])
    }

}

extension String {
    subscript(_ index: Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: index)]
    }
}
