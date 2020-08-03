"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.value}"

    # Insert the given value into the tree
    def insert(self, value):
        
        if self.value > value:
            if self.left != None:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else: 
            if self.right != None:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
                
                

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        
        if self.value == target:
            return True
        elif self.value > target:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)
        else:
             if self.right == None:
                return False
             else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        
        if self.value == None:
            return None
        elif self.right == None:
            return self.value
        else:

            currentNode = self.right
            currentMax = self.right.value

            while currentNode.right != None:

                if currentNode.value < currentNode.right.value:
                    currentMax = currentNode.right.value
            
                currentNode = currentNode.right

            return currentMax 

            

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        
        if self.value == None:
            pass
        else:
            fn(self.value)

            if self.left != None:
                self.left.for_each(fn)
            
            if self.right != None:
                self.right.for_each(fn)
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        
        
        if self.left:
            self.left.in_order_print()
        
        print(self.value)
        
        if self.right:
            self.right.in_order_print()
                
            

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):

        queue = []
        currentNode = None

        if not self.value:
            pass

        queue.append(self)

        if self.left:
            queue.append(self.left)
        if self.right:
            queue.append(self.right)

        print(queue.pop(0))

        while len(queue) > 0:

            currentNode = queue[0]

            if currentNode.left:
                queue.append(currentNode.left)
            
            if currentNode.right:
                queue.append(currentNode.right)           

            print(queue.pop(0))
            


        


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        
        queue = []
        currentNode = None

        if not self.value:
            pass

        queue.append(self)

        if self.left:
            queue.append(self.left)
        if self.right:
            queue.append(self.right)

        print(queue.pop(0))

        currentNode = queue[0]

        while currentNode != None:

            if currentNode.right:
                queue.insert(1, currentNode.right)
            
            if currentNode.left:
                queue.insert(1, currentNode.left)

        
            print(queue.pop(0))

            if len(queue) > 0:
                currentNode = queue[0]
            else:
                currentNode = None



    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        self.dft_print()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)


def print_node(value):
    print(value)

bst.dft_print()
# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
