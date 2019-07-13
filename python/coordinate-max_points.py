# P为给定的二维平面整数点集。定义 P 中某点x，如果x满足 P 中任意点都不在 x 的右上方区域内（横纵坐标都大于x），则称其为“最大的”。求出所有“最大的”点的集合
# （所有点的横坐标和纵坐标都不重复, 坐标轴范围在[0, 1e9) 内）

# 每个点只需与max points中 x轴第一次大于其 或 y轴第一次大于其 的点进行对比
# 看起来使用红黑树效果最好，插入、查找和删除时间复杂度都是log(n)
# 由于python并不自带，且随机的话，max points总是少数，故还是使用一般的排序数组吧

import bisect

def find_max_points(points):
    max_points_x = [points[0][0]]
    max_points_y = [points[0][1]]
    for single_point in points[1:]:
        index_of_first_larger_x = bisect.bisect_left(max_points_x,single_point[0])
        index_of_first_larger_y = bisect.bisect_left(max_points_y,single_point[1])
        #print(f"single_point:{single_point}")
        #print(f"max_points_x:{max_points_x}, max_points_y:{max_points_y}")
        #print(f"index_of_first_larger_x:{index_of_first_larger_x},index_of_first_larger_y:{index_of_first_larger_y}")
        if index_of_first_larger_x < len(max_points_x):
            if single_point[1] <= max_points_y[-index_of_first_larger_x-1]:
                continue
            if index_of_first_larger_y < len(max_points_y):
                if single_point[0] <= max_points_x[-index_of_first_larger_y-1]:
                    continue

        existing_max_point_number = len(max_points_x)
        if index_of_first_larger_y < len(max_points_y) and single_point[1] == max_points_y[index_of_first_larger_y]:
            if index_of_first_larger_x < len(max_points_x) and single_point[0] == max_points_x[index_of_first_larger_x]:
                del max_points_x[existing_max_point_number-index_of_first_larger_y-1:index_of_first_larger_x+1]
                del max_points_y[existing_max_point_number-index_of_first_larger_x-1:index_of_first_larger_y+1]
                max_points_x.insert(existing_max_point_number-index_of_first_larger_y-1,single_point[0])
                max_points_y.insert(existing_max_point_number-index_of_first_larger_x-1,single_point[1])
            else:
                del max_points_x[existing_max_point_number-index_of_first_larger_y-1:index_of_first_larger_x]
                del max_points_y[existing_max_point_number-index_of_first_larger_x:index_of_first_larger_y+1]
                max_points_x.insert(existing_max_point_number-index_of_first_larger_y-1,single_point[0])
                max_points_y.insert(existing_max_point_number-index_of_first_larger_x,single_point[1])
        else:
            if index_of_first_larger_x < len(max_points_x) and single_point[0] == max_points_x[index_of_first_larger_x]:
                del max_points_x[existing_max_point_number-index_of_first_larger_y:index_of_first_larger_x+1]
                del max_points_y[existing_max_point_number-index_of_first_larger_x-1:index_of_first_larger_y]
                max_points_x.insert(existing_max_point_number-index_of_first_larger_y,single_point[0])
                max_points_y.insert(existing_max_point_number-index_of_first_larger_x-1,single_point[1])
            else:
                del max_points_x[existing_max_point_number-index_of_first_larger_y:index_of_first_larger_x]
                del max_points_y[existing_max_point_number-index_of_first_larger_x:index_of_first_larger_y]
                max_points_x.insert(existing_max_point_number-index_of_first_larger_y,single_point[0])
                max_points_y.insert(existing_max_point_number-index_of_first_larger_x,single_point[1])


    return zip(max_points_x,max_points_y[-1:-len(max_points_y)-1:-1])

if __name__ == "__main__":
    points = [[1,2],[5,3],[4,6],[7,5],[9,0]]
    #points = [[1,2],[1,5],[5,3],[5,5],[4,6],[4,7],[7,5],[7,8],[9,0]]
    import random
    points = []
    for i in range(100000):
        points.append((i,random.randint(0,5000)))
        points.append((i,random.randint(5001,100000)))
    for single_max_point in find_max_points(points):
        print(f"{single_max_point[0]} {single_max_point[1]}") 

