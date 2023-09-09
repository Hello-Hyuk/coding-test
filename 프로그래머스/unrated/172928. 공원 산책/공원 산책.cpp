#include <string>
#include <vector>
#include <map>
#include <iostream>

using namespace std;

typedef struct {
int x, y;
}box;

// 상 하 좌 우
vector<pair<int,int>> moves = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
map<char, int> mapping = { { 'N', 0 }, { 'S', 1 }, { 'W', 2 }, { 'E', 3 } }; 

vector<int> solution(vector<string> park, vector<string> routes) {
	pair<int, int> loc;
	
    for (int r=0;r<park.size();r++){
        for(int c=0;c<park[0].size();c++){
            if(park[r][c]=='S'){
                loc = {r, c};
            }
        }
    }
    for (auto r : routes){
        cout << mapping[r[0]] << endl;
        
        int cnt = r[2] -48;
        int mr = moves[mapping[r[0]]].first;
        int mc = moves[mapping[r[0]]].second;
        
        int dr = loc.first;
        int dc = loc.second;
        while (cnt--){
             dr += mr;
             dc += mc;
            if (dr < 0 || dr >= park.size() || dc < 0 || dc >= park[0].size() || park[dr][dc] == 'X'){
                break;
            }
            else {
                if (cnt == 0) loc = {dr,dc};
            }
        }
    }
    
	return { loc.first, loc.second };
}