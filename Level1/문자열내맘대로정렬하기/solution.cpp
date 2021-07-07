#include <string>
#include <vector>
#include <algorithm>


using namespace std;

vector<string> solution(vector<string> strings, int n) {
    vector<string> answer;
    vector<string> new_strings;

    for(int i = 0; i < strings.size(); i++){
        new_strings.push_back(strings[i][n] + strings[i]);
    }

    sort(new_strings.begin(), new_strings.end());

    for(int i = 0; i < new_strings.size(); i++){
        answer.push_back(new_strings[i].substr(1));
    }


    return answer;
}