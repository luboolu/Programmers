#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string s) {
    string answer = "";

    int num = s.size();
    int div = num / 2;
    int re = num % 2;

    if (re == 0)
        answer = s.substr(div - 1 ,2);
    else
        answer = s[div];

    return answer;
}