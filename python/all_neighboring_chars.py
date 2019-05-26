# 输入一个字符串，输出该字符串中相邻字符的所有组合。
# 举个例子，如果输入abc，它的组合有a、b、c、ab、bc、abc。（注意：输出的组合需要去重）

import bisect
from functools import reduce

def get_substrs(s):
    all_substrs = []
    for substr_len in range(1,len(s)+1):
        all_substrs.append([])
        for start_index in range(len(s)+1-substr_len):
            if len(all_substrs[-1]) <= 0:
                all_substrs[-1] = [s[start_index:start_index+substr_len]]
                continue
            insert_index = bisect.bisect_right(all_substrs[-1],s[start_index:start_index+substr_len])
            if all_substrs[-1][insert_index-1] != s[start_index:start_index+substr_len]:
                all_substrs[-1].insert(insert_index,s[start_index:start_index+substr_len])
    return reduce(lambda x,y: x+y, all_substrs)
             
if __name__ == "__main__":
    s = "bac"
    substrs = get_substrs(s)
    print(" ".join(substrs))
     



