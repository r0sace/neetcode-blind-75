def max_profit(prices):
    left = 0
    right = 1
    max_profit = 0

    while right <= len(prices)-1:
        if prices[left] < prices[right]:
            temp_profit = prices[right] - prices[left]
            right += 1
            if temp_profit > max_profit:
                max_profit = temp_profit
        else:
            left = right
            right = right + 1

    return max_profit
max_profit([1,2,4,2,5,7,2,4,9,0,9])