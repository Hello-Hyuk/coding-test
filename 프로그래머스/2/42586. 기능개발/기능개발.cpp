#include <string>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> days;
    int idx=0;
    for(int i=0;i<progresses.size();i++){
        auto diff = ceil(float(100 - progresses[i])/float(speeds[i]));
        days.push_back(diff);
    }
    for(int i=0;i<days.size();i++){
        if (days[idx]<days[i]){
            answer.push_back(i-idx);
            idx = i;
        }
    }   
    answer.push_back(days.size()-idx);
    
    return answer;
}
/* 참고 코드 O(n)
#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;

    int day;
    int max_day = 0;
    for (int i = 0; i < progresses.size(); ++i)
    {
        day = (99 - progresses[i]) / speeds[i] + 1;

        if (answer.empty() || max_day < day)
            answer.push_back(1);
        else
            ++answer.back();

        if (max_day < day)
            max_day = day;
    }

    return answer;
}
*/