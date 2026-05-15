// Problem 2055: https://leetcode.com/problems/plates-between-candles/description/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> platesBetweenCandles(string s, vector<vector<int>>& queries) {
        vector<int> answer;
        
        int counter = 0;
        bool lowerbound = false;
        bool upperbound = false;
        for(int i = 0; i < queries.size(); i++){
            for(int j = queries[i][0]; j <= queries[i][1]; j++){
                // cout << i << ": "<< s.substr(queries[i][0], queries[i][1]) << endl;
                if(s[j] == '|')
                    lowerbound = true;
                    cout << i << ": "<< s.substr(queries[i][j], queries[i][1]) << endl;
                if(s[queries[i][1] - j] == '|')
                    upperbound = true;
                if(s[j] == '*' && lowerbound && upperbound)
                    counter++;
            }
            answer.push_back(counter);
            counter = 0;
        }

        return answer;
    }

    void printQueries(string s, vector<vector<int>>& queries) {
        for(int i = 0; i<queries.size(); i++){
            cout << i << ": " << s.substr(queries[i][0], queries[i][1]) << endl;
        }
    }
};

void printVector(vector<int> v){
    for(int i = 0; i<v.size(); i++){
        cout << v[i] << " ";
    }
    cout << endl;
}


int main(){
    Solution sol;

    // testcase 1
    string s = "***|**|*****|**||**|*";
    cout << "string length: " << s.length() << endl;
    vector<vector<int>>queries = {{1,17},{4,5},{14,17},{5,11},{15,16}};
    vector<int> output = {9,0,0,0,0};
    //sol.printQueries(s, queries);
    
    
    vector<int> answer = sol.platesBetweenCandles(s,queries);
    if(output != answer){
        cout << "Failed Testcase" << endl;
        cout << "Expected Output: ";
        printVector(output);

        cout << "Your Answer: ";
        printVector(answer);
    } else {
        cout  << "Passed Testcase" << endl;
    }
    

    return 0;
}