

# 简单插入排序
def insert_sort(nums):
    for sorted_index in range(len(nums)-1):
        need_to_insert_index = sorted_index + 1
        for check_index in range(sorted_index,-1,-1):
            if nums[check_index] >= nums[need_to_insert_index]:
                nums[check_index],nums[need_to_insert_index] = nums[need_to_insert_index],nums[check_index]
                need_to_insert_index = check_index
            else:
                break
    return nums

# 希尔增量排序
def shell_sort(nums):
    length = len(nums) // 2
    while(length >= 1):
        for sorted_index in range(len(nums)-length):
            need_to_insert_index = sorted_index + length
            for check_index in range(sorted_index,-1,-length):
                if nums[check_index] >= nums[need_to_insert_index]:
                    nums[check_index],nums[need_to_insert_index] = nums[need_to_insert_index],nums[check_index]
                    need_to_insert_index = check_index
                else:
                    break
        length //= 2
    return nums




if __name__ == "__main__":
    import random
    import time
    a = [random.randint(0,5000) for _ in range(5000)]
    b = a[:]

    s = time.time()
    insert_sort(a)
    e = time.time()
    print(f"insert_sort:{e-s:.3}s")


    s = time.time()
    shell_sort(b)
    e = time.time()
    print(f"shell_sort:{e-s:.3}s")
