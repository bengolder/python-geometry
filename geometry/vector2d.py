from .vector import VectorBase

class Vector2d(VectorBase):
    def __init__(self, x=0.0, y=0.0):
        VectorBase.__init__(self)
        self.coords = (x, y)

    @property
    def x(self):
        return self[0]
    @x.setter
    def x(self, value):
        self.coords = (value,) + self.coords[1:]

    @property
    def y(self):
        return self[1]
    @y.setter
    def y(self, value):
        self.coords = self.coords[:1] + (value,) + self.coords[2:]

    def asDict(self):
        """return dictionary representation of the vector"""
        return dict( zip( ('x','y'), self.coords ) )

    def __getitem__(self, key):
        """Treats the vector as a tuple or dict for indexes and slicing.
        """
        # dictionary
        if key in ('x','y'):
            return self.asDict()[key]
        # slicing and index calls
        else:
            return self.coords.__getitem__(key)

    def toX(self, number):
        """For getting a copy of the same vector but with a new x value"""
        return self.__class__(number, self[1])

    def toY(self, number):
        """For getting a copy of the same vector but with a new y value"""
        return self.__class__(self[0], number)

    def __repr__(self):
        return 'Vector2d(%s, %s)' % self.coords

PageX = Vector2d(1.0, 0.0)
PageY = Vector2d(0.0, 1.0)
