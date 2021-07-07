#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    bool answer = true;
    int p_num = 0;
    int y_num = 0;

    for (int i = 0; i < s.size(); i++){
        if (s[i] == 'p' or s[i] == 'P')
            p_num += 1;
        else if (s[i] =='y' or s[i] == 'Y')
            y_num += 1;
    }


    if (p_num == y_num)
        answer = true;
    else
        answer = false;

    return answer;
}