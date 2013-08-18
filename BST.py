import time
from nodes import BinaryTreeNode as Node
import nodes
        
class BSTunbalanced():
    """An instance of the BSTunbalanced contains a root of a tree"""
    def __init__(self,root=None):
        if root:
            self.root = Node(root)
        else:
            pass
        
    def find(self,target):
        return self.contains(self.root,target)    
        
    def contains(self,node,target):#sdfg
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
            
    def minNode(self,node=None):
        if node:
            if node.leftChild == None:
                return node
            return self.minNode(node.leftChild)
        else:
            node = self.root
            if node.leftChild == None:
                return node
            return self.minNode(node.leftChild)
        
    def max(self,node=None):
        if node:
            if node.rightChild == None:
                return node.value
            return self.max(node.rightChild)
        else:
            node = self.root
            if node.rightChild == None:
                return node.value
            return self.max(node.rightChild)
            
    def maxNode(self,node=None):
        if node:
            if node.rightChild == None:
                return node
            return self.maxNode(node.rightChild)
        else:
            node = self.root
            if node.rightChild == None:
                return node
            return self.maxNode(node.rightChild)
            
    def prior(self,node):
        check = type(node)
        if check==int or check==float:
            node = self.select(node)
        if node.leftChild:
            return self.max(node.leftChild)
        parent = node.parent
        while parent:
            if parent.value < node.value:
                return parent.value
            parent = parent.parent
    
    def priorNode(self,node):
        if node.leftChild:
            return self.maxNode(node.leftChild)
        parent = node.parent
        while parent:
            if parent.value < node.value:
                return parent
            parent = parent.parent
            
    def next(self,node):
        check = type(node)
        if check==int or check==float:
            node = self.select(node)
        if node.rightChild:
            return self.min(node.rightChild)
        parent = node.parent
        while parent:
            if parent.value > node.value:
                return parent.value
            parent = parent.parent
            
    def nextNode(self,node):
        if node.rightChild:
            return self.minNode(node.rightChild)
        parent = node.parent
        while parent:
            if parent.value > node.value:
                return parent
            parent = parent.parent
            
    def insert(self,value,subNode=None):
        if subNode == None:
            subNode = self.root
        if subNode.value < value:
            if subNode.rightChild:
                self.insert(value,subNode.rightChild)
            else:
                subNode.rightChild = Node(value)
                subNode.rightChild.parent = subNode
        elif subNode.value > value:
            if subNode.leftChild:
                self.insert(value,subNode.leftChild)
            else:
                subNode.leftChild = Node(value)
                subNode.leftChild.parent = subNode
        else:
            return None
        
    def delete(self,node):
        """Currently this can't handle the deletion of a root node."""
        check = type(node)
        if check==int or check==float:
            node = self.select(node)
        parent = node.parent
            
        if node.rightChild and node.leftChild:
            predecessor = self.priorNode(node)
            tempValue = predecessor.value
            self.delete(predecessor)
            node.value = tempValue
            
        elif node.rightChild:
            if parent.value > node.value:
                node.parent.leftChild = node.rightChild
            else:
                node.parent.rightChild = node.rightChild
        elif node.leftChild:
            if parent.value > node.value:
                node.parent.leftChild = node.leftChild
            else:
                node.parent.rightChild = node.leftChild
        else:
            if parent.value > node.value:
                node.parent.leftChild = None
            else:
                node.parent.rightChild = None
    # self.replaceNodeWith(node,None)
    # self.replaceNodeWith(node.leftChild)
    # self.replaceNodeWith(node.rightChild)
    def replaceNodeWith(self,node,child):
        if node.parent.value > node.value:
            node.parent.leftChild = child
        else:
            node.parent.rightChild = child
        
    def printTree(self,node=None):
        if node == None:
            return
        self.printTree(node.leftChild)
        print node.value
        self.printTree(node.rightChild)
        
        
if __name__ == "__main__":
    
    tree=BSTunbalanced(7)
    start = time.clock()
    root = tree.root
    tree.insert(4)
    tree.insert(1)
    tree.insert(5)
    tree.insert(8)
    tree.insert(7.5)
    tree.insert(6)
    print 'Nodes in tree in order:'
    tree.printTree(root)
    print 'Find node with value 2: {0} (False)'.format(tree.find(2))
    print 'Find node with value 8: {0} (True)'.format(tree.find(8))
    print 'Max node in a subtree 4: {0} (5)'.format(tree.max(tree.select(4)))
    print 'Min node in a subtree 8: {0} (7.5)'.format(tree.min(tree.select(8)))
    print 'Max node in tree: {0} (8)'.format(tree.max())
    print 'Min node in tree: {0} (1)'.format(tree.min())
    print 'Successor of 5: {0} (7)'.format(tree.next(5))
    print 'Successor of 7: {0} (7.5)'.format(tree.next(7))
    print 'Successor of 4: {0} (5)'.format(tree.next(4))
    print 'Successor of 8: {0} (None)'.format(tree.next(8))
    print 'Predecessor of 1: {0} (None)'.format(tree.prior(1))
    print 'Predecessor of 4: {0} (1)'.format(tree.prior(4))
    print 'Predecessor of 5: {0} (4)'.format(tree.prior(5))
    print 'Predecessor of 7.5: {0} (7)'.format(tree.prior(7.5))
    tree.printTree(root)
    tree.delete(7)
    print 'Tree'
    tree.printTree(root)
    print 'Tree ends'
    print time.clock() - start#dsf
    print tree.root.value
    