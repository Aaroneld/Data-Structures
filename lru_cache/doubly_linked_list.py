"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, key, value, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.key = key
        self.add_key(key, value)
            
    def __str__(self):
        return f"value: {getattr(self, self.key)}"

    def add_key(self, key, value = None):
        if value != None:
            setattr(self, key, value)
        else:
            setattr(self, key, key)

"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        if self.head == None:
            return 0
        elif self.head == self.tail:
            return 1 
        else:
            currentNode = self.head
            counter = 1 

            while currentNode != None:
                if currentNode.next != None:
                    counter += 1
            
                currentNode = currentNode.next

            return counter

    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, key, value):
      

        if self.head == None:
            self.head = self.tail = ListNode(key, value)
        elif self.tail == self.head:
            self.head = ListNode(key, value, None, self.tail)
            self.tail.prev = self.head
        else:
            shiftedHead = self.head
            self.head = ListNode(key, value, None, shiftedHead)
            shiftedHead.prev = self.head
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        
        if self.head == None: 
            return None
        elif self.head == self.tail:
            self.head = self.tail = None
        elif self.length == 2:
            self.tail.prev = None
            self.head = self.tail
           
        else:
            self.head = self.head.next
            self.head.prev = None
         

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def __str__(self):

        currentNode = self.head

        while currentNode != None:
            if currentNode:
                print(currentNode)
            currentNode = currentNode.next

    def contains(self, key):

        currentNode = self.head;

        while currentNode != None:

            if currentNode and currentNode.key == key:
                return {"node": currentNode, "value": getattr(currentNode, key)}

            currentNode = currentNode.next
        
        return None

    def add_to_tail(self, key, value):
        
        if self.tail == None:
            self.tail = self.head = ListNode(key, value)
        elif self.tail == self.head:
            self.tail = ListNode(key, value, self.head)
            self.head.next = self.tail
        else:
            shiftedTail = self.tail
            self.tail = ListNode(key, value, shiftedTail)
            shiftedTail.next = self.tail
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail == None: 
            return None;
        elif self.tail == self.head:
            self.tail = self.head = None

        elif self.length == 2:
            self.tail = self.head
        else:
            self.tail = self.tail.prev
            self.tail.next = None 

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        
        if self.head == None or self.head == node:
            pass
        elif self.length == 2:
            self.tail = self.head
            self.head.prev = None
            self.add_to_head(node.key, getattr(node, node.key))
        elif self.tail == node:
            self.tail = self.tail.prev
            self.tail.next = None 
            self.add_to_head(node.key, getattr(node, node.key))
        else:
            prevNode = node.prev
            nextNode = node.next

            prevNode.next = nextNode
            nextNode.prev = prevNode

            self.add_to_head(node.key, getattr(node, node.key)) 
        
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.head == None or self.tail == node:
            pass
        elif self.length == 2:
            self.head = self.tail
            self.head.prev = None
            self.add_to_tail(node.key, getattr(node, node.key))

        elif self.head == node:
            self.head = self.head.next
            self.head.prev = None
            self.add_to_tail(node.key, getattr(node, node.key))
        else:
            prevNode = node.prev
            nextNode = node.next

            prevNode.next = nextNode
            nextNode.prev = prevNode

            self.add_to_tail(node.key, getattr(node, node.key))

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        
        if self.head == None:
            pass
        elif self.head == node: 
            self.remove_from_head()

        elif self.tail == node:
            self.remove_from_tail()
        else:
            nextNode = node.next
            prevNode = node.prev

            nextNode.prev = prevNode
            prevNode.next = nextNode

                

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        
        if self.head == None:
            return None
        elif self.head == self.tail:
            return self.head.value
        elif self.length == 2:
            return self.head.value if self.head.value > self.tail.value else self.tail.value 
        else:
            currentNode = self.head
            currentMax = self.head.value 

            while currentNode != None: 
                if currentNode.next == None or currentMax > currentNode.next.value:
                    pass
                else:
                    currentMax = currentNode.next.value
                
                currentNode = currentNode.next 
            
            return currentMax


# dll = DoublyLinkedList(ListNode("key1", 1))
# dll.add_to_tail("key2", 2)
# dll.add_to_tail("key3", 3)
# dll.add_to_tail("key4", 4)

# print(dll.contains("key5"))