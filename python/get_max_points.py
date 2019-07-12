# 有N张卡牌堆成一摞，每张卡牌上都会有一个整数标记其分数。 
# 现有两个人要交替从牌堆顶拿牌，每次至少拿一张，至多拿M张，直到牌堆被拿完。 
# 每个人拿至手中的牌的分数和即为其最终得分。
# 假设两个人都会采取最佳策略拿牌来使自己的得分最大化，请问先手拿牌的人的得分为多少？

# 递推公式
# g[N] 表示还剩N张牌时，先手拿，最多能拿多少分
# g[N] = max{ N张牌总分 - g[N-s], s = 1,2,...,M } 
# 即拿了之后，另一个人拿了剩下的最多之后剩下的

def get_max_points(card_points,max_card_once):
    if len(card_points) <= max_card_once:
        return sum(card_points)

    # initialization
    sum_n = 0
    max_points = []
    for index in range(max_card_once):
        sum_n += card_points[-index-1]
        max_points.append(sum_n)

    # compute max_points
    for index in range(max_card_once,len(card_points)):
        sum_n += card_points[-index-1]
        max_points.append(sum_n - max_points[-1])
        for index2 in range(1,max_card_once):
            max_points[-1] = max(max_points[-1],sum_n - max_points[-index2-2])

    return max_points[-1]

if __name__ == "__main__":
    card_points = [3,-4,1,1,7]
    max_card_once = 2
    print(get_max_points(card_points,max_card_once))
