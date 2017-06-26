def findprofit(price):
  last = price[0]
  profit = 0
  for i in range (1, len(price)):
    profit += max(0, price[i] - last)
    last = price[i]
  return profit
