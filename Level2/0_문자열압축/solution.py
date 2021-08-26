def solution(s):
    answer = 0
    zip_result = []
    zip_result_len = []

    if len(s) == 1:
        return 1
    else:
        for i in range(1, len(s)):
            zip_tmp = ""
            slice_str = []
            for j in range(1, len(s) // i + 1):
                slice_str.append(s[i * (j - 1): i * j])

            slice_str.append(s[i * (len(s) // i):])

            l = 0
            zip_num = 1

            while l != len(slice_str):
                if l != len(slice_str) - 1 and slice_str[l] == slice_str[l + 1]:
                    ##압축할 수 있는 경우
                    zip_num += 1

                elif l != len(slice_str) - 1 and slice_str[l] != slice_str[l + 1]:
                    ##압축할 수 없는 경우
                    ##index l 까지 압축 후 zip_num 초기화
                    if zip_num > 1:
                        zip_tmp += str(zip_num) + slice_str[l]
                    else:
                        zip_tmp += slice_str[l]

                    zip_num = 1

                else:
                    ##가장 마지막 index
                    ##zip_num에 따라서 압축
                    if zip_num > 1:
                        zip_tmp += str(zip_num) + slice_str[l]
                    else:
                        zip_tmp += slice_str[l]

                l += 1

            zip_result.append(zip_tmp)
            zip_result_len.append(len(zip_tmp))

        answer = min(zip_result_len)

        return answer