EMPTY_STRING = ""
NULL_POINTER = -1
max_stack_size = 8
Stack = [EMPTY_STRING for x in range(0, max_stack_size)]

def initialize_stack():
    global base_of_stack_pointer 
    global top_of_stack_pointer
    base_of_stack_pointer = 0
    top_of_stack_pointer = NULL_POINTER
    print(Stack)


def push(new_item):
    global base_of_stack_pointer 
    global top_of_stack_pointer
    # to check is space in stack
    if top_of_stack_pointer < max_stack_size - 1:
        top_of_stack_pointer = top_of_stack_pointer + 1
        Stack[top_of_stack_pointer] = new_item
    print(Stack)

    
def pop():
    global base_of_stack_pointer 
    global top_of_stack_pointer
    item = EMPTY_STRING
    if top_of_stack_pointer > NULL_POINTER:
        # there is atleast one item in stack
        item = Stack[top_of_stack_pointer]
        top_of_stack_pointer = top_of_stack_pointer - 1
    return item



