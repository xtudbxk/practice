
# 给定一个数组，需要去除一些数字，使剩下的数字成高低交错排列，请问剩下的交错序列最长长度是多少


# solver1:
# 一般的动态规划，o(N^2)
def get_max_length_of_crisscross_series(array):
    max_lengths = [[1,1]] # max_lengths[index][flag] 代表在array中以index对应数字结尾时的交错序列的最长长度，其中flag=0代表最后一段为下降, flag=1代表最后一段为上升
    max_length = 1
    for cur_index in range(1,len(array)):
        max_lengths.append([1,1])
        for previous_index in range(cur_index):
            if array[cur_index] < array[previous_index]:
                max_lengths[cur_index][0] = max(max_lengths[cur_index][0],max_lengths[previous_index][1]+1)
            elif array[cur_index] > array[previous_index]:
                max_lengths[cur_index][1] = max(max_lengths[cur_index][1],max_lengths[previous_index][0]+1)
        max_length = max(max_length,max_lengths[cur_index][0],max_lengths[cur_index][1])
    return max_length


# solver2:
# 类似于最长上升子序列，可以使用辅助数组法, o(N)
import bisect
def get_max_length_of_crisscross_series2(array):
    min_number_of_series = [array[0]] # min_number_of_series[ length ] 表示最后一段为下降时，长度为length的序列中，最后一个为数字最小的值，易知其随着长度的增加而增加
    negative_max_number_of_series = [-array[0]] # negative_max_number_of_series[ length ] 表示最后一段为上升时，长度为length的序列中，最后一个为数字最大的值的相反数, 易知其随着长度的增加而增加

    for num_index in range(1,len(array)):
        # 可将当前数字插入的最长的最后一段为下降的序列的长度
        length1 = bisect.bisect_left(min_number_of_series,array[num_index])

        # 可将当前数字插入的最长的最后一段为上升的序列的长度
        length2 = bisect.bisect_left(negative_max_number_of_series,-array[num_index])

        # 将当前数字插入最后一段为下降时的序列后面，形成最后一段为上升的序列
        if len(negative_max_number_of_series) < length1+1:
            negative_max_number_of_series.append(-array[num_index]) # 形成新长度
        else:
            negative_max_number_of_series[length1] = min(negative_max_number_of_series[length1],-array[num_index])

        # 将当前数字插入最后一段为上升时的序列后面，形成最后一段为下降的序列
        if len(min_number_of_series) < length2+1:
            min_number_of_series.append(array[num_index]) # 形成新长度
        else:
            min_number_of_series[length2] = min(min_number_of_series[length2],array[num_index])
        print(f"num_index:{num_index}")
        print(f"min_number_of_series:{min_number_of_series}")
        print(f"negative_max_number_of_series:{negative_max_number_of_series}")
        
    return max(len(min_number_of_series),len(negative_max_number_of_series))

if __name__ == "__main__":
    import random
    #array = [random.randint(0,20) for _ in range(10)]
    array = [9,9,14,7,17,18,13,12,4,4]
    print(f"array:{array},max length:{get_max_length_of_crisscross_series(array)},max length:{get_max_length_of_crisscross_series2(array)}")


