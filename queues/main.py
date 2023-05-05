# create new queue
EMPTY_STRING = ""
NULL_POINTER = -1
max_queue_size = 8
Queue = [EMPTY_STRING for x in range(max_queue_size)]


def initialize_queue():
    global front_of_queue_pointer
    global end_of_queue_pointer
    global number_in_queue

    front_of_queue_pointer = NULL_POINTER
    end_of_queue_pointer = NULL_POINTER
    number_in_queue = 0

def add_to_queue(new_item):
    # there is space in the queue
    if number_in_queue < max_queue_size:
        end_of_queue_pointer = end_of_queue_pointer + 1
        if end_of_queue_pointer > max_queue_size - 1:
            end_of_queue_pointer = 0
        Queue[end_of_queue_pointer] = new_item
        number_in_queue = number_in_queue + 1

def remove_from_queue():
    item = EMPTY_STRING
    if number_in_queue > 0:
        item = Queue[front_of_queue_pointer]
        number_in_queue = number_in_queue - 1
        # if the queue is now empty, reset the pointers
        if number_in_queue == 0:
            initialize_queue()
        else:
            front_of_queue_pointer = front_of_queue_pointer + 1
            # check for wrap around
            if front_of_queue_pointer > max_queue_size - 1:
                front_of_queue_pointer = 0
    return item

    