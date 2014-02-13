"""This module is for the Vector class"""
from .vector2d import Vector2d

class Vector3d(Vector2d):
    """A 3d vector object
    """
    def __init__(self, x=0.0, y=0.0, z=0.0):
        # coords is the essence of the data structure. It's immutable and
        # iterable, allowing us to iterate over the values as well as providing
        # a little bit of protection from accidentally changing the values see
        # `classTest` in tests to understand more of the reasoning here.
        Vector2d.__init__(self)
        self.coords = (x, y, z)

    @property
    def z(self):
        return self[2]
    @z.setter
    def z(self, value):
        self.coords = (self.x, self.y, value)

    def toX(self, number):
        """For getting a copy of the same vector but with a new x value"""
        return self.__class__(number, self[1], self[2])

    def toY(self, number):
        """For getting a copy of the same vector but with a new y value"""
        return self.__class__(self[0], number, self[2])

    def toZ(self, number):
        """For getting a copy of the same vector but with a new z value"""
        return self.__class__(self[0], self[1], number)

    def asDict(self):
        """return dictionary representation of the vector"""
        return dict( zip( list('xyz'), self.coords ) )

    def __getitem__(self, key):
        """Treats the vector as a tuple or dict for indexes and slicing.
            >>> v
            Vector3d(2.0, 1.0, 2.2)
            >>> v[0]
            2.0
            >>> v[-1]
            2.2000000000000002
            >>> v[:2]
            (2.0, 1.0)
            >>> v['y']
            1.0
        """
        # dictionary
        if key in ('x','y','z'):
            return self.asDict()[key]
        # slicing and index calls
        else:
            return self.coords.__getitem__(key)

    def cross(self, other):
        """Gets the cross product between two vectors
            >>> v
            Vector3d(5, 1.20747670785, 60.0)
            >>> v1
            Vector3d(0.0, 2.0, 1.0)
            >>> v1.cross(v)
            Vector3d(118.792523292, 5.0, -10.0)
        """
        x = (self[1] * other[2]) - (self[2] * other[1])
        y = (self[2] * other[0]) - (self[0] * other[2])
        z = (self[0] * other[1]) - (self[1] * other[0])
        return self.__class__(x, y, z)

    def __repr__(self):
        return 'Vector3d(%s, %s, %s)' % self.coords


WorldX = Vector3d(1.0, 0.0, 0.0)
WorldY = Vector3d(0.0, 1.0, 0.0)
WorldZ = Vector3d(0.0, 0.0, 1.0)



