# 使用倍增算法找到最低公共父节点

from collections import deque

# Tree
class Node:
    def __init__(self,value):
        self.value = value
        self.left,self.right = None,None

# find cls by 倍增 algorithms
def find_depth_and_jump_array(root):
    depth,jump = {},{}
    max_depth = 0
    nodes_queue = deque([root])
    while(len(nodes_queue)>0):
        cur_node = nodes_queue.popleft()
        if cur_node.value not in depth:
            depth[cur_node.value] = 1
            jump[cur_node.value] = [cur_node.value]
        if cur_node.left is not None:
            depth[cur_node.left.value] = depth[cur_node.value] + 1
            nodes_queue.append(cur_node.left)
            jump[cur_node.left.value] = [cur_node.value]
            max_depth = max(max_depth,depth[cur_node.left.value])
        if cur_node.right is not None:
            depth[cur_node.right.value] = depth[cur_node.value] + 1
            nodes_queue.append(cur_node.right)
            jump[cur_node.right.value] = [cur_node.value]
            max_depth = max(max_depth,depth[cur_node.right.value])

    # compute the left element in jump array by jump[i][j] = jump[jump[i][j-1]][j-1]
    j = 1
    while( 2**j < max_depth):
        for single_value in jump.keys():
            jump[single_value].append(jump[jump[single_value][j-1]][j-1])
        j += 1

    return depth,jump

def find_cls(query_pair_node,depth,jump):
    node1,node2 = query_pair_node
    if depth[node1] < depth[node2]:
        node2,node1 = node1,node2
    depth_diff = depth[node1] - depth[node2]

    # node1 jumps to the same depth with node2
    j = 0
    while(depth_diff > 0):
        if depth_diff & 0x01 > 0:
            node1 = jump[node1][j]
        depth_diff >>= 1
        j += 1

    # both node1 and node2 jumps
    if node1 is not node2:
        j_max = len(jump[node1])-1
        for j in range(j_max,-1,-1):
            if jump[node1][j] != jump[node2][j]:
                node1,node2 = jump[node1][j],jump[node2][j]

        return jump[node1][0]
    else:
        return node1

if __name__ == "__main__":
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    root.left.right.left = Node(7)
    root.left.right.right = Node(8)

    root.left.right.left.left = Node(9)

    depth,jump = find_depth_and_jump_array(root)
    print(f"depth:{depth}")
    print(f"jump:{jump}")
    print(find_cls((8,9),depth,jump))
    print(find_cls((5,9),depth,jump))
    print(find_cls((7,6),depth,jump))
