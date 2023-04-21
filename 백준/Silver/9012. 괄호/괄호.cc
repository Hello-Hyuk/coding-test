#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main(){
    int k;
    cin >> k;
    for(int i=0;i<k;i++){
        string input;
        cin >> input;

        stack<char> st;
        string answer = "YES";
        for (int j=0;j<input.length();j++){
            if (input[j] == '('){
                st.push(input[j]);
            }
            else if (!st.empty() && st.top() == '(' && input[j] == ')'){
                st.pop();
            }
            else {
                answer = "NO";
                break;
            }
        }
        if (!st.empty()) answer = "NO";
        cout << answer << endl;
    }
    return 0;
}