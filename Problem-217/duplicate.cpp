// https://leetcode.com/problems/contains-duplicate/description/

#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution{
    public:
        bool containsDuplicate(vector<int>& nums){
            unordered_set<int> seen;
            for(int n: nums){
                if (seen.count(n) > 0){
                    return true;
                }
                seen.insert(n);
            }
            return false;
        }
};

int main(){
    Solution s;

    cout << "Test Case 1" << endl;
    vector<int> nums = {1,2,3,1};
    string result = (s.containsDuplicate(nums)) ? "True": "false";
    cout << "Output: " << result << endl;
    cout << "Expected: True" << endl;
}

// Solved