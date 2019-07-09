# 红黑树实现

# 
def get_direction(node1,node2):
    return "left" if node1.left is node2 else ("right" if node1.right is node2 else ("top" if node1.top is node2 else None))
def get_other_direction(direction):
    return "left" if direction is "right" else "right"

# 树节点
class Node():
    def __init__(self,value,color="black"):
        self.value = value
        self.top = None
        self.left = None
        self.right = None
        self.color = color

    def __getitem__(self,key): # now, we can use node["top"] to replace node.top
        return super(Node,self).__getattribute__(key)
    def __setitem__(self,key,value):
        return super(Node,self).__setattr__(key,value)

# 红黑树
class RedBlackTree():
    def __init__(self):
        self.root = Node(None) # value为None即为叶节点

    def rotate(self,node,direction):
        other_direction = get_other_direction(direction)
        assert node[other_direction] is not None, f"{other_direction} child node is None when {direction} rotating"

        top_node = node["top"]
        node[other_direction]["top"] = top_node
        tmp_node = node[other_direction][direction]
        node[other_direction][direction] = node
        node["top"] = node[other_direction]
        node[other_direction] = tmp_node
        tmp_node["top"] = node
        if top_node is not None:
            top_node[get_direction(top_node,node)] = node["top"]
        else: # root
            self.root = node["top"]

        return node["top"]

    # 插入
    def insert(self,value):
        # find the position to insert
        search_node = self.root
        while(search_node.value is not None):
            if search_node.value > value:
                search_node = search_node["left"]
            else:
                search_node = search_node["right"]

        # insert a new node
        new_node = Node(value)
        new_node["top"] = search_node["top"]
        new_node["left"] = Node(None)
        new_node["left"].top = new_node
        new_node["right"] = Node(None)
        new_node["right"].top = new_node
        if new_node["top"] is not None:
            new_node["top"][get_direction(new_node["top"],search_node)] = new_node

        # set color to red
        new_node.color = "red"

        while(True):
            # if new_node is root, over
            if new_node["top"] is None:
                new_node.color = "black"
                self.root = new_node
                return True

            # if color of father node is "black", over
            if new_node["top"].color == "black":
                return True

            direction = get_direction(new_node["top"],new_node)
            other_direction = get_other_direction(direction)
            direction_for_top = get_direction(new_node["top"]["top"],new_node["top"])
            other_direction_for_top = get_other_direction(direction_for_top)

            # if color of uncle node is red
            if new_node["top"]["top"][other_direction_for_top].color == "red":
                new_node["top"].color = "black"
                new_node["top"]["top"][other_direction_for_top].color = "black"
                new_node["top"]["top"].color = "red"
                new_node = new_node["top"]["top"] 
                continue

            # if color of uncle node is black

            # if father node is left child of grandfather node and new_node is right chld of father node, left rotate along father node
            # or 
            # if father node is right child of grandfather node and new_node is left chld of father node, right rotate along father node
            if direction != direction_for_top:
                self.rotate(new_node["top"],direction_for_top)
                new_node = new_node[direction_for_top]

            # if father node is left child of grandfather node and new_node is left chld of father node
            # or
            # if father node is right child of grandfather node and new_node is right chld of father node
            new_node["top"]["top"].color = "red"
            new_node["top"].color = "black"
            self.rotate(new_node["top"]["top"],other_direction_for_top)
            return True

    def search(self,value):
        search_node = self.root
        while(search_node.value is not None):
            if search_node.value == value:
                return search_node
            elif search_node.value > value:
                search_node = search_node.left
            else:
                search_node = search_node.right
        return None

    def delete(self,value):
        # find the node to delete
        search_node = self.root
        while(search_node.value is not None):
            if search_node.value == value:
                break
            elif search_node.value > value:
                search_node = search_node.left
            else:
                search_node = search_node.right
        if search_node.value is None: # the value doesn't exist
            return False

        # find the node which replaces the searched node to be deleted
        if search_node.right.value is None:
            delete_node = search_node # no one can replace
        else:
            # the most left node in the right child tree
            delete_node = search_node.right
            while(delete_node.left.value is not None):
                delete_node = delete_node.left

        # move value of delete node to search_node
        search_node.value = delete_node.value

        # find replace node which replaces the deleted node in tree
        if delete_node.left.value is not None: # in case delete node is search node
            replace_node = delete_node.left
        else:
            replace_node = delete_node.right # in case delete node is the most left node in the right child tree of search node

        # replacing
        replace_node["top"] = delete_node["top"]
        if delete_node["top"] is not None:
            direction = get_direction(delete_node["top"],delete_node)
            delete_node["top"][direction] = replace_node

        # check color of delete_node
        if delete_node.color == "red":
            return True

        # then we need to add an extra "black" for the replace_node
        while(True):
            if replace_node.color == "red": # add a "black" by set replace node to "black"
                replace_node.color = "black"
                return True
            if replace_node["top"] is None: # replace node is root, then we don't need to add an extra "black"
                self.root = replace_node
                return True
            
            direction = get_direction(replace_node["top"],replace_node)
            other_direction = get_other_direction(direction)

            father_node = replace_node["top"]
            brother_node = father_node[other_direction]

            # if brother_node is red
            if brother_node.color == "red":
                brother_node.color = "black"
                father_node.color = "red"
                self.rotate(father_node,direction)
                continue

            if brother_node[other_direction].color == "black":
                if brother_node[direction].color == "black":
                    brother_node.color = "red"
                    replace_node = father_node
                    continue
                else:
                    brother_node[direction].color = "black"
                    brother_node.color = "red"
                    self.rotate(brother_node,other_direction)
                    continue

            brother_node.color = father_node.color
            father_node.color = "black"
            brother_node[other_direction].color = "black"
            self.rotate(father_node,direction)
            return True

    def display(self):
        import graphviz
        from collections import deque

        graph = graphviz.Digraph("display")
        nodes = deque([self.root])
        while(len(nodes) > 0):
            cur_node = nodes.popleft()
            if cur_node is None: continue
            graph.node(str(id(cur_node)),label=str(cur_node.value),shape="circle",color=cur_node.color)
            if cur_node.top is not None:
                graph.edge(str(id(cur_node.top)),str(id(cur_node)))
            nodes.append(cur_node.left)
            nodes.append(cur_node.right)
        import random
        graph.view("tmp_" + str(random.random()))

if __name__ == "__main__":
    RBTree = RedBlackTree()
    RBTree.insert(1)
    RBTree.insert(2)
    RBTree.insert(3)
    RBTree.insert(4)
    RBTree.insert(5)
    RBTree.insert(6)
    RBTree.insert(6)
    RBTree.insert(7)
    RBTree.insert(8)
    RBTree.insert(9)
    RBTree.insert(10)
    RBTree.insert(11)
    RBTree.insert(12)
    RBTree.insert(13)
    RBTree.insert(14)
    print(f"search 10:{RBTree.search(10)}")
    print(f"search 6:{RBTree.search(6)}")
    print(f"search 1:{RBTree.search(1)}")
    print(f"search 11:{RBTree.search(11)}")
    RBTree.delete(5)
    RBTree.delete(6)
    RBTree.delete(6)
    print(f"delete 6:{RBTree.delete(6)}")
    RBTree.delete(4)
    RBTree.delete(1)
    #RBTree.delete(5)
    RBTree.display()
