
# 归并排序
def merge_sort(nums):
    if len(nums) <= 1: return nums
    left_sorted_nums = merge_sort(nums[:len(nums)//2])
    right_sorted_nums = merge_sort(nums[len(nums)//2:])
    p_left,p_right = 0,0
    while(p_left<len(left_sorted_nums) and p_right < len(right_sorted_nums)):
        if left_sorted_nums[p_left] < right_sorted_nums[p_right]:
            nums[p_left+p_right] = left_sorted_nums[p_left]
            p_left += 1
        else:
            nums[p_left+p_right] = right_sorted_nums[p_right]
            p_right += 1
    while(p_left<len(left_sorted_nums)):
        nums[p_left+p_right] = left_sorted_nums[p_left]
        p_left += 1
    while(p_right<len(right_sorted_nums)):
        nums[p_left+p_right] = right_sorted_nums[p_right]
        p_right += 1
    return nums

if __name__ == "__main__":
    import random 
    a = [random.randint(0,100) for _ in range(100)]
    print(merge_sort(a))

