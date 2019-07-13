

def binary_search(datas,target):
    assert len(datas) > 0, "binary_search requires lenght of datas to be larger than 0"
    low,high = 0,len(datas)-1
    middle = (low+high)//2
    while(datas[middle]!=target and low <= high):
        if target > datas[middle]:
            low = middle+1
            middle = (low+high)//2
        else:
            high = middle-1
            middle = (low+high)//2
    middle = (low+high)//2
    if datas[middle] == target:
        return middle
    else:
        return None


if __name__ == "__main__":
    a = [1,2,3,5,6,7,8,11,15,17]
    print(f"a:{a}")
    print(f"search 1 in a, result:{binary_search(a,1)}")
    print(f"search 17 in a, result:{binary_search(a,17)}")
    print(f"search 7 in a, result:{binary_search(a,7)}")
    print(f"search 3 in a, result:{binary_search(a,3)}")
    print(f"search 4 in a, result:{binary_search(a,4)}")



