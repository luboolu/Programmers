def solution(n, arr1, arr2):
    answer = []
    arr1_decode = []
    arr2_decode = []

    for i in range(0, n):
        arr1_map = bin(arr1[i])[2:].zfill(n)
        arr2_map = bin(arr2[i])[2:].zfill(n)

        tmp = ""
        for j in range(0, n):
            if arr1_map[j] == "0" and arr2_map[j] == "0":
                tmp += " "
            else:
                tmp += "#"
        answer.append(tmp)

    return answer

solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])