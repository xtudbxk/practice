
# 给定两个单词word1和word2, 计算出将word1转为word2所需的最小操作数
# 操作有三种： 1. 插入一个字符  2. 删除一个字符 3. 替换一个字符

# solver:
# 采用类似于最大公共子序列的方法，将两个序列分别进行划分，即可减小规模
# f[n][m] =  # 描述了两个序列只有前n和只有前m个时的最小操作数
#     1. f[n-1][m-1]   while word2[m] == word1[n]
#     2.  min( f[n][m-1]+1,  f[n-1][m-1]+1, f[n-1][m]+1 )  分别代表对word1的最后一个字符进行删除、替换、和插入

def get_min_operations(word1:str, word2:str) -> int:
    # initialization
    min_operations = [[] for _ in range(max(len(word1),len(word2))+1)]
    for word1_len in range(len(word1)+1):
        min_operations[0].append(word1_len)
    for word2_len in range(len(word2)+1):
        min_operations[word2_len].append(word2_len)

    # dp
    for char1_index in range(len(word1)):
        for char2_index in range(len(word2)):
            if word1[char1_index] == word2[char2_index]:
                min_operations[char2_index+1].append( min_operations[char2_index][char1_index] )
            else:
                # delete the last char in word1
                min_operations[char2_index+1].append( min_operations[char2_index+1][char1_index]+1 )
                # replace the last char in word1
                min_operations[char2_index+1][char1_index+1] = min(min_operations[char2_index+1][char1_index+1],
                        min_operations[char2_index][char1_index]+1)
                # insert a new char which is same with the last char in word2 in word1
                min_operations[char2_index+1][char1_index+1] = min(min_operations[char2_index+1][char1_index+1],
                        min_operations[char2_index][char1_index+1]+1)
    return min_operations[len(word2)][len(word1)]


if __name__ == "__main__":
    word1 = "intention"
    word2 = "execution"

    print(f"min operations:{get_min_operations(word1,word2)}")
