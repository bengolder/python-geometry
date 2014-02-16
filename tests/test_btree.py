import unittest
import random


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
        p = BTreeNode(2,
            {'x':9},
            left=n,
            right=m,
            )
        self.assertEqual(p.key, 2)
        self.assertEqual("BTreeNode(5)", str(p.left))


class TestBinarySearchTree(unittest.TestCase):

    def assertIterEqual(self, a, b):
        for na, nb in zip(a, b):
            self.assertEqual(na, nb)

    def setUp(self):
        from .test_vector import CoordGenerator
        gen3 = CoordGenerator(dim=3, number_type=int)
        gen1 = CoordGenerator(dim=1, number_type=int)
        self.coords = [tuple(gen3()) for i in range(20)]
        self.numbers = [gen1()[0] for i in range(20)]

    def test_tree_build_simple(self):
        # build from numbers
        from geometry import BinarySearchTree
        tree = BinarySearchTree(self.numbers)
        nodes = [n[0] for n in tree.walk()]
        values = sorted(self.numbers)
        self.assertEqual( len(nodes), len(values) )
        self.assertIterEqual( nodes, values )
        self.assertEqual( tree.min()[0], values[0] )
        self.assertEqual( tree.max()[0], values[-1] )

    def test_tree_build_with_key_function(self):
        # build from key
        from geometry import BinarySearchTree
        key = lambda p: p[0]
        tree = BinarySearchTree(self.coords, key)
        nodes = [n[1] for n in tree.walk()]
        values = sorted(self.coords, key=key)
        self.assertEqual( len(nodes), len(values) )
        self.assertIterEqual( nodes, values )
        self.assertEqual( tree.min()[1], values[0] )
        self.assertEqual( tree.max()[1], values[-1] )

    def test_tree_find(self):
        from geometry import BinarySearchTree
        tree = BinarySearchTree(self.numbers)



class TestBalancedBinarySearchTree(unittest.TestCase):
    def setUp(self):
        from geometry import BalancedBinarySearchTree
        tree = BalancedBinarySearchTree()


