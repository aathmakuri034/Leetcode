// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

#include <iostream>
#include <string>
#include <vector>

// Solved
using namespace std;

class Solution {
    public:
        int maxProfit(vector<int>& prices){

            int buyPrice = prices[0];
            int profit = 0;
            for(int i = 0; i < prices.size(); i++){
                if(buyPrice < prices[i]){
                    if(profit < prices[i] - buyPrice){
                        profit = prices[i] - buyPrice;
                    }
                } else {
                    buyPrice = prices[i];
                }
            }

            return profit;
        }
};


int main(){

    Solution s;

    vector<int> input_one = {7,1,5,3,6,4};

    cout << "Output: " << s.maxProfit(input_one) << endl;
    cout << "Expected Output: 5" << endl;


}