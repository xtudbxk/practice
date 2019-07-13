# 字符串搜索 KMP算法

def get_next_comparation_function(s):
    next_comparation = [-1]
    index,compare_index = 1,0
    while(index<len(s)):
        if s[index] == s[compare_index]:
            next_comparation.append( next_comparation[compare_index] )
            index += 1
            compare_index += 1
        else:
            if compare_index == 0:
                next_comparation.append(0)
                index += 1
            else:
                compare_index = next_comparation[compare_index]
    return next_comparation

def search_substring(main_s,sub_s):
    next_comparation = get_next_comparation_function(sub_s)
    print(f"sub_s:{sub_s},next_comparation:{next_comparation}")
    index,compare_index = 1,0
    while(index<len(main_s)):
        if main_s[index] != sub_s[compare_index]:
            compare_index = next_comparation[compare_index]
            if compare_index == -1:
                index += 1
                compare_index += 1
        else:
            index += 1
            compare_index += 1
        if compare_index == len(sub_s):
            break
    else:
        return False
    return index - compare_index


if __name__ == "__main__":
    main_s = "afessoiejf2fh9827heri8r972397234hueu92er43"
    sub_s = "97234"
    print(f"main_s:{main_s}\nsub_s:{sub_s}\ncomparation_result:{search_substring(main_s,sub_s)}")
    sub_s = "972397234"
    print(f"main_s:{main_s}\nsub_s:{sub_s}\ncomparation_result:{search_substring(main_s,sub_s)}")
    
