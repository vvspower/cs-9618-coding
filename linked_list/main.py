# create a new linked list


NULL_POINTER = -1

class ListNode:
    def __init__(self):
        self.data = ""
        self.pointer = 0
    
    def __str__(self) -> str:
        return self.data    

start_pointer = 0 # integer

array = [ListNode() for x in range(0, 6)]


def initialize_list():
    global start_pointer 
    global free_list_ptr
    start_pointer = NULL_POINTER
    free_list_ptr = 0
    for x in range(0,5):
        print(x)
        array[x].pointer = x + 1
    array[5].pointer = NULL_POINTER




def insert_new_node(new_item):
    # check if there is space in the array
    if free_list_ptr != NULL_POINTER:
        new_node_ptr = free_list_ptr
        # data stored in node
        array[new_node_ptr].pointer = new_item
        # free list pointer points to next node
        free_list_ptr = array[free_list_ptr].pointer
        this_node_ptr = start_pointer
        while this_node_ptr != NULL_POINTER and array[this_node_ptr].data < new_item:
            previous_node_ptr = this_node_ptr
            this_node_ptr = array[this_node_ptr].pointer
        if previous_node_ptr == start_pointer:
            # inserting new node at the start of the list
            array[new_node_ptr].pointer = start_pointer
            start_pointer = new_node_ptr
        else:
            array[new_node_ptr].pointer = array[previous_node_ptr].pointer
            array[previous_node_ptr].pointer = new_node_ptr


def find_element(data_item):
    current_node_ptr = start_pointer
    while current_node_ptr != NULL_POINTER and array[current_node_ptr].data != data_item:
        current_node_ptr = array[current_node_ptr].pointer
    return current_node_ptr

#  baki deleting and finding is quite easy
