
class LinkedList:

    head = None
    tail = None
    
    def add_to_tail(self, value):
        node = Node(value)

        if self.head == None:
            self.head = node
            self.tail = node 
        else :
            self.tail.next = node
            self.tail = node
    
    
    def __len__(self):

        counter = 0 
        currentNode = self.head

        while counter != "None":
            
            if(currentNode):
                counter += 1
                currentNode = currentNode.node["nextNode"]
            else: return counter

    def remove_head(self):
        if self.head != None:
            value = self.head.getValue()
            self.head = self.head.node["nextNode"]
            if not self.head:
                self.tail = None
                print(self.tail)
            return value
        else: return None
    
    def contains(self, value):
        
        if(self.head):
             currentNode = self.head
             returnValue = currentNode.contains(value)
             while returnValue != None:
                 returnValue = currentNode.contains(value)
            
                 if returnValue: 
                     return True
                 elif currentNode.node['nextNode'] != None:
                     currentNode = currentNode.node['nextNode']
                 else: 
                     return False 
        else: return False 

    def getHead(self):
        return self.head.__str__()

    def get_max(self): 

        if not self.head: return None

        currentNode = self.head
        maxValue = currentNode.getValue()

        while maxValue != None:
            currentNode = currentNode.node["nextNode"]

            if not currentNode: 
                return maxValue
            elif(maxValue < currentNode.getValue()):
                maxValue = currentNode.getValue()



class Node:

    def __init__(self, value, next = None):
        self.next = None
        self.value = value

    def addNextNode(self, node):
        self.next = node

    def __str__(self):
        return str(self.value)

    def getValue(self):
        return self.value
    
    def contains(self, value):
        if self.value == value: return True
        else: return False 

