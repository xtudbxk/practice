
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
# 需注意由于交错序列本身的特点，细节上有许多不同
# 辅助数组 dd,da,aa,ad, d代表下降，a代表上升， dd[length-2] 代表长度为length的, 开头为下降，未尾为下降的序列中 最后一位数字最小的值, 其余类同
#
# 以每个数字为当前数字进行循环:
#     分别讨论四个辅助数组对应的四种情况:
#        以dd为例:
#        1. 在dd中查找当前数字能插入的位置
#        2. 在da中根据位置更新相应的值
#        3. 更新da，使其重新成为有序的list
#

import bisect
def get_max_length_of_crisscross_series2(array):
    # 在序列最前方虚拟两个数字，一个比array[0]小，一个比array[0]大，以便辅助数组初始化
    fuzhu = [[array[0]],[],[-array[0]],[]] # 分别是 dd,da,aa,ad, 负号是为了让list都为升序排列

    for cur_index in range(1,len(array)):
        # get insert index
        insert_index = []
        for fuzhu_index in range(4):
            if fuzhu_index in [1,2]: # da or aa
                insert_index.append( bisect.bisect_left( fuzhu[fuzhu_index], -array[cur_index] ) )
            else:
                insert_index.append( bisect.bisect_left( fuzhu[fuzhu_index], array[cur_index] ) )

        # update fuzhu
        # dd
        update_index = insert_index[1]
        if len(fuzhu[0]) > update_index:
            fuzhu[0][update_index] = min(fuzhu[0][update_index],array[cur_index]) 
        else:
            fuzhu[0].append(array[cur_index]) 
        # da
        update_index = insert_index[0]-1
        if update_index >= 0:
            if len(fuzhu[1]) > update_index:
                fuzhu[1][update_index] = min(fuzhu[1][update_index],-array[cur_index]) # da
            else:
                fuzhu[1].append(-array[cur_index])
        else:
            fuzhu[0][0] = min(fuzhu[0][0],array[cur_index]) # 更新length=2对应的值
        # aa
        update_index = insert_index[3]
        if len(fuzhu[2]) > update_index:
            fuzhu[2][update_index] = min(fuzhu[2][update_index],-array[cur_index])
        else:
            fuzhu[2].append(-array[cur_index])
        # ad
        update_index = insert_index[2]-1
        if update_index >= 0:
            if len(fuzhu[3]) > update_index:
                fuzhu[3][update_index] = min(fuzhu[3][update_index],array[cur_index])
            else:
                fuzhu[3].append(array[cur_index])
        else:
            fuzhu[2][0] = min(fuzhu[2][0],array[cur_index])

        # reorder fuzhu
        # dd
        reorder_index = insert_index[1]-1
        while(reorder_index >= 0 and fuzhu[0][reorder_index] > array[cur_index]):
            fuzhu[0][reorder_index] = array[cur_index]
            reorder_index -= 1
        # da
        reorder_index = insert_index[0]-2
        while(reorder_index >= 0 and fuzhu[1][reorder_index] > -array[cur_index]):
            fuzhu[1][reorder_index] = -array[cur_index]
            reorder_index -= 1
        # aa
        reorder_index = insert_index[3]-1
        while(reorder_index >= 0 and fuzhu[2][reorder_index] > -array[cur_index]):
            fuzhu[2][reorder_index] = -array[cur_index]
            reorder_index -= 1
        # ad
        reorder_index = insert_index[2]-2
        while(reorder_index >= 0 and fuzhu[3][reorder_index] > array[cur_index]):
            fuzhu[3][reorder_index] = array[cur_index]
            reorder_index -= 1

    return max( 2*max(len(fuzhu[0]),len(fuzhu[2])), 2*max(len(fuzhu[1]),len(fuzhu[3]))+1 )-1

if __name__ == "__main__":
    import random
    array = [random.randint(0,100) for _ in range(1000)]
    print(f"array:{array},max length:{get_max_length_of_crisscross_series(array)},max length:{get_max_length_of_crisscross_series2(array)}")


