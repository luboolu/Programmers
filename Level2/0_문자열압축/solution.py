def solution(s):
    answer = len(s)
    print(len(s))
    for i in range(1, len(s) // 2 + 1):
        if len(s) % i == 0:
            slice_str = []
            for j in range(1, len(s) // i + 1):
                slice_str.append(s[i * (j - 1): i * j])
            print(slice_str)
            print()

            zip_str = ""
            zip_num = 1
            zip_tmp = ""
            for j in range(len(slice_str)):
                if j < len(slice_str) - 1:
                    if slice_str[j] == slice_str[j + 1]:
                        zip_num += 1
                        zip_tmp = slice_str[j]
                    else:
                        zip_num = 1

                    if zip_tmp != "" and zip_num != 1:
                        zip_str += str(zip_num) + zip_tmp
                    else:
                        zip_str += slice_str[j]

                    print(zip_str)

    return answer