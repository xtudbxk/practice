
# 简单选择排序
def select_sort(nums):
    for index in range(len(nums)-1):
        min_value = nums[index]
        min_index = index
        for select_index in range(index+1,len(nums)):
            if min_value > nums[select_index]:
                min_value = nums[select_index]
                min_index = select_index
        nums[index],nums[min_index] = nums[min_index],nums[index]
    return nums

# 堆排序
import heapq
def heap_sort(nums):
    heap = [-single_num for single_num in nums] # heapq didn't support only treat part of list as a heap, so we here use an extra list to store the heap. And in origin heap_sort, we can sort without this extra list
    heapq.heapify(heap)
    for index in range(len(nums)-1,-1,-1): 
        nums[index] = -heapq.heappop(heap)
    return nums



if __name__ == "__main__":
    import random
    import time
    a = [random.randint(0,5000) for _ in range(5000)]
    b = a[:]

    s = time.time()
    select_sort(a)
    e = time.time()
    print(f"select sort:{e-s:.3}s")

    s = time.time()
    heap_sort(a)
    e = time.time()
    print(f"heap sort:{e-s:.3}s")
        


