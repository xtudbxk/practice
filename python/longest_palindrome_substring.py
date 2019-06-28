
def get_max_length_of_substring_palindrome(string):
    new_string = "#".join(list(string))
    new_string = f"#{new_string}#"

    middle_index_of_one_palindrome,right_index_of_one_palindrome = -1,-1 # the one which rightest char has max index
    max_length_of_palindrome_between_index = []
    #print(f"new_string:{new_string}")
    for char_index,char in enumerate(new_string):
        if char_index <= right_index_of_one_palindrome:
            corresponding_char_index = 2*middle_index_of_one_palindrome - char_index
            if max_length_of_palindrome_between_index[corresponding_char_index] < 2*(right_index_of_one_palindrome - char_index)+1:
                max_length_of_palindrome_between_index.append(max_length_of_palindrome_between_index[corresponding_char_index])
            else:
                max_length_of_palindrome_between_index.append(2*(right_index_of_one_palindrome-char_index)+1)
                left,right = 2*char_index - right_index_of_one_palindrome-1,right_index_of_one_palindrome+1
                while(left >= 0 and right < len(new_string) and new_string[left] == new_string[right]):
                    left,right = left-1, right+1
                    max_length_of_palindrome_between_index[-1] += 2
        else:
            max_length_of_palindrome_between_index.append(1)
            left,right = char_index-1, char_index+1
            #print(f"left:{left},{new_string[left]},right:{right},{new_string[right]}")
            while(left >= 0 and right < len(new_string) and new_string[left] == new_string[right]):
                left,right = left-1, right+1
                max_length_of_palindrome_between_index[-1] += 2
        #if max_length_of_palindrome_between_index[-1] >= 2*(right_index_of_one_palindrome-middle_index_of_one_palindrome)+1:
        #    middle_index_of_one_palindrome = char_index
        #    right_index_of_one_palindrome = char_index + max_length_of_palindrome_between_index[-1] // 2
        if max_length_of_palindrome_between_index[-1]//2 + char_index > right_index_of_one_palindrome:
            middle_index_of_one_palindrome = char_index
            right_index_of_one_palindrome = max_length_of_palindrome_between_index[-1]//2 + char_index
        #print(f"char:{char},index:{char_index},length:{max_length_of_palindrome_between_index}")
    return right_index_of_one_palindrome-middle_index_of_one_palindrome


if __name__ == "__main__":
    string = "2123321"
    #string = "212333321"
    print(f"string:{string}")
    print(f"max length of substring palindrome:{get_max_length_of_substring_palindrome(string)}")




