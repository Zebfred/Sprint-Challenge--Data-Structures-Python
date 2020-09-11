class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    #gets value from node
    def get_value(self):
        return self.value

    #gets next value from node
    def get_next(self):
        return self.next_node

    #sets next value of node
    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    #adds value to the head node 
    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node
    #checks to see if the value is in the list
    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()
        return False

    """
     def reverse_list(self, node,prev):
        if node.next_node != None :
            self.reverse_list(node.next_node, prev=node)
        node.next_node = prev
        return

        next = node.next_node
        node.next_node = prev
        self.reverse_list(next, node)    
    """
    """
    def reverse_list(self, node, prev):
        if self.head is None:
            return
        # else maybe?     
        if node.next_node is None:
            self.head = prev
            return

        next = node.next_node
        node.next_node = prev
        self.reverse_list(next, node) 
    """    
    # reverses the list by taking the previous node's value from the current node's value    
    def reverse_list(self, current_node, prev):
        
        if current_node is None:
            self.head = prev
        else:
            next = current_node.next_node
            current_node.next_node = prev
            prev = current_node
            current_node = next
           
            self.reverse_list(current_node, prev)            