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
            cout << idx << endl;
        }
    }   
    answer.push_back(days.size()-idx);
    
    return answer;
}