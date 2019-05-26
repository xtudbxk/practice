# we complete the code for kd tree in this file

import heapq
from collections import deque

class kd_node:
    def __init__(self,examples=None,cut_dimension_index=None,cut_value=None):
        self.examples,self.cut_dimension_index,self.cut_value = examples,cut_dimension_index,cut_value
        self.top,self.left,self.right = None,None,None

class kd_tree:
    def __init__(self,datas):
        self.datas = datas
        self.root = kd_node()
        self.root.top = None
        processed_datas = self._process_datas(datas)
        self.build_tree(self.root,processed_datas,0)

    def _process_datas(self,datas):
        return [[-1,single_data] for single_data in datas]

    def build_tree(self,cur_node,datas,feature_id):
        left_datas = []
        right_datas = []
        mid_len = len(datas) // 2 + 1
        #print(f"mid_len:{mid_len}")
        for data_index,single_data in enumerate(datas):
            _,single_data = single_data
            if len(right_datas) < mid_len:
                heapq.heappush(right_datas,[single_data["x"][feature_id],single_data])
            else:
                poped_data = heapq.heappushpop(right_datas,[single_data["x"][feature_id],single_data])
                heapq.heappush(left_datas,[-poped_data[0],poped_data[1]])
        #print(f"datas:{datas}")
        #print(f"left_datas:{left_datas}")
        #print(f"right_datas:{right_datas}")
        mid_value = right_datas[0][0]
        mid_datas = []
        while(len(right_datas) > 0 and right_datas[0][0] == mid_value):
            mid_datas.append( heapq.heappop(right_datas)[1] )
        while(len(left_datas) > 0 and left_datas[0][0] == -mid_value):
            mid_datas.append( heapq.heappop(left_datas)[1] )
        #print(f"mid_datas:{mid_datas}")
        #print(f"left_datas:{left_datas}")
        #print(f"right_datas:{right_datas}")

        cur_node.examples = mid_datas
        cur_node.cut_dimension_index = feature_id
        cur_node.cut_value = mid_value

        if len(left_datas) > 0:
            cur_node.left = kd_node()
            cur_node.left.top = cur_node
            self.build_tree(cur_node.left,left_datas, (feature_id+1)%len(mid_datas[0]["x"]))
        if len(right_datas) > 0:
            cur_node.right = kd_node()
            cur_node.right.top = cur_node
            self.build_tree(cur_node.right,right_datas, (feature_id+1)%len(mid_datas[0]["x"]))

        return cur_node

    def search(self,k,target_data,tree=None,collected_datas=None):
        tree = tree if tree is not None else self.root
        collected_datas = collected_datas if collected_datas is not None else []
        #print(f"k:{k}, target_data:{target_data}")
        #print(f"tree:{tree.examples},\ncollected_datas:{collected_datas}")

        # go to the leaf node
        cur_node = tree
        while(cur_node.left is not None or cur_node.right is not None):
            if cur_node.left is not None and cur_node.right is not None:
                if cur_node.cut_value <= target_data["x"][cur_node.cut_dimension_index]:
                    cur_node = cur_node.right
                else:
                    cur_node = cur_node.left
            else:
                cur_node = cur_node.left if cur_node.left is not None else cur_node.right

        # find k nearest nodes
        while(cur_node is not None):
            # search in cur_node
            #print(f"cur_node:{cur_node.examples}")
            for single_example in cur_node.examples:
                distance = sum([(single_example["x"][feature_index]-target_data["x"][feature_index])**2 for feature_index in range(len(target_data["x"]))])
                if len(collected_datas) < k:
                    heapq.heappush(collected_datas, [-distance,single_example])
                else:
                    heapq.heappushpop(collected_datas, [-distance,single_example])
            # search in brother node
            if cur_node is tree: break
            distance_to_cut_plane = (cur_node.top.examples[0]["x"][cur_node.top.cut_dimension_index] - collected_datas[0][1]["x"][cur_node.top.cut_dimension_index])**2
            #print(f"distance_to_cut_plane:{distance_to_cut_plane}")
            #print(f"-collected_datas:{-collected_datas[0][0]}")
            if distance_to_cut_plane < -collected_datas[0][0]:
                #print("overlapped")
                brother_node = None
                if cur_node == cur_node.top.left:
                    brother_node = cur_node.top.right 
                elif cur_node == cur_node.top.right:
                    brother_node = cur_node.top.left
                if brother_node is not None:
                    #print(f"in _search brother_node:{brother_node.examples}")
                    self.search(k,target_data,tree=brother_node,collected_datas=collected_datas)

            #print("go to top")
            cur_node = cur_node.top

        return collected_datas

    def display_tree(self):
        display_stack = deque([[self.root]])
        layer_index = 0
        while(len(display_stack) > 0):
            items_of_this_layer = display_stack.popleft()
            next_layer_items = []
            for item_index,single_item in enumerate(items_of_this_layer):
                if layer_index <= 0:
                    print("root:",end=" ")
                else:
                    if item_index % 2 == 0:
                        print(f"{layer_index}th layer {item_index//2}th item left",end=" ")
                    else:
                        print(f"{layer_index}th layer {item_index//2}th item right",end=" ")
                if single_item is not None:
                    for single_example in single_item.examples:
                        print(single_example,end=" ")
                    print("")
                    next_layer_items.append(single_item.left)
                    next_layer_items.append(single_item.right)
                else:
                    print("None")
                    next_layer_items.append(None)
                    next_layer_items.append(None)
            for item in next_layer_items:
                if item is not None:
                    display_stack.append(next_layer_items)
                    break
            layer_index += 1
            print("\n")
        print("\n\n")


if __name__ == "__main__":
    datas =  [{"x":(2,3),"y":0},{"x":(5,4),"y":0},{"x":(9,6),"y":0},{"x":(4,7),"y":0},{"x":(8,1),"y":0},{"x":(7,2),"y":0}] 
    a = kd_tree(datas)
    a.display_tree()
    b = a.search(3,{"x":(2,3),"y":0})
    print(f"search result:{b}")
