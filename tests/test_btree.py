import unittest

class TestBTreeNode(unittest.TestCase):

    def test_constructor(self):
        from geometry import BTreeNode
        n = BTreeNode(5)
        key_func = lambda d: d['x']
        m = BTreeNode(key_func,
            {'x':6},
            parent=n
            )
        self.assertEqual(m.key, 6)
        p = BTreeNode('x',
            {'x':9},
            left=n,
            right=m,
            )
        self.assertEqual(p.key, 9)
        self.assertEqual("BTreeNode(5)", str(p.left))

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        from geometry import Point3d
        from .test_vector import CoordGenerator
        self.gen = CoordGenerator()
        self.points = [self.gen.point() for i in range(20)]

    def test_tree_build(self):
        from geometry import BinarySearchTree
        tree = BinarySearchTree()

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        from geometry import BalancedBinarySearchTree
        tree = BalancedBinarySearchTree()


