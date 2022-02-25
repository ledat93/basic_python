'''
A linked list can be a sequence of data elements that are linked.
Each data element can be connected in form of a pointer.

Node => data value and next value
The first node => head

This example will be: create a linked list; insert or update a new value; remove a value in list.
'''
##########################
## CREATE A LINKED LIST
##########################
class Node:
    def __init__(self, val = None):
        self.data_cell = val
        self.next_cell = None

class SimpleLinkedList:
    def __init__(self):
        self.head_node = None
        
    def print_elements(self):
        item = self.head_node
        while item is not None:
            print(item.data_cell)
            item = item.next_cell

####################################################
## INSERT, UPDATE, REMOVE A VALUE IN THE LINKED LIST
####################################################
## CASE 1: insert new data into a linked list
## here, the current head node will become the second code and created node => begining
## in end insert, the current last node will become the second last node and new node is last.
## in middle insert, there are two nodes: 1 exist node and new node with new data
##      => the next cell of the exist node will be pointer into new_node.
class InsertingLinkedList:
    def __init__(self):
        self.head_node = None
        
    def print_elements(self):
        item = self.head_node
        while item is not None:
            print(item.data_cell)
            item = item.next_cell
            
    def insert_begining(self, new_val):
        new_node = Node(new_val)        
        ## update new node at the begining
        new_node.next_cell = self.head_node
        self.head_node = new_node
    
    def insert_end(self, new_data):
        new_node = Node(new_data)
        if self.head_node is None:
            self.head_node = new_node
        end_node = self.head_node
        while end_node.next_cell:            
            end_node = end_node.next_cell
        end_node.next_cell = new_node
    
    def insert_middle(self, new_node, new_data):
        if new_node is Node:
            print('The mentional node is nothing')
            return
        node = Node(new_data)
        node.next_cell = new_node.next_cell
        new_node.next_cell = node

## CASE 2: remove a data in the linked list
## here, to remove a item in linked list, we use the key for that node and the position of delected node
## is for next node.
    def remove(self, key):
        head = self.head_node
        if head is not None:            
            if head.data_cell == key:
                self.head_node = head.next_cell
                head = None
                return
        elif head is None:
            return
        while head is not None:            
            if head.data_cell == key:
                break
            previous = head
            head = head.next_cell
        
        previous.next_cell = head.next_cell
        head = None
    
lst = [i for i in range(5)]
llist = InsertingLinkedList()
##create nodes
llist.head_node = Node(lst[0])
nodes = list()
for e in lst[1:]:
    nodes.append(Node(e))    
## link nodes
llist.head_node.next_cell = nodes[0]
for j in range(len(nodes)-1):
    nodes[j].next_cell = nodes[j+1]

llist.print_elements()
llist.insert_begining(-10)
llist.insert_end(8)
llist.insert_middle(nodes[1].next_cell, 7)
llist.remove(1)
llist.print_elements()
