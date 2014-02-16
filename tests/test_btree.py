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
    def setUp(self):
        from .test_vector import CoordGenerator
        gen3 = CoordGenerator(dim=3, number_type=int)
        gen1 = CoordGenerator(dim=1, number_type=int)
        self.coords = [tuple(gen3()) for i in range(20)]
        self.numbers = [gen1()[0] for i in range(20)]

    def test_tree_build_simple(self):
        # build from numbers
        from geometry import BinarySearchTree
        treeB = BinarySearchTree(self.numbers)
        sorted_keys = [n[0] for n in treeB.walk()]
        sorted_numbers = sorted(self.numbers)
        self.assertItemsEqual(sorted_keys, sorted_numbers)
        self.assertEqual( treeB.min()[0], sorted_numbers[0] )
        self.assertEqual( treeB.max()[0], sorted_numbers[-1] )

    def test_tree_build_with_key_function(self):
        # build from key
        from geometry import BinarySearchTree
        key = lambda p: p[0]
        tree = BinarySearchTree(self.coords, key)
        sorted_items = [n[1] for n in tree.walk()]
        sorted_points = sorted(self.coords, key=key)
        self.assertItemsEqual(sorted_items, sorted_points)
        self.assertEqual( tree.min()[1], sorted_points[0] )
        self.assertEqual( tree.max()[1], sorted_points[-1] )

    def test_tree_find(self):
        from geometry import BinarySearchTree
        tree = BinarySearchTree(self.numbers)



class TestBalancedBinarySearchTree(unittest.TestCase):
    def setUp(self):
        from geometry import BalancedBinarySearchTree
        tree = BalancedBinarySearchTree()


