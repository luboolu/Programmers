#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;
    int num = 0;
    int zero = 0;

    for (int i = 0; i < lottos.size(); i++){
        if (lottos[i] != 0)
            for (int j = 0; j < win_nums.size(); j++){
                if (lottos[i] == win_nums[j])
                    num += 1;
            }
        else
            zero += 1;
    }

    int rank[] = {6, 6, 5, 4, 3, 2, 1};

    answer.push_back(rank[num + zero]);
    answer.push_back(rank[num]);

    return answer;
}