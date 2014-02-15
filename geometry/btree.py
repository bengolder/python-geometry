
class BTreeNode(object):
    def __init__(self, key, data=None, parent=None, left=None,
            right=None):
        """Should not be instantiated directly. Should be created by a search
        tree.
        Make a new node from a value, or data that has a key attribute
        """
        self.parent = parent
        self.left = left
        self.right = right
        self.data = data
        self.key = key

    @property
    def key(self):
        return self._key( self.data )

    @key.setter
    def key(self, value):
        if hasattr(value, '__call__'):
            self._key = value
        elif isinstance(value, basestring):
            self._key = lambda d: d[value]
        else:
            self._key = lambda d: value

    def __repr__(self):
        return "BTreeNode(%s)" % self.key


class BinarySearchTree(object):
    def walk(self, node):
        if node != None:
            self.walk(node.left)
            print( node.key )
            self.walk(node.right)

    def insert(self, key, data=None):
        pass

    def delete(self, key):
        pass

    def min(self):
        pass

    def max(self):
        pass

    def find(self, key):
        pass

class BalancedBinarySearchTree(object):
    pass
