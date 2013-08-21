import unittest
import BST

class TestMain(unittest.TestCase):
    def makeTree(self):
        self.tree=BST.BSTunbalanced(7)
        root = self.tree.root
        self.tree.insert(4)
        self.tree.insert(1)
        self.tree.insert(5)
        self.tree.insert(8)
        self.tree.insert(7.5)
        
    def testFind(self):
        self.makeTree()
        expected = False
        result = self.tree.find(2)
        self.assertEqual(expected, result)
        
        expected = True
        result = self.tree.find(8)
        self.assertEqual(expected, result)
        
    def testMaxMin(self):
        self.makeTree()
        expected = 8
        result = self.tree.max()
        self.assertEqual(expected, result)
        
        expected = 1
        result = self.tree.min()
        self.assertEqual(expected, result)
        
        expected = 5
        result = self.tree.max(self.tree.select(4))
        self.assertEqual(expected, result)
        
        expected = 7.5
        result = self.tree.min(self.tree.select(8))
        self.assertEqual(expected, result)
        
    def testNext(self):
        self.makeTree()
        expected = 7
        result = self.tree.next(5)
        self.assertEqual(expected, result)
        
        expected = 7.5
        result = self.tree.next(7)
        self.assertEqual(expected, result)
        
        expected = 5
        result = self.tree.next(4)
        self.assertEqual(expected, result)
        
        expected = None
        result = self.tree.next(8)
        self.assertEqual(expected, result)
        
    def testPrior(self):
        self.makeTree()
        expected = None
        result = self.tree.prior(1)
        self.assertEqual(expected, result)
        
        expected = 1
        result = self.tree.prior(4)
        self.assertEqual(expected, result)
        
        expected = 4
        result = self.tree.prior(5)
        self.assertEqual(expected, result)
        
        expected = 7
        result = self.tree.prior(7.5)
        self.assertEqual(expected, result)
        
    def testRotation(self):
        self.makeTree()
        self.tree.insert(6)
        expected = [[1, -1, -1, 4],[4, 1, -1, 5],[5, 4, 6, 7],[6, -1, -1, 5],
                    [7, 5, 8, -1],[7.5, -1, -1, 8],[8, 7.5, -1, 7]]
        self.tree.rotateLeft(4)
        result = self.tree.relations(self.tree.root)
        self.assertEqual(expected, result)
        
        expected = [[1, -1, -1, 4],[4, 1, 7, -1],[5, -1, 6, 7],[6, -1, -1, 5],
                    [7, 5, 8, 4],[7.5, -1, -1, 8],[8, 7.5, -1, 7]]
        self.tree.rotateRight(7)
        result = self.tree.relations(self.tree.root)
        self.assertEqual(expected, result)
        
if __name__ == '__main__':
    unittest.main()