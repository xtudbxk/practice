# 作为一个手串艺人，有金主向你订购了一条包含n个杂色串珠的手串——每个串珠要么无色，要么涂了若干种颜色。为了使手串的色彩看起来不那么单调，金主要求，手串上的任意一种颜色（不包含无色），在任意连续的m个串珠里至多出现一次（注意这里手串是一个环形）。手串上的颜色一共有c种。现在按顺时针序告诉你n个串珠的手串上，每个串珠用所包含的颜色分别有哪些。请你判断该手串上有多少种颜色不符合要求。即询问有多少种颜色在任意连续m个串珠中出现了至少两次。

from functools import reduce

def get_unsatisfied_color_number(n,m,c,colors):
    position_of_last_appearance = [-m]*c
    unsatisfed_color_flag = [False]*c
    for count in range(n+m-1):
        cur_pearl_index = count % n
        print(f"position_of_last_appearance:{position_of_last_appearance}")
        print(f"colors:{colors[cur_pearl_index]}")
        print(f"unsatisfed_color_flag:{unsatisfed_color_flag}")
        for single_color in colors[cur_pearl_index]:
            if count - position_of_last_appearance[single_color-1] < m:
                unsatisfed_color_flag[single_color-1] = True
            else:
                position_of_last_appearance[single_color-1] = count
    return reduce(lambda x,y: x+1 if y is True else x,unsatisfed_color_flag,0)

if __name__ == "__main__":
    n,m,c = 5,2,3
    colors = [[1,2,3],[],[2,3],[2],[3]]
    print(get_unsatisfied_color_number(n,m,c,colors))
