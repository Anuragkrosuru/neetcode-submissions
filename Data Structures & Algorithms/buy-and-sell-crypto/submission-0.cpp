class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int j = 0;
        int n = prices.size();
        int output = 0;
        int r = 1;
        while(r < n){
            if(prices[j] < prices[r]){
                int profit = prices[r] - prices[j];
                output = max(output, profit);
            } else {
                j = r;
            }
            r++;
        }
        return output;
    }
};
