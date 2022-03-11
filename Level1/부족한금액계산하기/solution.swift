func solution(_ price:Int, _ money:Int, _ count:Int) -> Int64{
    var cost: Int = 0

    for c in 1...count {
        cost += price * c
    }

    if cost > money {
        return Int64(cost - money)
    } else {
        return 0
    }
}