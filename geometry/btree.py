from .core import string_type

class BTreeNode(object):
    # I should have two types of nodes: simple values
    # and nodes with key retrievals
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
        else:
            self._key = lambda d: value

    def __call__(self):
        return self.key, self.data

    def __repr__(self):
        return "BTreeNode(%s)" % self.key


class BinarySearchTree(object):
    def __init__(self, data=None, key=None):
        self.key = key
        self.root = None
        if data != None:
            self.extend(data)

    def extend(self, items, key=None):
        if key != None:
            self.key = key
        if self.key != None:
            for item in items:
                self.append( self.key, item )
        else:
            for item in items:
                self.append( item )

    def _walk(self, node):
        if node != None:
            self._walk(node.left)
            self._nodelist.append(node())
            self._walk(node.right)

    def walk(self):
        if self.root == None:
            return []
        self._nodelist = []
        self._walk(self.root)
        nodes = self._nodelist
        delattr(self, '_nodelist')
        return nodes

    def append(self, key, data=None):
        node = BTreeNode( key, data )
        parent = None
        cursor = self.root
        while cursor != None:
            parent = cursor
            if node.key < cursor.key:
                cursor = cursor.left
            else:
                cursor = cursor.right
        node.parent = parent
        if parent == None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

    def delete(self, key):
        pass

    def min(self):
        node = self.root
        while node.left != None:
            node = node.left
        return node()

    def max(self):
        node = self.root
        while node.right != None:
            node = node.right
        return node()

    def find(self, key):
        pass

class BalancedBinarySearchTree(object):
    pass
