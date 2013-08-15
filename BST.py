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
        
        
    def find(self,node,target):
        if node == None:
            return False  
        if node.value < target:
            return self.find(node.rightChild,target)
        elif node.value > target:
            return self.find(node.leftChild,target)
        else:
            return True
        
    def select(self,node,target):
        if node == None:
            return None
        if node.value < target:
            return self.select(node.rightChild,target)
        elif node.value > target:
            return self.select(node.leftChild,target)
        else:
            return node
        
    def min(self,node):
        if node.leftChild == None:
            return node.value
        return self.min(node.leftChild)
        
    def max(self,node):
        if node.rightChild == None:
            return node.value
        return self.max(node.rightChild)
        
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
    print 'XXX'
    root = tree.root
    tree.insert(root,4)
    tree.insert(root,1)
    tree.insert(root,5)
    tree.insert(root,8)
    tree.insert(root,7.5)
    print 'Nodes in tree in order:'
    tree.printTree(root)
    print 'Find node with value 2: {0}'.format(tree.find(root,2))
    print 'Find node with value 8: {0}'.format(tree.find(root,8))
    print 'Max node in tree: {0}'.format(tree.max(root))
    print 'Min node in tree: {0}'.format(tree.min(root))
    print 'Successor of 5: {0}'.format(tree.next(tree.select(root,5)))
    print 'Successor of 7: {0}'.format(tree.next(tree.select(root,7)))
    print 'Successor of 4: {0}'.format(tree.next(tree.select(root,4)))
    print 'Successor of 8: {0}'.format(tree.next(tree.select(root,8)))
    print 'Predecessor of 1: {0}'.format(tree.prior(tree.select(root,1)))
    print 'Predecessor of 4: {0}'.format(tree.prior(tree.select(root,4)))
    print 'Predecessor of 5: {0}'.format(tree.prior(tree.select(root,5)))
    print 'Predecessor of 7.5: {0}'.format(tree.prior(tree.select(root,7.5)))
    print time.clock() - start