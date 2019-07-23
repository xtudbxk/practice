
# 一个含有n个元素的数组，元素值的范围在1~n, 有些元素出现了两次，一些出现了一次，找到所有没出来的数字

def find_missing_numbers(array):
    for index in range(len(array)):
        while array[index] != index+1 and array[array[index]-1] != array[index]:
            tmp = array[index]
            array[index] = array[tmp-1]
            array[tmp-1] = tmp
            #array[index],array[array[index]-1] = array[array[index]-1],array[index] # bad in python

    missing_numbers = []
    for index in range(len(array)):
        if array[index] != index+1:
            missing_numbers.append(index+1)

    return missing_numbers

if __name__ == "__main__":
    array = [1,1,2,5,3,4,5,7]
    print(f"array:{array},missing:{find_missing_numbers(array)}")




