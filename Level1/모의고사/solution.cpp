#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;

    vector<int> one = {1,2,3,4,5};
    vector<int> two = {2,1,2,3,2,4,2,5};
    vector<int> three = {3,3,1,1,2,2,4,4,5,5};

    vector<int> one_answer, two_answer, three_answer;

    for(int i = 0; i < answers.size(); i++){
        one_answer.push_back(one[i % one.size()]);
        two_answer.push_back(two[i % two.size()]);
        three_answer.push_back(three[i % three.size()]);
    }

    vector<int> score = {0,0,0};

    for(int i = 0; i < answers.size(); i++){
        if (one_answer[i] == answers[i])
            score[0] += 1;
        if (two_answer[i] == answers[i])
            score[1] += 1;
        if (three_answer[i] == answers[i])
            score[2] += 1;
    }


    int max = max_element(score.begin(),score.end()) - score.begin();

    answer.push_back(max + 1);

    for(int i = 0; i < score.size(); i++){
        if (i != max and score[i] == score[max])
            answer.push_back(i + 1);
    }


    return answer;
}