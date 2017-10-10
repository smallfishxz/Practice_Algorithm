# You are given the stock prices yesterday. Find the max profit you could make with one buy and one sell.

import sys
# The main goal here is to buy at the lowest and sell at the highest. 
# Linear scan the price array. For each price, find the lowest price it, and get the current profit. Compare with what is recorded
# as max_profit, and update max_profit if current profit is higher. 
def findProfit(price):
  currMin = price[0]
  profit = 0
  # scan from the second price.
  for i in range (1, len(price)):
    # current profit is price[i] - the lowest before it, and record the max profit by comparing current and max profit
    profit = max(profit, price[i] - currMin)
    # update Min to get prepard for next price scan
    currMin = min(currMin, price[i]) 
    
  return profit

# This is my own solution, and should also work. But the current profit will be 0 other than minus for all sells.
def find_profit(price):
  min_price = sys.maxsize
  # Initialize max_profit as 0 as it is required to return 0 if no profit could be made. 
  max_profit = 0
  
  for i in range(len(price)):
    min_price = min(price[i], min_price)
    max_profit = max(price[i] - min_price, max_profit)
  
  return max_profit
  

print(find_profit([20,40,52,15,30,50,10,25]))
print(findProfit([20,40,52,15,30,50,10,25]))


