
class heap(): # minum-top heap
    def __init__(self,nums): 
        self.heap = nums
        self.heapify() # construct heap in-place

    def heapify(self):
        last_not_leaf_index = len(self.heap)//2-1
        for index in range(last_not_leaf_index,-1,-1):
            right_child_index = 2*index+2
            left_child_index = 2*index+1
            if right_child_index < len(self.heap) and self.heap[index] > self.heap[right_child_index]:
                self.heap[index],self.heap[right_child_index] = self.heap[right_child_index],self.heap[index]
            if self.heap[index] > self.heap[left_child_index]:
                self.heap[index],self.heap[left_child_index] = self.heap[left_child_index],self.heap[index]
    
    def pop(self):
        pop_num = self.heap[0]
        self.heap[0] = self.heap.pop() # list output the last number
        index = 0
        while(index < len(self.heap)):
            left_child_index = 2*index+1
            right_child_index = 2*index+2
            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[index]:
                if right_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[right_child_index]:
                    pass
                else:
                    self.heap[left_child_index],self.heap[index] = self.heap[index],self.heap[left_child_index]
                    index = left_child_index
                    continue
            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[index]:
                if self.heap[right_child_index] <= self.heap[left_child_index]:
                    self.heap[right_child_index],self.heap[index] = self.heap[index],self.heap[right_child_index]
                    index = right_child_index
                    continue
            break
        return pop_num

    def insert(self,single_num):
        self.heap.append(single_num)
        index = len(self.heap)-1
        while(index > 0):
            father_index = (index+1)//2-1
            if self.heap[father_index] > self.heap[index]:
                self.heap[father_index],self.heap[index] = self.heap[index],self.heap[father_index]
                index = father_index
            else:
                break

if __name__ == "__main__":
    import random
    nums = [random.randint(0,10) for _ in range(10)]
    print(f"origin nums:{nums}")

    h = heap(nums)
    print(f"heap:{h.heap}")

    h.insert(3)
    h.insert(5)
    h.insert(8)
    print(f"heap:{h.heap}")

    print(f"pop:{h.pop()},heap:{h.heap}")
    print(f"pop:{h.pop()},heap:{h.heap}")
    print(f"pop:{h.pop()},heap:{h.heap}")
