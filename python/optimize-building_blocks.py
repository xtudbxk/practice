
#  一共有n块积木，每块积木有长度L和重量W两种属性。在堆积积木时，要求上面一块的长度要严格小于下面一块的长度，且每块积木能承受其上的总重量不超过其自身的7倍，求使用n块积木能搭建的最高层数为多少？

# 易知，由于长度为严格小，我们可首先对积木按长度进行排序，之后问题可转化为在每一级别的长度的积木中选择一块(可不选)来进行堆积，求最大层数，变成类似背包问题
# 而 长度的级别个数 即可视为选择的规模， 重量即为限制条件
# 
# 则单一操作导致重量的变化为
#    使用积木
#        1.下往上推公式
#            \latex $ w_{new} = min(w_{old} - w_{this\_layer}, 7w_{this\_layer}) ~~\forall ~w_{old} ~ \&\& ~w_{this\_layer}
#                      ## 该公式需要对下层中所有的w_{old}和w_{this\_layer}进行遍历，再对相同w_{new}取层数最大的结果
#        2.上往下推公式
#            \latex $ w_{new} = \begin{cases} w_{old} - w_{this\_layer} ~~&~\forall~w_{this\_layer} < \frac 17 w_{new} ~ \&\& ~ w_{old} < 8 w_{this\_layer} \\ 7w_{this\_layer} ~~&~\forall ~w_{this\_layer} = \frac 17 w_{new} ~\&\& ~w_{old} \ge 8w_{this\_layer} \end{cases}
#                      ## 该公式需对每个w_{new}进行遍历，然后再对每个w_{new}中符合条件的所有w_{old}和w_{this\_layer}进行遍历
#                      ### 更详细的分析中，可知w_{new}遍历个数可缩减为w_{this\_layer}中值的个数，\\并使用在线递增方法对w_{old}和w_{this\_layer}进行遍历，\\故实际遍历次数应少于从下往上递推公式，但编程更复杂
#    不使用积木
#        \latex $ w_{new} = w_{old} $
#
# 单一操作导致层数变化为
#    使用积木
#        \latex $ f_{n} = f_{n-1} + 1
#    不使用积木
#        \latex $ f_n = f_{n-1}


# solver1: 使用从下往上推公式
# 
def get_max_heights(blocks): # blocks = [(l1,w1),(l2,w2),...]
    blocks.sort() # sort with length increase
    print(f"sorted blocks:{blocks}")

    # 
    max_length_of_n_subtract_1 = []
    while(len(blocks) > 0):
        # get all candidate weight of nth choice
        len_of_n = blocks[-1][0] # the max len of left blocks
        weight_of_n = []
        while(len(blocks) > 0 and blocks[-1][0] == len_of_n):
            weight_of_n.append(blocks.pop()[1])

        # initialization
        # no block is choosed
        max_length_of_n = [max_length_of_n_subtract_1[weight] for weight in range(len(max_length_of_n_subtract_1))]
        # the choosed block is the block of the first layer
        max_length_of_n.extend([0 for _ in range( 7*max(weight_of_n)-len(max_length_of_n)+1 )])
        for weight in weight_of_n: max_length_of_n[7*weight] = max(max_length_of_n[7*weight],1)
        # dp
        for single_w in weight_of_n:
            for old_w in range(single_w,len(max_length_of_n_subtract_1)):
                new_w = min(old_w-single_w,7*single_w)
                max_length_of_n[new_w] = max(max_length_of_n[new_w],max_length_of_n_subtract_1[old_w]+1)

        #
        max_length_of_n_subtract_1 = max_length_of_n
    return max(max_length_of_n_subtract_1)

# solver2: 使用从上往下推公式
#
def get_max_heights2(blocks): # blocks = [(l1,w1),(l2,w2),...]
    blocks.sort() # sort with length increase
    print(f"sorted blocks:{blocks}")

    # 
    max_length_of_n_subtract_1 = []
    while(len(blocks)>0):
        # get all candidate weight of nth choice
        len_of_n = blocks[-1][0] # the max len of left blocks
        weight_of_n = []
        while(len(blocks) > 0 and blocks[-1][0] == len_of_n):
            weight_of_n.append(blocks.pop()[1])

        max_length_of_n = []
        for new_w in range(7*max(weight_of_n)+1):
            max_length_of_n.append(0)
            for single_w in weight_of_n:
                if 7*single_w > new_w:
                    old_w = new_w + single_w
                    if old_w < len(max_length_of_n_subtract_1):
                        max_length_of_n[new_w] = max(max_length_of_n[new_w],max_length_of_n_subtract_1[old_w]+1)
                else:
                    max_length_of_n[new_w] = max(max_length_of_n[new_w],1) # if this choosed block is the first one
                    for old_w in range(8*single_w,len(max_length_of_n_subtract_1)):
                        max_length_of_n[new_w] = max(max_length_of_n[new_w],max_length_of_n_subtract_1[old_w]+1)

        max_length_of_n_subtract_1 = max_length_of_n

    return max(max_length_of_n)


if __name__ == "__main__":
    import random
    blocks = [(random.randint(1,10),random.randint(1,10)) for _ in range(10)]
    blocks = [(1, 1), (2, 7), (3, 1), (7, 2), (7, 6), (8, 1), (9, 1), (9, 6), (9, 7), (10, 8)]
    blocks2 = [one for one in blocks]
    print(f"max length:{get_max_heights(blocks)}")
    print(f"max length:{get_max_heights2(blocks2)}")






