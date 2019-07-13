
# 冒泡排序
def exchange_sort(nums):
    for completed_index in range(len(nums),0,-1):
        for exchange_index in range(completed_index-1):
            if nums[exchange_index] > nums[exchange_index+1]:
                nums[exchange_index],nums[exchange_index+1] = nums[exchange_index+1],nums[exchange_index]
    return nums

# 快排
def quick_sort(nums):
    if len(nums) <= 1: return nums
    positions = [0,len(nums)-1]
    target_index_in_p = 0
    while(positions[0] != positions[1]):
        other_index_in_p = target_index_in_p ^ 0x01
        flag = (-1)**target_index_in_p
        if flag*nums[positions[target_index_in_p]] > flag*nums[positions[other_index_in_p]]:
            nums[positions[target_index_in_p]],nums[positions[other_index_in_p]] = nums[positions[other_index_in_p]],nums[positions[target_index_in_p]]
            positions[target_index_in_p] += flag
            target_index_in_p ^= 0x01
        else:
            positions[other_index_in_p] += -flag

    return quick_sort(nums[:positions[0]])+[nums[positions[0]]]+quick_sort(nums[positions[0]+1:])

if __name__ == "__main__":
    import random
    import time
    import sys

    a = [random.randint(0,5000) for _ in range(5000)]
    sys.setrecursionlimit(len(a))
    b = a[:]

    s = time.time()
    #print(exchange_sort(a))
    exchange_sort(a)
    e = time.time()
    print(f"exchange_sort:{e-s:.3}s")

    s = e
    #print(quick_sort(b))
    quick_sort(b)
    e = time.time()
    print(f"exchange_sort:{e-s:.3}s")
    
