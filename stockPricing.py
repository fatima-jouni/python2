# the concept of this program is to calculate the max profit a trader can have
# searching for the minimum price to buy and the maximum price to sell

prices = [5,7,3,8,5,10,7,5] 
#each index represent a day, day 0 ,day 1...

def max_profit(prices):
 min = prices[1]
 for i in range(len(prices)-1):
    if prices[i]<min:
        min = prices[i]
        index=i
     
 print("you must buy on day",index)
 max = prices[1]
 for i in range(len(prices)-1):
    if prices[i]>max:
        max = prices[i]
        index=i
      
 print("you should sell on day",index,"to achieve max profit ")
 print("you will achieve", max-min,"profit")

max_profit(prices)



