// https://leetcode.com/problems/triangle/description/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
    public:

        int min(int a, int b){
            cout << a << ", " << b << endl;
            return a<b ? a:b;
        }

        int minimumTotal(vector<vector<int>>& triangle){
            int total = triangle[0][0];
            // cout << total << " + ";
            for(int i = 1; i<triangle.size(); i++){
                total += min(triangle[i][i], triangle[i][i-1]);
                // cout << min(triangle[i][i], triangle[i][i-1]) << " + ";
            }
            cout << endl;
            return total;
        }
};

int main(){
    Solution sol; 

    //testcase 1
    vector<vector<int>> triangle = {{2}, {3,4}, {6,5,7}, {4,1,8,3}};
    int output = 11;

    int answer = sol.minimumTotal(triangle);

    if(answer == output)
        cout << "Test passed" << endl;
    else {
        cout << "Test Failed" << endl;
        cout << "Expected Output: " << output << endl;
        cout << "Your Answer: " << answer << endl;
    }
}