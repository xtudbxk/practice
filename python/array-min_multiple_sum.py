# 给定一个数组序列, 需要求选出一个区间, 使得该区间是所有区间中经过如下计算的值最大的一个：
# 区间中的最小数 * 区间所有数的和最后程序输出经过计算后的最大值即可，不需要输出具体的区间。

def get_max_value_of_minnum_multiple_sum(a):
    # get prefix sum
    sum_,prefix_sum = 0,[0]
    for single_a in a:
        sum_ += single_a
        prefix_sum.append(sum_)

    # get left and right index if current node is minum
    left_indexs = []
    right_indexs = []
    for index,single_a in enumerate(a):
        test_index = index - 1
        while(test_index >= 0):
            if a[test_index] < single_a:
                left_indexs.append(test_index+1)
                right_indexs.append(len(a)-1)
                break
            elif a[test_index] == single_a:
                left_indexs.append(left_indexs[test_index])
                right_indexs.append(len(a)-1)
                break
            else:
                test_index = left_indexs[test_index] - 1
                right_indexs[test_index] = min(right_indexs[test_index],index-1)
        else:
            left_indexs.append(0)
            right_indexs.append(len(a)-1)

    # get max values of minum multiple sum
    max_value = 0
    for index in range(len(a)):
        max_value = max(max_value,a[index]*(prefix_sum[right_indexs[index]+1]-prefix_sum[left_indexs[index]]))

    return max_value

if __name__ == "__main__":
    #a = [6,2,1]
    a = [6,2,1,2,6,4,3,9,10,1,2,4,5,3,5,6,7,2,1,4,9,6,4,65,4,3,6,7]
    print(get_max_value_of_minnum_multiple_sum(a))

                


