"""Create a Python program that implements a singly linked list using Object-Oriented Programming (OOP) principles. Your implementation should 
include the following: A Node class to represent each node in the list. A LinkedList class to manage the nodes, with methods to: Add a node to the 
end of the list Print the list Delete the nth node (where n is a 1-based index) Include exception handling to manage edge casessuch as:
Deleting a node from an empty list Deleting a node with an index out of range Test your implementation with at least one sample list."""
class Node:
    """
    Node class to represent each node in the linked list.
    Each node contains data and a reference to the next node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    LinkedList class to manage the nodes with various operations.
    Implements singly linked list using OOP principles.
    """
    
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
        self.size = 0
    
    def add_node(self, data):
        """
        Add a node to the end of the list.
        
        Args:
            data: The data to be stored in the new node
        """
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.size += 1
        print(f"Added node with data: {data}")
    
    def print_list(self):
        """
        Print all elements in the linked list.
        """
        if not self.head:
            print("List is empty")
            return
        
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print("Linked List: " + " -> ".join(elements) + " -> None")
    
    def delete_nth_node(self, n):
        """
        Delete the nth node from the linked list (1-based indexing).
        
        Args:
            n (int): The position of the node to delete (1-based index)
            
        Raises:
            ValueError: If the list is empty
            IndexError: If the index is out of range
        """
        #handling empty list
        if not self.head:
            raise ValueError("Cannot delete from an empty list")
        
        #handling index out of range
        if n < 1 or n > self.size:
            raise IndexError(f"Index {n} is out of range. List has {self.size} elements.")
        
        #special case: deleting the first node (head)
        if n == 1:
            deleted_data = self.head.data
            self.head = self.head.next
            self.size -= 1
            print(f"Deleted node at position {n} with data: {deleted_data}")
            return
        
        #finding the node before the one to be deleted
        current = self.head
        for i in range(1, n - 1):
            current = current.next
        
        #sttoring the node that is to be deleted
        node_to_delete = current.next
        deleted_data = node_to_delete.data
        
        #here i am updating the link to skip the node to be deleted
        current.next = node_to_delete.next
        
        self.size -= 1
        print(f"Deleted node at position {n} with data: {deleted_data}")
    
    def get_size(self):
        """
        Get the current size of the linked list.
        
        Returns:
            int: The number of nodes in the list
        """
        return self.size
    
    def is_empty(self):
        """
        Check if the linked list is empty.
        
        Returns:
            bool: True if the list is empty, False otherwise
        """
        return self.head is None

#testing the implementation
def test_linked_list():
    """
    Test function to demonstrate the linked list implementation.
    """
    print(" this marks the beginning of the testing of linked list implementation\n")
    
    #creating a new linked list
    ll = LinkedList()
    
    #test no. 1 printing the empty list
    print("printing the empty list in test no.1")
    ll.print_list()
    print(f"Size: {ll.get_size()}")
    print(f"Is empty: {ll.is_empty()}\n")
    
    #test no. 2 adding nodes to the list
    print("adding nodes to the list in test no. 2")
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)
    ll.add_node(50)
    ll.print_list()
    print(f"Size: {ll.get_size()}\n")
    
    #test no. 3 deleting  middle node
    print("deleting  middle node in test no. 3")
    ll.delete_nth_node(3)
    ll.print_list()
    print(f"Size: {ll.get_size()}\n")
    
    #test no. 4 deleting the first node
    print("deleting the first node i.e head in test no. 4")
    ll.delete_nth_node(1)
    ll.print_list()
    print(f"Size: {ll.get_size()}\n")
    
    #test no. 5 deleting the last node
    print("deleting the last node in test no. 5")
    ll.delete_nth_node(ll.get_size())
    ll.print_list()
    print(f"Size: {ll.get_size()}\n")
    
    #test no. 6 exception handling for deleting from empty list
    print("exception handling for deleting from empty list")
    empty_list = LinkedList()
    try:
        empty_list.delete_nth_node(1)
    except ValueError as e:
        print(f"caught expected error: {e}")
    
    #test no. 7 exception handling  for index out of range
    try:
        ll.delete_nth_node(10)
    except IndexError as e:
        print(f"caught expected error: {e}")
    
    try:
        ll.delete_nth_node(0)
    except IndexError as e:
        print(f"caught expected error: {e}")
    
    print("\n all the tests are now successfully completed")

#here i am running the test
if __name__ == "__main__":
    test_linked_list()