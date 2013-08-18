
class BinaryTreeNode:
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
        
        
def nodeSwap(node1,node2):
    """Swaps node1 and node2sdf"""
    node1.value, node2.value = node2.value, node1.value