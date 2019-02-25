class Node(object):
    def __init__(self, data=None, next_node=None):
        """Initialize with a single datum and set pointer to next node
        if no next node then point to none (null)"""
        self.data = data
        self.next = next_node

    def get_data(self):
        """get value of current node"""
        return self.data

    def get_next(self):
        """get current node's pointer to next """
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        """set the next pointer to add the next node"""
        self.next = new_next


class LinkedList(object):
    """Initialize the LinkedList 'head' has no nodes when initialized
    so default head to None (null)"""
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        # return T/F depending on whether the head of the linked list is null or not
        return self.head is None

    def append_data(self, val_to_append):
        # check to see if LinkedList is None
        if self.is_empty():
            # create 1st node with value
            new_node = Node(val_to_append)
            # designate the newly created node as the head
            self.head = new_node
        else:  # traverse the list
            current = self.head
            # keep traversing list until the current node points to None, indicating end of linked list
            while current.get_next() is not None:
                current = current.get_next()
            # once next is None, create the new node
            add_node = Node(val_to_append)
            # set the pointer on the current
            current.next = add_node

    def prepend_data(self, val_to_prepend):
        # create a new node object with provided value
        new_node = Node(val_to_prepend)
        # the new_node default next is None/null so set this node's next (pointer)
        # to current LinkedList object's head
        new_node.set_next(self.head)
        # reset the head of the LinkedList object to the node just created
        self.head = new_node

    def print_values(self):
        result = []
        if self.is_empty():
            result = "The Linked List is empty."
        else:  # traverse the list
            current = self.head
            while current.get_next() is not None:
                result += current.get_data()

        return result

    def remove_node(self, val_to_remove):
        if self.is_empty():
            # handle an empty list
            return "the LinkedList is empty"
        else:  # traverse the list until the value is found
            current = self.head
            previous = None
            while current.get_data is not val_to_remove:
                previous = current
                current = current.get_next()
                # handle the case that the value is not in the list
                if current is None:
                    return "the value is not in the linkedlist"
            # when value is found set the previous node's pointer to the
            # current node's next
            previous.set_next(current.get_next())


