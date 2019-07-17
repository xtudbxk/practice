
# 由长度为length的array表示的整数，允计相邻位数交换，求n步交换内能得到的最小整数

# solver1
# 易知，要得最小整数，则应将从首个数字开始算的第一个降序数字进行交换(如 [3,2],[5,1]等，但[1,0]不用交换)
def get_max_exchanged_num(array,max_exchanged_num):
    exchange_p = 0
    while(exchange_p<len(array)-1):
        if array[exchange_p] > array[exchange_p+1] and (exchange_p != 0 or array[exchange_p+1] != 0):
            array[exchange_p],array[exchange_p+1] = array[exchange_p+1],array[exchange_p]
            max_exchanged_num -= 1
            if max_exchanged_num <= 0: break

            exchange_p2 = exchange_p
            while(array[exchange_p2] < array[exchange_p2-1] and (exchange_p2 != 1 or array[exchange_p2] != 0) and max_exchanged_num > 0):
                array[exchange_p2],array[exchange_p2-1] = array[exchange_p2-1],array[exchange_p2]
                max_exchanged_num -= 1
                exchange_p2 -= 1
            if max_exchanged_num <= 0: break
        exchange_p += 1
    return array


if __name__ == "__main__":
    array = [1,2,4,0,1,5,4,3,6,2,7,4]
    print(f"origin   :{array}")
    print(f"exchanged:{get_max_exchanged_num(array,1)}")
    array = [1,2,4,0,1,5,4,3,6,2,7,4]
    print(f"exchanged:{get_max_exchanged_num(array,3)}")
    array = [1,2,4,0,1,5,4,3,6,2,7,4]
    print(f"exchanged:{get_max_exchanged_num(array,5)}")
    array = [1,2,4,0,1,5,4,3,6,2,7,4]
    print(f"exchanged:{get_max_exchanged_num(array,7)}")
    array = [1,2,4,0,1,5,4,3,6,2,7,4]
    print(f"exchanged:{get_max_exchanged_num(array,10)}")
