
class BinaryTreeNode:
    def __init__(self,value):
        self.value = value
        self.leftChild = None
        self.rightChild = None
        self.parent = None
        
    def getChildren(self):
        children = [None,None]
        if self.leftChild != None:    
            children[0] = self.leftChild
        if self.rightChild != None:
            children[1] = self.rightChild
        return children
        
       
    def getSibling(self):
        if self.parent.leftChild.value == self.value:
            return self.parent.leftChild
        else:
            return self.parent.rightChild
            
class RedBlackNode(BinaryTreeNode):
    def __init__(self,value,colour):
        BinaryTreeNode.__init__(self,value)
        self.colour = colour

class AVLNode(BinaryTreeNode):
    def __init__(self,value):
        BinaryTreeNode.__init__(self,value)
        self.height = None
        
    #def 
            
        
        
def nodeSwap(node1,node2):
    """Swaps node1 and node2sdf"""
    node1.value, node2.value = node2.value, node1.value
    
if __name__ == "__main__":
    node = RedBlackNode(5,'r')
    print node.value,node.colour
    