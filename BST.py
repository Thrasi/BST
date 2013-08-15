import heapq as hp
import time

class Node:
    def __init__(self,value):
        self.value = value
        self.leftChild = None
        self.rightChild = None
        self.parent = None
        
    def getChildren(self):
        children = []
        if self.leftChild != None:    
            children.append(self.leftChild)
        if self.rightChild != None:
            children.append(self.rightChild)
        return children
        
        
class unbalancedBST():
    def __init__(self,root=None):
        if root:
            self.root = Node(root)
        else:
            pass
        
    def find(self,target):
        return self.contains(self.root,target)    
        
    def contains(self,node,target):
        if node == None:
            return False  
        if node.value < target:
            return self.contains(node.rightChild,target)
        elif node.value > target:
            return self.contains(node.leftChild,target)
        else:
            return True
            
    def select(self,target):
        return self.getNode(self.root,target)
        
    def getNode(self,node,target):
        if node == None:
            return None
        if node.value < target:
            return self.getNode(node.rightChild,target)
        elif node.value > target:
            return self.getNode(node.leftChild,target)
        else:
            return node
        
    def min(self,node=None):
        if node:
            if node.leftChild == None:
                return node.value
            return self.min(node.leftChild)
        else:
            node = self.root
            if node.leftChild == None:
                return node.value
            return self.min(node.leftChild)
        
    def max(self,node=None):
        if node:
            if node.rightChild == None:
                return node.value
            return self.max(node.rightChild)
        else:
            node = self.root
            if node.leftChild == None:
                return node.value
            return self.min(node.leftChild)
            
    def prior(self,node):
        if node.leftChild:
            return self.max(node.leftChild)
        parent = node.parent
        while parent:
            if parent.value < node.value:
                return parent.value
            parent = parent.parent
            
    def next(self,node):
        if node.rightChild:
            return self.min(node.rightChild)
        parent = node.parent
        while parent:
            if parent.value > node.value:
                return parent.value
            parent = parent.parent
            
    def insert(self,root,value):
        """Excludes duplicate values"""
        if root == None: #Does this ever happen?
            return Node(value)
        if root.value < value:
            if root.rightChild:
                self.insert(root.rightChild,value)
            else:
                root.rightChild = Node(value)
                root.rightChild.parent = root
        elif root.value > value:
            if root.leftChild:
                self.insert(root.leftChild,value)
            else:
                root.leftChild = Node(value)
                root.leftChild.parent = root
        else:
            return None
            
    def delete(self,root,node):
        pass
        
    def printTree(self,node):
        if node == None:
            return
        self.printTree(node.leftChild)
        print node.value
        self.printTree(node.rightChild)
        
if __name__ == "__main__":
    
    tree=unbalancedBST(7)
    start = time.clock()
    root = tree.root
    tree.insert(root,4)
    tree.insert(root,1)
    tree.insert(root,5)
    tree.insert(root,8)
    tree.insert(root,7.5)
    print 'Nodes in tree in order:'
    tree.printTree(root)
    print 'Find node with value 2: {0} (False)'.format(tree.find(2))
    print 'Find node with value 8: {0} (True)'.format(tree.find(8))
    print 'Max node in a subtree 4: {0} (5)'.format(tree.max(tree.select(4)))
    print 'Min node in a subtree 8: {0} (7.5)'.format(tree.min(tree.select(8)))
    print 'Max node in tree: {0} (1)'.format(tree.max())
    print 'Min node in tree: {0} (8)'.format(tree.min())
    print 'Successor of 5: {0} (7)'.format(tree.next(tree.select(5)))
    print 'Successor of 7: {0} (7.5)'.format(tree.next(tree.select(7)))
    print 'Successor of 4: {0} (5)'.format(tree.next(tree.select(4)))
    print 'Successor of 8: {0} (None)'.format(tree.next(tree.select(8)))
    print 'Predecessor of 1: {0} (None)'.format(tree.prior(tree.select(1)))
    print 'Predecessor of 4: {0} (1)'.format(tree.prior(tree.select(4)))
    print 'Predecessor of 5: {0} (4)'.format(tree.prior(tree.select(5)))
    print 'Predecessor of 7.5: {0} (7)'.format(tree.prior(tree.select(7.5)))
    print time.clock() - start
    #min/max argument is optional now
    #find/select no longer need a node argument