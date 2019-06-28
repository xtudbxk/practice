
def quick_sort(datas,low=None,high=None):
    if low is None:
        low,high = 0,len(datas)-1
    else:
        if low == high: return 
    #print(f"low:{low},high:{high}")
    p_to_middle,p_to_other = low,high
    while(p_to_middle != p_to_other):
        if p_to_middle > p_to_other:
            if datas[p_to_middle] >= datas[p_to_other]:
                p_to_other += 1
            else:
                datas[p_to_middle],datas[p_to_other] = datas[p_to_other],datas[p_to_middle]
                p_to_middle,p_to_other = p_to_other,p_to_middle
                p_to_other -= 1
        else:
            if datas[p_to_middle] <= datas[p_to_other]:
                p_to_other -= 1
            else:
                datas[p_to_middle],datas[p_to_other] = datas[p_to_other],datas[p_to_middle]
                p_to_middle,p_to_other = p_to_other,p_to_middle
                p_to_other += 1
    if low < p_to_middle:
        quick_sort(datas,low=low,high=p_to_middle-1)
    if high > p_to_middle:
        quick_sort(datas,low=p_to_middle+1,high=high)
    return datas

if __name__ == "__main__":
    datas = [1,2,5,32,5,2,1,7,8,9,4,3,2]
    print(f"origin:{datas}")
    print(f"quick sort:{quick_sort(datas)}")
        
