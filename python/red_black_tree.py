# 红黑树实现

# 树节点
class Node():
    def __init__(self,value,color="black"):
        self.value = value
        self.left = None
        self.right = None
        self.top = None
        self.color = color

class RedBlackTree():
    def __init__(self):
        self.root = Node(None) # value为None即为叶节点

    # 左旋
    def left_rotate(self,node):
        top_node = node.top
        right_node = node.right
        assert right_node is not None,"right child node is None while left rotating"
        right_left_node = right_node.left
    
        right_node.top = top_node
        right_node.left = node
        node.top = right_node
        node.right = right_left_node
    
        if top_node is not None:
            if top_node.left is node:
                top_node.left = right_node
            else:
                top_node.right = right_node
    
        return right_node
    
    # 右旋
    def right_rotate(self,node):
        top_node = node.top
        left_node = node.left
        assert left_node is not None,"left child node is None while left rotating"
        left_right_node = left_node.right
    
        left_node.top = top_node
        left_node.right = node
        node.top = left_node
        node.left = left_right_node
    
        if top_node is not None:
            if top_node.left is node:
                top_node.left = left_node
            else:
                top_node.right = left_node
    
        return left_node

    # 插入
    def insert(self,value):
        # find the position to insert
        search_node = self.root
        while(search_node.value is not None):
            if search_node.value > value:
                search_node = search_node.left
            else:
                search_node = search_node.right
        # insert a new node
        new_node = Node(value)
        new_node.top = search_node.top
        new_node.left = Node(None)
        new_node.right = Node(None)
        if search_node.top is not None:
            if search_node.top.left is search_node:
                search_node.top.left = new_node
            else:
                search_node.top.right = new_node

        # set color to red
        new_node.color = "red"

        while(True):
            # if new_node is root, over
            if new_node.top is None:
                new_node.color = "black"
                return True

            # if color of father node is "black", over
            if new_node.top.color == "black":
                return True

            # if color of uncle node is red
            if new_node.top.top.right.color == "red":
                new_node.top.color = "black"
                new_node.top.top.right.color = "black"
                new_node.top.top.color = "red"
                new_node = new_node.top.top 
                continue

            # if color of uncle node is black
            # if father node is left child of grandfather node and new_node is right chld of father node, left rotate along father node
            if new_node.top.right is new_node and new_node.top.top.left is new_node.top: 
                self.left_rotate(new_node.top)
                new_node = new_node.left # the old father node

            # if father node is right child of grandfather node and new_node is left chld of father node, right rotate along father node
            if new_node.top.left is new_node and new_node.top.top.right is new_node.top: 
                self.right_rotate(new_node.top)
                new_node = new_node.right # the old father node

            # if father node is left child of grandfather node and new_node is left chld of father node
            if new_node.top.left is new_node:
                new_node.top.top.color = "red"
                new_node.top.color = "black"
                self.right_rotate(new_node.top.top)
                return True

            # if father node is right child of grandfather node and new_node is right chld of father node
            if new_node.top.right is new_node:
                new_node.top.top.color = "red"
                new_node.top.color = "black"
                self.left_rotate(new_node.top.top)
                return True

    def search(self,value):
        # find the position to insert
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
        if search_node.right.value is not None:
            delete_node = search_node
        else:
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
        replace_node.top = delete_node.top
        if delete_node.top is not None:
            if delete_node.top.right is delete_node:
                delete_node.top.right = replace_node
            else:
                delete_node.top.left = replace_node

        # check color of delete_node
        if delete_node.color == "red":
            return True

        # then we need to add an extra "black" for the replace_node
        while(True):
            if replace_node.color == "red": # add a "black" by set replace node to "black"
                replace_node.color = "black"
                return True
            if replace_node.top is None: # replace node is root, then we don't need to add an extra "black"
                return True
            
            top_node = replace_node.top
            if top_node.left is replace_node:
                brother_node = top_node.right
            else:
                brother_node = top_node.left

            # if 



        



