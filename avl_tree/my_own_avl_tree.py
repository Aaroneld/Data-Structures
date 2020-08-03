

class AVLTreeNode():

    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.height = 0 if value else -1
        self.right = right
        self.left = left

    def __str__(self):

        if not self.value:
            pass

        print(f"value: {self.value}, height: {self.height}")
        # print(f"value: {self.right.value}, height: {self.right.height}")
        # print(f"value: {self.left.value}, height: {self.left.height}")
        if self.left:
            self.left.__str__()
        if self.right:
            self.right.__str__()
        return "Done"

    def balance_tree(self):

        if self.height == 0 and not self.left and not self.right:
            return 0
        
        leftDepth = 0
        rightDepth = 0 

        if self.left: 
            
            leftDepth = self.left.get_branch_depth()
        
        if self.right:

            rightDepth = self.right.get_branch_depth()
        
        balance = abs(leftDepth - rightDepth)


        if balance > 1:
            if leftDepth > rightDepth:
                self.rotateRight()
            else:

                self.rotateLeft()

        return balance

    def get_branch_depth(self):

        maxDepth = self.height
      

        if self.left:
            depth = self.left.get_branch_depth()
            if depth > maxDepth:
                maxDepth = depth
        if self.right:
            depth = self.right.get_branch_depth()
            if depth > maxDepth:
                maxDepth = depth

    
        return maxDepth

    
    def rotateRight(self):

        left = self.left 
        self.left = None 

        rightQueue = self.dft()
        self.right = None

        maxNode = left.get_max()

        if maxNode != left:
        
            maxNodeQueue = left.right.dft()[1:]
            left.right = None
            leftQueue = left.dft()
            
            self.value = maxNode.value
            
            [self.insert(value, 1) for value in maxNodeQueue]
            [self.insert(value, 1) for value in leftQueue]
            [self.insert(value, 1) for value in rightQueue]
        
        else: 

            leftQueue = left.dft()[1:]
            self.value = left.value

            [self.insert(value, 1) for value in leftQueue]
            [self.insert(value, 1) for value in rightQueue]
       
      
            


    def rotateLeft(self):

        right = self.right 
        self.right = None 

        leftQueue = self.dft()
        self.left = None

        minNode = right.get_min()
        print(minNode.value, right.value)

        if minNode != right:
            
            print("here")
            minNodeQueue = right.left.dft()[1:]
            print(minNodeQueue)
           
            right.left = None
            rightQueue = right.dft()
          
            
            self.value = minNode.value
            
            [self.insert(value, 1) for value in minNodeQueue]
            [self.insert(value, 1) for value in leftQueue]
            [self.insert(value, 1) for value in rightQueue]
        
        else: 
            print(right.value)
            rightQueue = right.dft()[1:]
            print("here")
            print(rightQueue)
            self.value = right.value

            [self.insert(value, 1) for value in leftQueue]
            [self.insert(value, 1) for value in rightQueue]
        

    def dft(self):
        
        queue = []
        returnQueue = []
        currentNode = None

        if not self.value:
            pass

        queue.append(self)

        if self.left:
            queue.append(self.left)
        if self.right:
            queue.append(self.right)

        returnQueue.append(queue.pop(0).value)

        currentNode = queue[0]

        while currentNode != None:

            if currentNode.right:
                queue.insert(1, currentNode.right)
            
            if currentNode.left:
                queue.insert(1, currentNode.left)

        
            returnQueue.append(queue.pop(0).value)

            if len(queue) > 0:
                currentNode = queue[0]
            else:
                currentNode = None

        return returnQueue


    def get_max(self):
        
        if self.value == None:
            return None
        elif self.right == None:
            return self
        else:

            currentNode = self.right
            currentMax = self.right

            while currentNode.right != None:

                if currentNode.value < currentNode.right.value:
                    currentMax = currentNode.right
            
                currentNode = currentNode.right

            return currentMax

    def get_min(self):

        if self.value == None:
            return None
        elif self.left == None:
            return self
        else:

            currentNode = self.left
            currentMax = self.left

            while currentNode.left != None:

                if currentNode.value > currentNode.left.value:
                    currentMax = currentNode.left
            
                currentNode = currentNode.left

            return currentMax


    def insert(self, value, root = None):

        if not root:
            root = self

        if not self.value: 
            self.value = value
            self.height = 0 
        elif self.value > value:
            if not self.left:
                self.left = AVLTreeNode(value)
                self.left.height = self.height + 1
            else:
                self.left.insert(value, root)
        else:
            if not self.right:
                self.right = AVLTreeNode(value)
                self.right.height = self.height + 1
            else:
                self.right.insert(value, root)
        
        if root == self:
            root.balance_tree()

    
root = AVLTreeNode(10)
root.insert(9)
root.insert(14)
root.insert(18)
root.insert(12)
root.insert(13)
root.insert(15)
root.insert(16)
root.insert(17)
root.insert(122)
root.insert(3)
root.insert(5)
root.insert(2)
root.insert(20)
root.insert(22)
root.insert(138)
root.insert(4)
root.insert(21)
root.insert(19)
# root.insert(19)

# print(root.balance_tree())

print(root)

