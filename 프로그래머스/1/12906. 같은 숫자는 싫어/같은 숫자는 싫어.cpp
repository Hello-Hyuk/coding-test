#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    /* <algorithm>
    unique : 정렬된 상태의 vector에서 중복된 값을 쓰레기 값으로 처리하여 뒤로 보내며
             쓰레기값의 시작 위치를 return 한다.
    */
    /* <vector>
    vector.erase(vec p1, vec p2) vector에서 p1 위치와 p2위치 사이의 값을 삭제
    vector.begin(), vector.end() : vector에서 처음, 끝 값의 위치를 return
    vector.front(), vector.back() : vector에서 처음, 끝 값을 반환
    */
    arr.erase(unique(arr.begin(),arr.end()),arr.end());
    vector<int> answer = arr;
    return answer;
}