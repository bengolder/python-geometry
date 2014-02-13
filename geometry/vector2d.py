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
        self.coords = self.coords[:1] + value + self.coords[2:]

    def asDict(self):
        """return dictionary representation of the vector"""
        return dict( zip( list('xy'), self.coords ) )

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

class Point2d(Vector2d):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

    def __repr__(self):
        return 'Point2d(%s, %s, %s)' % self.coords

    def distanceTo(self, other):
        """Find the distance between this point and another.
            >>> p1 = Point3d(-2.2, -0.5, 0.0034)
            >>> p2 = Point3d(3.45, 0.01, -2004.665)
            >>> p1.distanceTo(p2)
            2004.676426897508
        """
        return (other - self).length

PageX = Vector2d(1.0, 0.0)
PageY = Vector2d(0.0, 1.0)

