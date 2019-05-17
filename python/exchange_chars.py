#Algorith Problem
#字符串S由小写字母构成，长度为n。定义一种操作，每次都可以挑选字符串中任意的两个相邻字母进行交换。询问在至多交换m次之后，字符串中最多有多少个连续的位置上的字母相同
#
#思路:
#以每个点当做最长连续子序列中未移动的点，进行向左向右扩展

def get_max_length_of_substring_has_same_characters_after_exchaing(s,m):
    left_and_right_p_of_same_char = []
    nearest_position_of_left_char = {}
    for single_index,single_c in enumerate(s):
        if single_c not in nearest_position_of_left_char:
            left_and_right_p_of_same_char.append({"left":None,"right":None})
        else:
            left_and_right_p_of_same_char.append({"left":nearest_position_of_left_char[single_c],"right":None})
            left_and_right_p_of_same_char[nearest_position_of_left_char[single_c]]["right"] = single_index
        nearest_position_of_left_char[single_c] = single_index

    max_length = 0
    for single_index,not_moving_char in enumerate(s):
        max_moving_steps = 0
        left_p,right_p = left_and_right_p_of_same_char[single_index]["left"],left_and_right_p_of_same_char[single_index]["right"]
        left_moving_to_p,right_moving_to_p = single_index-1,single_index+1
        while(max_moving_steps <= m):
            #print(f"max_moving_steps:{max_moving_steps}")
            if left_p is not None:
                left_moving_step = left_moving_to_p - left_p
            if right_p is not None:
                right_moving_step = right_p - right_moving_to_p
            if left_p is not None and right_p is not None:
                if left_moving_step > right_moving_step:
                    max_moving_steps += right_moving_step
                    right_p = left_and_right_p_of_same_char[right_p]["right"]
                    right_moving_to_p += 1
                else:
                    max_moving_steps += left_moving_step
                    left_p = left_and_right_p_of_same_char[left_p]["left"]
                    left_moving_to_p -= 1
            elif left_p is None and right_p is not None:
                max_moving_steps += right_moving_step
                right_p = left_and_right_p_of_same_char[right_p]["right"]
                right_moving_to_p += 1
            elif left_p is not None and right_p is None:
                max_moving_steps += left_moving_step
                left_p = left_and_right_p_of_same_char[left_p]["left"]
                left_moving_to_p -= 1
            elif left_p is None and right_p is None:
                break
        if max_moving_steps > m:
            max_length = max(max_length,right_moving_to_p-left_moving_to_p - 2)
        else:
            max_length = max(max_length,right_moving_to_p-left_moving_to_p - 1)
        #print(f"single_index:{single_index},not_moving_char:{not_moving_char}")
        #print(f"max_moving_steps:{max_moving_steps},{right_moving_to_p-left_moving_to_p}")


    return max_length


if __name__ == "__main__":
    s,m = "hspxmbqwrlhxuzpfkhrezotvanhkkh",20
    print(get_max_length_of_substring_has_same_characters_after_exchaing(s,m))
