#  create a binary tree

NULL_POINTER = -1


class TreeNode:
    def __init__(self):
        self.data = ""
        self.left_pointer = 0
        self.right_pointer = 0


Tree = [TreeNode() for x in range(0, 7)]
print(Tree)


def initialize_tree():
    global root_pointer  # integer
    global free_ptr  # integer
    root_pointer = NULL_POINTER
    free_ptr = 0
    for x in range(0, 6):
        Tree[x].left_pointer = x + 1
    Tree[6].left_pointer = NULL_POINTER


def insert_node(new_item):
    # there is space in the array
    if free_ptr != NULL_POINTER:
        new_node_ptr = free_ptr
        free_ptr = Tree[free_ptr].left_pointer
        Tree[new_node_ptr].data = new_item
        Tree[new_node_ptr].left_pointer = NULL_POINTER
        Tree[new_node_ptr].right_pointer = NULL_POINTER
        if root_pointer == NULL_POINTER:
            root_pointer = new_node_ptr
        else:
            this_node_ptr = root_pointer
            while this_node_ptr != NULL_POINTER:
                prev_node_ptr = this_node_ptr
                if Tree[this_node_ptr].data > new_item:
                    turned_left = True
                    this_node_ptr = Tree[this_node_ptr].left_pointer
                else:
                    turned_left = False
                    this_node_ptr = Tree[this_node_ptr].right_pointer
            if turned_left == True:
                Tree[prev_node_ptr].left_pointer = new_node_ptr
                Tree[prev_node_ptr].right_pointer = new_node_ptr


def find_node(search_item):
    this_node_ptr = root_pointer
    while this_node_ptr != NULL_POINTER and Tree[this_node_ptr].data != search_item:
        if Tree[this_node_ptr].data > search_item:
            this_node_ptr = Tree[this_node_ptr].left_pointer
        else:
            this_node_ptr = Tree[this_node_ptr].right_pointer
