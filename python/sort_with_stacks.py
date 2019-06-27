# 给一个栈，里面元素乱序，给一个相同大小的栈，和一个变量的位置，让写一个程序对这个进行排序

def sorts(stack1,stack2):
    while(len(stack1) > 0):
        element = stack1.pop()
        while(len(stack2) > 0 and stack2[-1] > element):
            stack1.append(stack2.pop())
        stack2.append(element)
    return stack2

if __name__ == "__main__":
    stack1 = [1,2,5,7,4,2,8,4,38,0,1,4,-3,6,4,3]
    stack2 = []
    print(f"before sort:{stack1}")
    print(f"after sort:{sorts(stack1,stack2)}")


