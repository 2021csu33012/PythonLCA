import unittest
from unittest import result

import LowestCA
from LowestCA import findLCA, findLCAUtil, __init__, Node

class FirstTest(unittest.TestCase):

    def test(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        result = 2
        self.assertEqual(findLCA(root, 4, 5).key, result)

class nullr(unittest.TestCase):

    def nullTest(self):
        root = Node(1)
        root.left = None
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        result = None
        self.assertEqual(findLCA(root, 4, 5), result)

if __name__ == '__main__':
    unittest.main()
