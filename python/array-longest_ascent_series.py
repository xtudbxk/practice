# 给出一个序列a1,a2,a3,a4,a5,a6,a7....an,求它的一个子序列（设为s1,s2,...sn），使得这个子序列满足这样的性质，s1<s2<s3<...<sn并且这个子序列的长度最长。输出这个最长的长度。


# solver1
# 动态规划，求出结果随序列长度增长的变化, 递推公式如下：
# dp[i] = max(dp[j], j=1,...,i) + 1     if s[j] < s[i]
#    or = 1                             if s[j] >= s[i]
def get_max_length_of_ascent_series(s):
    max_length = [1]
    for single_s in s[1:]:
        max_length.append(1)
        for index_j in range(len(max_length)):
            if s[index_j] < single_s:
                max_length[-1] = max(max_length[-1],max_length[index_j]+1)
    return max(max_length)

# solver2
# 使用辅助数组c, c[i]是长度为i的所有上升序列中最小的末尾元素
# 遍历元素，动态更新c, c中最后一个元素即为最大长度

import bisect 
def get_max_length_of_ascent_series2(s):
    minum_of_last_element_given_length = []
    for single_s in s:
        update_index = bisect.bisect_right(minum_of_last_element_given_length,single_s) # minum_of_last_element_given_length is ascended
        if update_index < len(minum_of_last_element_given_length):
            if single_s < minum_of_last_element_given_length[update_index]:
                minum_of_last_element_given_length[update_index] = single_s
        else:
            minum_of_last_element_given_length.append(single_s)
    return len(minum_of_last_element_given_length)

if __name__ == "__main__":
    s = [1,2,3,12,4,5,7,1,2,3]
    print(f"s:{s}, max length:{get_max_length_of_ascent_series2(s)}")

