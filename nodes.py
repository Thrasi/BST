
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