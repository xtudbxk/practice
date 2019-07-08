# 田忌赛马问题
# 田忌与齐王赛马，双方各有n匹马参赛（n<=100），每场比赛赌注为1两黄金，现已知齐王与田忌的每匹马的速度，并且齐王肯定是按马的速度从快到慢出场，现要你写一个程序帮助田忌计算他最好的结果是赢多少两黄金

# solver1
# 动态规划
# f[i][j] 表示田忌在经过i场比赛后，使用了从慢到快的j匹慢马所达到的最大收益,则有
# f[i][j] = max{ f[i-1][j] + score(i-j,j), f[i-1][j-1]+score(n-j+1,j) }
# 其中score(x,y)表示田忌的第x匹马与齐王的第y匹马比赛所能获得的分数

def get_gold_by_one_race(horse_tian,horse_qi):
    return 1 if horse_tian > horse_qi else (-1 if horse_tian < horse_qi else 0)

def get_max_golds(horses_tian,horses_qi):
    horses_tian.sort(reverse=True)
    horses_qi.sort(reverse=True)

    max_golds = []
    # initailization, only one race
    max_golds.append([])
    max_golds[-1].append(get_gold_by_one_race(horses_tian[0],horses_qi[0])) # not use slow horse
    max_golds[-1].append(get_gold_by_one_race(horses_tian[-1],horses_qi[0])) # use slow horse

    # dp
    for race_num in range(2,len(horses_tian)+1):
        max_golds.append([])
        # slow_horse_num = 0
        max_golds[-1].append(max_golds[-2][0]+get_gold_by_one_race(horses_tian[race_num-1],horses_qi[race_num-1]))
        # 0 < slow_horse_num < race_num
        for slow_horse_num in range(1,race_num):
            max_golds[-1].append(
                max(max_golds[-2][slow_horse_num]+get_gold_by_one_race(horses_tian[race_num-slow_horse_num-1],horses_qi[race_num-1]),
                    max_golds[-2][slow_horse_num-1]+get_gold_by_one_race(horses_tian[-slow_horse_num],horses_qi[race_num-1])))
        # slow_horse_num = race_num
        max_golds[-1].append(max_golds[-2][race_num-1]+get_gold_by_one_race(horses_tian[-race_num],horses_qi[race_num-1])) # slow_horse_num = race_num

    return max(max_golds[-1])

# solver2
# 贪心算法
# 1. 如果田忌最慢的马能赢齐王最慢的马，则先赢一局
# 2. 田忌最慢的马比齐王最慢的马慢，则和齐王最快的马比，先输一场
# 3. 田忌最慢的马和齐王最慢的马相等
#    1. 田忌最快的马比齐王最快的马快，先赢一场
#    2. 田忌最快的马和齐王最快的马慢，拿最慢的马和齐王最快的马比
#    3. 田忌最快的马和齐王最快的马相等，拿最慢的马和齐王最快的马比

from collections import deque

def get_max_golds2(horses_tian,horses_qi):
    horses_tian.sort()
    horses_qi.sort()
    horses_tian = deque(horses_tian)
    horses_qi = deque(horses_qi)

    max_scores = 0
    while(len(horses_tian) > 0):
        if horses_tian[0] > horses_qi[0]:
            max_scores += 1
            horses_tian.popleft()
            horses_qi.popleft()
        elif horses_tian[0] < horses_qi[0]:
            max_scores -= 1
            horses_tian.popleft()
            horses_qi.pop()
        else:
            if horses_tian[-1] > horses_qi[-1]:
                max_scores += 1
                horses_tian.pop()
                horses_qi.pop()
            elif horses_tian[-1] < horses_qi[-1]:
                max_scores -= 1
                horses_tian.popleft()
                horses_qi.pop()
            else:
                if horses_tian[0] < horses_qi[-1]:
                    max_scores -= 1
                elif horses_tian[0] > horses_qi[-1]:
                    max_scores += 1
                horses_tian.popleft()
                horses_qi.pop()

    return max_scores



if __name__ == "__main__":
    horses_tian = [1,2,3,4]
    horses_qi = [2,4,4,6]
    print(get_max_golds2(horses_tian,horses_qi))
