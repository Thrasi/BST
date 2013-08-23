import time
from nodes import BinaryTreeNode as Node
import nodes
import Queue
        
class BST():
    """An instance of the BST contains a root of a tree"""
    def __init__(self,root=None):
        if root:
            self.root = Node(root)
        else:
            self.root = None
        
    def find(self,target):
        return self.__contains(self.root,target)    
        
    def __contains(self,node,target):
        if node == None:
            return False  
        if node.value < target:
            return self.__contains(node.rightChild,target)
        elif node.value > target:
            return self.__contains(node.leftChild,target)
        else:
            return True
            
    def select(self,target):
        return self.__getNode(self.root,target)
        
    def __getNode(self,node,target):
        if node == None:
            return None
        if node.value < target:
            return self.__getNode(node.rightChild,target)
        elif node.value > target:
            return self.__getNode(node.leftChild,target)
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
        """node can either be a number or Node instance. If it is a number
        it runs in O(log(height)) time.
        Returns a number.
        """
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
        """node must be a Node instance.
        Returns a Node instance."""
        if node.leftChild:
            return self.maxNode(node.leftChild)
        parent = node.parent
        while parent:
            if parent.value < node.value:
                return parent
            parent = parent.parent
            
    def next(self,node):
        """node can either be a number or Node instance. If it is a number
        it runs in O(log(height)) time. Returns a number.
        """
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
        """node must be a Node instance.
        Returns a Node instance.
        """
        if node.rightChild:
            return self.minNode(node.rightChild)
        parent = node.parent
        while parent:
            if parent.value > node.value:
                return parent
            parent = parent.parent
            
    def insert(self,value,subNode=None):
        """This needs work in order to handle double entries
        """
        if subNode == None:
            subNode = self.root
        try:
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
        except AttributeError:
            print "CREATED ROOT!"
            self.root = Node(value)
        
    def delete(self,node):
        """If node is a number we find the node instance corresponding to the
        number.  This runs in O(log(height)) time.  If node is already a node instance
        this runs in O(1) time
        """
        check = type(node)
        if check==int or check==float:
            node = self.select(node)
            
        if node.rightChild and node.leftChild:
            predecessor = self.priorNode(node)
            tempValue = predecessor.value
            self.delete(predecessor)
            node.value = tempValue
        elif node.rightChild:
            self.__replaceNodeWith(node,node.rightChild)
        elif node.leftChild:
            self.__replaceNodeWith(node,node.leftChild)
        else:
            self.__replaceNodeWith(node,None)
            
    def __replaceNodeWith(self,node,child):
        if node.parent.value > node.value:
            node.parent.leftChild = child
        else:
            node.parent.rightChild = child
        if child:
            child.parent = node.parent
        
    def height(self,node=None,height = 1):
        if node==None:
            node=self.root
        if node.leftChild:
            leftHeight = self.height(node.leftChild,height+1)
        else:
            leftHeight = height
        if node.rightChild:
            rightHeight = self.height(node.rightChild,height+1)
        else:
            rightHeight = height
        if leftHeight > rightHeight:
            return leftHeight
        else:
            return rightHeight
            
    def rotateRight(self,node):
        check = type(node)
        if check==int or check==float:
            node = self.select(node)
        if node.leftChild==None:
            print "Argument has no left child!"
            return
        if node == self.root:
            self.root = node.leftChild
        else:
            self.__replaceNodeWith(node,node.leftChild)
        #The actiual rotation:
        pivot = node.leftChild
        node.leftChild = pivot.rightChild
        pivot.rightChild = node
        node = pivot
        #Fix the parental relations:
        node.parent = node.rightChild.parent
        node.rightChild.parent = node
        if node.rightChild.leftChild:
            node.rightChild.leftChild.parent = node.rightChild
        
    def rotateLeft(self,node):
        check = type(node)
        if check==int or check==float:
            node = self.select(node)
        if node.rightChild==None:
            print "Argument has no right child!"
            return
        if node == self.root:
            self.root = node.rightChild
        else:
            self.__replaceNodeWith(node,node.rightChild)
        
        #The actiual rotation:
        pivot = node.rightChild
        node.rightChild = pivot.leftChild
        pivot.leftChild = node
        node = pivot
        #Fix the parental relations:
        node.parent = node.leftChild.parent
        node.leftChild.parent = node
        if node.leftChild.rightChild:
            node.leftChild.rightChild.parent = node.leftChild
        
    def relations(self):
        return self.__relations(self.root)
        
    def __relations(self,node=None):
        """Returns a list of where each element lists a node and its 
        direct relatives: [node value, left child, right child, parent]
        """
        if node == None:
            return []
        relationList = []
        leftResults = self.__relations(node.leftChild)
        
        if leftResults:
            for element in leftResults:
                relationList.append(element)
        value = node.value
        lc = -1
        rc = -1
        parent = -1
        if node.leftChild:
            lc = node.leftChild.value
        if node.rightChild:
            rc = node.rightChild.value
        if node.parent:
            parent = node.parent.value
        relationList.append([value,lc,rc,parent])
        
        rightResults = self.__relations(node.rightChild)
        if rightResults:
            for element in rightResults:
                relationList.append(element)
        return relationList
    
    
    def printTree(self,node=None):
        if node:
            self.__printTree(node)
        else:
            self.__printTree(self.root)
        
    def __printTree(self,node=None):
        if node == None:
            return
        self.__printTree(node.leftChild)
        print node.value
        self.__printTree(node.rightChild)
            
    def levelPrint(self):
        currentLvl = Queue.Queue()
        currentLvl.put(self.root)
        nextLvl = Queue.Queue()
        level = ""
        while not currentLvl.empty():
            node=currentLvl.get()
            level += str(node.value) + " "
            for child in node.getChildren():
                if child:
                    nextLvl.put(child)
            if currentLvl.empty():
                print level
                level = ""
                while not nextLvl.empty():
                    currentLvl.put(nextLvl.get())
        
class AVLTree(BST):
    pass
        
if __name__ == "__main__":
    
    tree = BST(7)
    root = tree.root
    tree.insert(4)
    tree.insert(1)
    tree.insert(5)
    tree.insert(8)
    tree.insert(7.5)
    tree.insert(6)
    print 'Nodes in tree in order:'
    tree.printTree(root)
    print 'Tree ends'
    tree.levelPrint()
    #tree2 = BST(4)
    #tree2.insert(7)
    #tree2.insert(1)
    #tree2.insert(8)
    #tree2.insert(5)
    #tree2.insert(6)
    #tree2.insert(7.5)
    #tree2.levelPrint()
    tree3=BST()
    tree3.insert(4)
    
    
    
    