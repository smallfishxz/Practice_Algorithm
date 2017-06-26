def findProfit(price):
  currMin = price[0]
  profit = 0
  for i in range (0, len(price)):
    profit = max(profit, price[i] - currMin)
    currMin = min(currMin, price[i]) 
  return profit
