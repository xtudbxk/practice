# 有N张卡牌堆成一摞，每张卡牌上都会有一个整数标记其分数。 
# 现有两个人要交替从牌堆顶拿牌，第一个人可以拿1~2张，后面每次可以拿的牌数为 1~上一个人拿的牌数乘2, 直至拿完全部牌
# 每个人拿至手中的牌的分数和即为其最终得分。
# 假设两个人都会采取最佳策略拿牌来使自己的得分最大化，请问先手拿牌的人的得分为多少？

# 递推公式
# g[N][S] 表示还剩N张牌时，先手拿S张牌，最多能拿多少分
# g[N][S] = N张牌总分 - max{ g[N-S][s], s = 1,2,...,2S } 
# 即拿了之后，另一个人拿了剩下的最多之后剩下的

# 虽然可以拿牌的个数呈指数增长, 但实际上若S大于N,则g[N][S] = 0, 故只需考虑S <= N时的g[N][S]
# 由于不知道哪些需要g[N][S]需要计算，使用递归会方便很多

max_points = {}
def get_max_points(card_points,taked_cards_num):
    if len(card_points) in max_points and taked_cards_num in max_points[len(card_points)]:
        return max_points[len(card_points)][taked_cards_num]

    sum_ = sum(card_points)
    # set initialization values to max_points
    if taked_cards_num >= len(card_points) or len(card_points) <= 1:
        return sum_

    # compute max_points for other taked_cards_num and len(card_points)
    if len(card_points) not in max_points:
        max_points[len(card_points)] = {}
    max_points[len(card_points)][taked_cards_num] = sum_-get_max_points(card_points[taked_cards_num:],1)
    for taked_cards_num_by_other in range(2,2*taked_cards_num+1):
        max_points[len(card_points)][taked_cards_num] = min(max_points[len(card_points)][taked_cards_num],sum_-get_max_points(card_points[taked_cards_num:],taked_cards_num_by_other))

    return max_points[len(card_points)][taked_cards_num]


if __name__ == "__main__":
    card_points = [3,-4,1,1,7]
    print(max(get_max_points(card_points,1),get_max_points(card_points,2)))
