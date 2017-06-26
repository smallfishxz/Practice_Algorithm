# Variance 3 - difficult

# Following the same question, there are up to 2 buy-sell transactions can be made, 
# given that the 2nd buy cannot be made before the 1st buy has been sold, what's the total profit from those transactions?

# The solution is based on the code from the base question, 
# however, an array to store the maximum value to the right has to be made first.

# int findProfit(int * input, int n) {
#     int rightMax[n];
#     int curMax = input[n-1];
#     for (int i = n -1; i >= 0; i--) {
#        curMax = max(curMax, input[i]);
#        rightMax[i] = curMax;
#     }
#     int curMin = input[0], 1stProfit = 0, profit = 0;
#     for(int i=1; i<n; i++) {
#        profit = max(profit, rightMax[i] - input[i] + 1stProfit);
#        curMin = min(curMin, input[i]);
#        1stProfit = max(1stProfit, input[i] - curMin);
#     }
#     return max(profit, 1stProfit);
# }
