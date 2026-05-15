#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution{
    public:
        int lengthOfSubstring(string s){
            string pal = s.substr(0,1);
            bool isUnique = false;
            for(int i = 0; i < s.length(); i++){
                for(int j = 0; j< pal.length(); j++){
                    if(s[i] == pal[j]){
                        isUnique = false;
                    } else {
                        isUnique = true;
                    }
                }
                if(isUnique){
                    pal.push_back(s[i]);
                    cout << "pal: " << pal << endl;
                    cout << s[i] << " added" << endl;
                }

                isUnique = false;

            }

            return pal.length();
        }
};

int main(){
    
    Solution s;

    cout << "Test 1" << endl;
    cout << "Expected Output: 3" << endl;
    cout << "Actual Output: " << s.lengthOfSubstring("abcabcbb") << endl;
    cout << endl;

    // cout << "Test 2" << endl;
    // cout << "Expected Output: 1" << endl;
    // cout << "Actual Output: " << s.lengthOfSubstring("bbbbb") << endl;
    // cout << endl;

    // cout << "Test 3" << endl;
    // cout << "Expected Output: 3" << endl;
    // cout << "Actual Output: " << s.lengthOfSubstring("pwwkew") << endl;
    // cout << endl;

    return 0;
}