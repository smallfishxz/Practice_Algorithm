# int findProfit(int[] input, int cost) {
#   if (input.length == 0) { 
#     return 0; 
#   }
#   var profit = 0;
#   var min = input[0];
#   var max = input[0];
#   for (var i = 1; i < input.length; i++) {
#     if (max - input[i] >= cost) {
#       profit += Math.max(0, max - min - cost);
#       max = min = input[i];
#     }
#     max = Math.max(max, input[i]);
#     if (input[i] < min) {
#       max = min = input[i];
#     }
#   }
#   profit += Math.max(0, max - min - cost);
#   return profit;
# }
