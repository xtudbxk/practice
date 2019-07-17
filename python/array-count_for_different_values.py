# 排序数组中绝对值不同的个数

# 首尾双指针扫描
def get_count_of_different_values(sorted_array):
    head,tail = 0,len(sorted_array)-1
    count = 0
    while(head!=tail):
        if abs(sorted_array[head]) < abs(sorted_array[tail]):
            count += 1
            tail -= 1
        elif abs(sorted_array[head]) > abs(sorted_array[tail]):
            count += 1
            head += 1
        else:
            tail -= 1
    count += 1
    return count

if __name__ == "__main__":
    import random
    sorted_array = [random.randint(-10,10) for _ in range(15)]
    sorted_array.sort()
    print(f"sorted_array:{sorted_array}")
    print(f"count:{get_count_of_different_values(sorted_array)}")

