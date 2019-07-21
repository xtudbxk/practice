
# 获取两个字符串的最大连续子串的长度

def get_max_length_of_continous_common_substr(str1,str2):

    # initialization
    max_length_including_last_char = []
    for str1_len in range(len(str1)+1):
        max_length_including_last_char.append([0])
    for str2_len in range(len(str2)+1):
        max_length_including_last_char[0].append(0)

    # dp
    max_length = 0
    for str1_len in range(1,len(str1)+1):
        for str2_len in range(1,len(str2)+1):
            if str1[str1_len-1] == str2[str2_len-1]:
                max_length_including_last_char[str1_len].append(max_length_including_last_char[str1_len-1][str2_len-1]+1)
            else:
                max_length_including_last_char[str1_len].append(0)
            max_length = max(max_length,max_length_including_last_char[str1_len][str2_len])

    return max_length

if __name__ == "__main__":
    str1 = "afesffesfsefsglife"
    str2 = "ffesfseflfesf"
    print(f"str1:{str1}")
    print(f"str2:{str2}")
    print(f"max_len:{get_max_length_of_continous_common_substr(str1,str2)}")

