
class LinkedList:

    head = None
    tail = None

    
    def __len__(self):

        counter = 0 

        if self.head == None:
            return 0
        
        currentNode = self.head
        
        while counter != "None":
    
            if(currentNode):  
                counter += 1
                currentNode = currentNode.node["nextNode"]
            else: return counter
    
    def add_to_tail(self, value):
        node = Node(value)

        if self.head == None:
            self.head = node
            self.tail = node 
        else :
            self.tail.addNextNode(node)
            self.tail = node

    def remove_head(self):
        if self.head != None:
            value = self.head.getValue()
            self.head = self.head.node["nextNode"]
            if not self.head:
                self.tail = None
    
            return value
        else: return None
    
    def remove_tail(self):

        node = self.tail;

        if self.tail == self.head:
            self.tail = self.head = None
            return node.getValue()

        currentNode = self.head

        while currentNode.node["nextNode"] != None:
        
            if currentNode.node["nextNode"].node["nextNode"] != None:
                currentNode = currentNode.node["nextNode"]
            else: 
                 currentNode.node["nextNode"] = None
                 break;
        
        self.tail = currentNode
        self.tail.node["nextNode"] = None
        return node.getValue()
        

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

    value = None

    def __init__(self, value):
        self.node = {
            'value': value,
            'nextNode': None 
        }
        self.value = value

    def addNextNode(self, node):
        self.node["nextNode"] = node

    def __str__(self):
        return str(self.node)

    def getValue(self):
        return self.node['value']
    
    def contains(self, value):
        if self.node['value'] == value: return True
        else: return False 

