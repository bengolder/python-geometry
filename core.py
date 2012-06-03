"""
An attempt to make a pure python, pythonic, and very abstracted geometry
library that spans from vectors to NURBS, and includes lots of useful
algorithms. I intend to value abstraction and portability over
performance where necessary. Towards that end I don't plan to use numpy or
other awesome and amazing modules that performance-oriented developers might
use.

Here's some examples:

    >>> from core import Vector3D, Point3D
    >>> # test add
    ... v = Vector3D(0.0, 1.0, 2.0)
    >>> v1 = v + 1
    >>> v1
    Vector3D(0.0, 1.4472135955, 2.894427191)
    >>> v1.length - v.length
    0.99999999999999956
    >>>
    >>> v1 = Vector3D(0.0, 2.0, 1.0)
    >>> v1.length
    2.2360679774997898
    >>> v2 = v1 + 4
    >>> v2.length
    6.2360679774997889
    >>> v3 = v1 + -7
    >>> v1 + v3
    Vector3D(0.0, -2.260990337, -1.1304951685)
    >>> v1 - v2
    Vector3D(0.0, -3.577708764, -1.788854382)
    >>> v1 * v3
    -10.652475842498529
    >>> v3[0]
    0.0
    >>> v1['x']
    0.0
    >>> v1[:2]
    (0.0, 2.0)
    >>> v3[-1]
    -2.1304951684997055
    >>> v2
    Vector3D(0.0, 5.577708764, 2.788854382)
    >>> v3
    Vector3D(0.0, -4.260990337, -2.1304951685)
    >>> v4 = v3.cross(v2)
    >>> # v3 and v2 point in the same direction
    ... v4
    Vector3D(0.0, -0.0, 0.0)
    >>> # this is a vector of length 0
    ... # so it's length can't be adjusted
    ... v4.length = 1.0
    Traceback (most recent call last):
      File "<stdin>", line 3, in <module>
      File "core.py", line 119, in length
        v = self.normalized() * number
      File "core.py", line 147, in normalized
        raise ZeroDivisionError
    ZeroDivisionError
    >>> p1 = Point3D(*v3)
    >>> p2 = Point3D(3.45, 0.01, -2004.665)
    >>> p1.distanceTo(p2)
    2002.5420312440888
    >>> p2.vectorTo(p1)
    Vector3D(-3.45, -4.270990337, 2002.53450483)
    >>> p1 - p2
    Vector3D(-3.45, -4.270990337, 2002.53450483)

First development target: intersections!!

References

[Geometry]
    http://plib.sourceforge.net/sg/index.html

[API]
    Check out the python data model emulation stuff here:
    http://docs.python.org/reference/datamodel.html

classes:

    float
    Vec2
    Vec3
    Vec4
    Mat4
    Coord
    Line3
    LineSegment3
    Quat
    Sphere
    Box
    Frustum
"""

import math
import numbers

# For float comparison:
def isRoughlyZero(number):
    return round(number, 7) == 0
# though there are better ways to do this.
# It would be nice if this could handle all sorts of numbers
# see:
# http://floating-point-gui.de/errors/comparison/
# http://stackoverflow.com/questions/9528421/value-for-epsilon-in-python
# http://stackoverflow.com/questions/4028889/floating-point-equality-in-python
# http://stackoverflow.com/questions/3049101/floating-point-equality-in-python-and-in-general




class Vector3D(object):
    """A 3D vector object"""

    def __init__(self, x=0.0, y=0.0, z=0.0):
        for arg in (x, y, z):
            if not isinstance(arg, numbers.Number):
                raise TypeError
        # coords is the essence of the data structure. It's immutable and
        # iterable, allowing us to iterate over the values as well as providing
        # a little bit of protection from accidentally changing the values see
        # `classTest` in tests to understand more of the reasoning here.
        self.coords = (x, y, z)
    # defining x, y, and z like this to allow for the coords to remain a
    # non-mutable iterable.
    @property
    def x(self):
        return self[0]
    @x.setter
    def x(self, number):
        self.coords = (number, self[1], self[2])
    @property
    def y(self):
        return self[1]
    @y.setter
    def y(self, number):
        self.coords = (self[0], number, self[2])
    @property
    def z(self):
        return self[2]
    @z.setter
    def z(self, number):
        self.coords = (self[0], self[1], number)

    @property
    def length(self):
        """get the vector length / amplitude
            >>> v = Vector3D(0.0, 2.0, 1.0)
            >>> v.length
            2.2360679774997898
        """
        # iterate through the coordinates, square each, and return the root of
        # the sum
        return math.sqrt(sum(n**2 for n in self))

    @length.setter
    def length(self, number):
        """set the vector amplitude
            >>> v = Vector3D(0.0, 2.0, 1.0)
            >>> v.length
            2.2360679774997898
            >>> v.length = -3.689
            >>> v
            Vector3D(-0.0, -3.2995419076, -1.6497709538)
        """
        # depends on normalized() and __mult__
        # create a vector as long as the number
        v = self.normalized() * number
        # copy it
        self.match(v)


    def normalize(self):
        """edits vector in place to amplitude 1.0 and then returns self
            >>> v
            Vector3D(-0.0, -3.2995419076, -1.6497709538)
            >>> v.normalize()
            Vector3D(-0.0, -0.894427191, -0.4472135955)
            >>> v
            Vector3D(-0.0, -0.894427191, -0.4472135955)
        """
        # depends on normalized and match
        self.match(self.normalized())
        return self

    def normalized(self):
        """just returns the normalized version of self without editing self in
        place.
            >>> v.normalized()
            Vector3D(0.0, 0.894427191, 0.4472135955)
            >>> v
            Vector3D(0.0, 3.2995419076, 1.6497709538)
        """
        # think how important float accuracy is here!
        if isRoughlyZero(sum(n**2 for n in self)):
            raise ZeroDivisionError
        else:
            return self * (1 / self.length)

    def match(self, other):
        """sets the vector to something, either another vector,
        a dictionary, or an iterable.
        If an iterable, it ignores everything
        beyond the first 3 items.
        If a dictionary, it only uses keys 'x','y', and 'z'
            >>> v
            Vector3D(0.0, 3.2995419076, 1.6497709538)
            >>> v.match({'x':2.0, 'y':1.0, 'z':2.2})
            >>> v
            Vector3D(2.0, 1.0, 2.2)
        """
        # this basically just makes a new vector and uses it's coordinates to
        # reset the coordinates of this one.
        if isinstance(other, Vector3D):
            self.coords = other.coords
        elif isinstance(other, dict):
            self.coords = (other['x'], other['y'], other['z'])
        else: # assume it is some other iterable
            self.coords = tuple(other[:3])

    def asList(self):
        """return vector as a list"""
        return [c for c in self]

    def asDict(self):
        """return dictionary representation of the vector"""
        return dict( zip( list('xyz'), self.coords ) )

    def __getitem__(self, key):
        """Treats the vector as a tuple or dict for indexes and slicing.
            >>> v
            Vector3D(2.0, 1.0, 2.2)
            >>> v[0]
            2.0
            >>> v[-1]
            2.2000000000000002
            >>> v[:2]
            (2.0, 1.0)
            >>> v['y']
            1.0
        """
        # key index
        if isinstance(key, int):
            return self.coords[key]
        # dictionary
        elif key in ('x','y','z'):
            return self.asDict()[key]
        # slicing
        elif isinstance(key, type(slice(1))):
            return self.coords.__getitem__(key)
        else:
            raise KeyError

    def __setitem__(self, key, value):
        """Treats the vector as a list or dictionary for setting values.
            >>> v
            Vector3D(0.0, 1.20747670785, 2.4149534157)
            >>> v[0] = 5
            >>> v
            Vector3D(5, 1.20747670785, 2.4149534157)
            >>> v['z'] = 60.0
            >>> v
            Vector3D(5, 1.20747670785, 60.0)
        """
        if not isinstance(value, numbers.Number):
            raise ValueError
        if key in ('x','y','z'):
            d = self.asDict()
            d.__setitem__(key, value)
            self.match(d)
        elif key in (0,1,2):
            l = self.asList()
            l.__setitem__(key, value)
            self.match(l)
        else:
            raise KeyError

    def __iter__(self):
        """For iterating, the vectors coordinates are represented as a tuple."""
        return self.coords.__iter__()

    ## Time for some math

    def dot(self, other):
        """Gets the dot product of this vector and another.
            >>> v
            Vector3D(5, 1.20747670785, 60.0)
            >>> v1
            Vector3D(0.0, 2.0, 1.0)
            >>> v1.dot(v)
            62.41495341569977
        """
        return sum((p[0] * p[1]) for p in zip(self, other))

    def cross(self, other):
        """Gets the cross product between two vectors
            >>> v
            Vector3D(5, 1.20747670785, 60.0)
            >>> v1
            Vector3D(0.0, 2.0, 1.0)
            >>> v1.cross(v)
            Vector3D(118.792523292, 5.0, -10.0)
        """
        # I hope I did this right
        x = (self[1] * other[2]) - (self[2] * other[1])
        y = (self[2] * other[0]) - (self[0] * other[2])
        z = (self[0] * other[1]) - (self[1] * other[0])
        return Vector3D(x, y, z)

    def __add__(self, other):
        """we want to add single numbers as a way of changing the length of the
        vector, while it would be nice to be able to do vector addition with
        other vectors.
            >>> from core import Vector3D
            >>> # test add
            ... v = Vector3D(0.0, 1.0, 2.0)
            >>> v1 = v + 1
            >>> v1
            Vector3D(0.0, 1.4472135955, 2.894427191)
            >>> v1.length - v.length
            0.99999999999999956
            >>> v1 + v
            Vector3D(0.0, 2.4472135955, 4.894427191)
        """
        if isinstance(other, numbers.Number):
            # then add to the length of the vector
            # multiply the number by the normalized self, and then
            # add the multiplied vector to self
            return self.normalized() * other + self

        elif isinstance(other, Vector3D):
            # add all the coordinates together
            # there are probably more efficient ways to do this
            return Vector3D(*(sum(p) for p in zip(self, other)))
        else:
            raise NotImplementedError

    def __sub__(self, other):
        """Subtract a vector or number
            >>> v2 = Vector3D(-4.0, 1.2, 3.5)
            >>> v1 = Vector3D(2.0, 1.1, 0.0)
            >>> v2 - v1
            Vector3D(-6.0, 0.1, 3.5)
        """
        return self.__add__(other * -1)

    def __mul__(self, other):
        """if with a number, then scalar multiplication of the vector,
            if with a Vector, then dot product, I guess for now, because
            the asterisk looks more like a dot than an X.
            >>> v2 = Vector3D(-4.0, 1.2, 3.5)
            >>> v1 = Vector3D(2.0, 1.1, 0.0)
            >>> v2 * 1.25
            Vector3D(-5.0, 1.5, 4.375)
            >>> v2 * v1 #dot product
            -6.6799999999999997
        """
        if isinstance(other, numbers.Number):
            # scalar multiplication for numbers
            return Vector3D( *((n * other) for n in self))

        elif isinstance(other, Vector3D):
            # dot product for other vectors
            return self.dot(other)

    def __repr__(self):
        return 'Vector3D%s' % self.coords

class Point3D(Vector3D):
    """Works like a Vector3D. I might add some point specific methods.
    """
    def __init__(self, *args, **kwargs):
        super(Point3D, self).__init__(*args, **kwargs)

    def __repr__(self):
        return 'Point3D%s' % self.coords

    def distanceTo(self, other):
        """Find the distance between this point and another.
            >>> p1 = Point3D(-2.2, -0.5, 0.0034)
            >>> p2 = Point3D(3.45, 0.01, -2004.665)
            >>> p1.distanceTo(p2)
            2004.676426897508
        """
        return (other - self).length

    def vectorTo(self, other):
        """Find the vector to another point.
            >>> p1 = Point3D(-2.2, -0.5, 0.0034)
            >>> p2 = Point3D(3.45, 0.01, -2004.665)
            >>> p1.distanceTo(p2)
            2004.676426897508
            >>> p1.distanceTo(p2)
            2004.676426897508
            >>> p2.vectorTo(p1)
            Vector3D(-5.65, -0.51, 2004.6684)
            >>> p1 - p2
            Vector3D(-5.65, -0.51, 2004.6684)
        """
        return other - self

class PointSet(object):
    """This class is meant to hold a set of *unique* points.
    It enforces this using python's built in `set` type. But points may still
    be within some tolerance of each other.

    In general, this class should be preferred to PointList because many
    geometric algorithms will not assume duplicate points and could produce
    invalid results (such as 0 length edges, collapsed faces, etc) if run on
    points wiht duplicates.

    Basically this provides hooks to using a python 'set' containing tuples of
    the point coordinates.

    This should actually be an ordered set, not just a set. I'm not sure how
    much it matters though if the points can be looked up by their coordinates
    so easily.

    Perhaps the core set can be defined by a list and a dictionary. __iter__
    would call on the list, while one would be able to look up the hashed
    coordinate tuples as dictionary keys to get their index.

    I like this list/dictionary combo, because even though what I would truly
    want is an ordered set, OrderedSets as a class aren't introduced until
    Python 3.0 or maybe 2.7 (not sure). Ideally this library would be
    compatible with Python versions at least as early as 2.6 and hopefully 2.4
    as well.
    """
    def __init__(self, points=None):
        # can be initialized with an empty set.
        # this set needs to contain tuples of point coords
        # and then extend and manage the use of that set
        if not points:
            self.pointList = []
            self.pointDict = {}
        else:
            # parse the points to create the pointList and pointDict
            # we want to be able to accept points as tuples, as lists, as
            # Point3D objects, and as Vector3D objects. I guess if I add them
            # as iterables, that would be the simplest.
            raise NotImplementedError

    @property
    def points(self):
        # go through the list and get each tuple as Point3D object
        return [Point3D(*point) for point in pointList]

    @points.setter
    def points(self, value):
        # reset the pointList and pointDict objects
        raise NotImplementedError





WorldX = Vector3D(1.0, 0.0, 0.0)
WorldY = Vector3D(0.0, 1.0, 0.0)
WorldZ = Vector3D(0.0, 0.0, 1.0)

