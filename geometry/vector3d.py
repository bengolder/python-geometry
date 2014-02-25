"""This module is for the Vector class"""
from .vector2d import Vector2d

class Vector3d(Vector2d):
    """A 3d vector object
    """
    def __init__(self, x=0.0, y=0.0, z=0.0):
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
        """
        # dictionary
        if key in ('x','y','z'):
            return self.asDict()[key]
        # slicing and index calls
        else:
            return self.coords.__getitem__(key)

    def cross(self, other):
        """Gets the cross product between two vectors
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



