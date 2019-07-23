
# 假设你有一个数组，它的第i个元素是一支给定的股票在第i天的价格。设计一个算法来找到最大的利润。你最多可以完成两笔交易。你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）

# solver:
# 我们以每个间隔为界，将stocks分成两部分，其中一次交易在左边完成，另一次在右边完成

from collections import deque
def get_max_profit(stocks):
    assert len(stocks) > 4
    left_max_profit = stocks[1] - stocks[0]
    left_max_profits = [left_max_profit]
    left_min_stock = stocks[0]
    for right_index_of_left_stocks in range(1,len(stocks)-2):
        left_max_profit = max(left_max_profit,stocks[right_index_of_left_stocks]-left_min_stock)
        left_min_stock = min(left_min_stock,stocks[right_index_of_left_stocks])
        left_max_profits.append(left_max_profit)

    right_max_profit = stocks[-1] - stocks[-2]
    right_max_profits = deque([right_max_profit])
    right_max_stock = stocks[-1]
    for left_index_of_right_stocks in range(-2,-len(stocks)+1,-1):
        right_max_profit = max(right_max_profit,right_max_stock - stocks[left_index_of_right_stocks])
        right_max_stock = max(right_max_stock,stocks[left_index_of_right_stocks])
        right_max_profits.appendleft(right_max_profit)

    max_profit = left_max_profit + right_max_profit
    #print(f"left_max_profits:{left_max_profits}")
    #print(f"right_max_profits:{right_max_profits}")
    for left_profit,right_profit in zip(left_max_profits,right_max_profits):
        max_profit = max(max_profit,max(0,left_profit) + max(0,right_profit))

    return max_profit

if __name__ == "__main__":
    stocks = [1,2,4,2,4,7,6,3,5,2,4,8,9]
    print(f"stocks:{stocks},max_profit:{get_max_profit(stocks)}")
    stocks = [3,3,5,0,0,3,1,4]
    print(f"stocks:{stocks},max_profit:{get_max_profit(stocks)}")
    stocks = [1,2,3,4,5]
    print(f"stocks:{stocks},max_profit:{get_max_profit(stocks)}")
    stocks = [7,6,4,3,1]
    print(f"stocks:{stocks},max_profit:{get_max_profit(stocks)}")
