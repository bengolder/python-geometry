"""This module is for the Vector class"""

import math
import numbers

from core import isRoughlyZero


class Vector3d(object):
    """A 3d vector object

    """
    def __init__(self, x=0.0, y=0.0, z=0.0):
        # coords is the essence of the data structure. It's immutable and
        # iterable, allowing us to iterate over the values as well as providing
        # a little bit of protection from accidentally changing the values see
        # `classTest` in tests to understand more of the reasoning here.
        self.coords = (x, y, z)

    @property
    def x(self):
        return self[0]
    @x.setter
    def x(self, value):
        self.coords = (value, self.y, self.z)

    @property
    def y(self):
        return self[1]
    @y.setter
    def y(self, value):
        self.coords = (self.x, value, self.z)

    @property
    def z(self):
        return self[2]
    @z.setter
    def z(self, value):
        self.coords = (self.x, self.y, value)

    @property
    def length(self):
        """get the vector length / amplitude
            >>> v = Vector3d(0.0, 2.0, 1.0)
            >>> v.length
            2.2360679774997898
        """
        # only calculate the length if asked to.
        return math.sqrt(sum(n**2 for n in self))

    def toLength(self, number):
        """Get a parallel vector with the input amplitude."""
        # depends on normalized() and __mul__
        # create a vector as long as the number
        return self.normalized() * number

    def toX(self, number):
        """For getting a copy of the same vector but with a new x value"""
        return Vector3d(number, self[1], self[2])

    def toY(self, number):
        """For getting a copy of the same vector but with a new y value"""
        return Vector3d(self[0], number, self[2])

    def toZ(self, number):
        """For getting a copy of the same vector but with a new z value"""
        return Vector3d(self[0], self[1], number)

    def normalized(self):
        """just returns the normalized version of self without editing self in
        place.
            >>> v.normalized()
            Vector3d(0.0, 0.894427191, 0.4472135955)
            >>> v
            Vector3d(0.0, 3.2995419076, 1.6497709538)
        """
        # think how important float accuracy is here!
        if isRoughlyZero(sum(n**2 for n in self)):
            raise ZeroDivisionError
        else:
            return self * (1 / self.length)

    def asList(self):
        """return vector as a list"""
        return [c for c in self]

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

    def __iter__(self):
        """For iterating, the vectors coordinates are represented as a tuple."""
        return self.coords.__iter__()

    ## Time for some math

    def dot(self, other):
        """Gets the dot product of this vector and another.
            >>> v
            Vector3d(5, 1.20747670785, 60.0)
            >>> v1
            Vector3d(0.0, 2.0, 1.0)
            >>> v1.dot(v)
            62.41495341569977
        """
        return sum((p[0] * p[1]) for p in zip(self, other))

    def cross(self, other):
        """Gets the cross product between two vectors
            >>> v
            Vector3d(5, 1.20747670785, 60.0)
            >>> v1
            Vector3d(0.0, 2.0, 1.0)
            >>> v1.cross(v)
            Vector3d(118.792523292, 5.0, -10.0)
        """
        # I hope I did this right
        x = (self[1] * other[2]) - (self[2] * other[1])
        y = (self[2] * other[0]) - (self[0] * other[2])
        z = (self[0] * other[1]) - (self[1] * other[0])
        return Vector3d(x, y, z)

    def __add__(self, other):
        """we want to add single numbers as a way of changing the length of the
        vector, while it would be nice to be able to do vector addition with
        other vectors.
            >>> from core import Vector3d
            >>> # test add
            ... v = Vector3d(0.0, 1.0, 2.0)
            >>> v1 = v + 1
            >>> v1
            Vector3d(0.0, 1.4472135955, 2.894427191)
            >>> v1.length - v.length
            0.99999999999999956
            >>> v1 + v
            Vector3d(0.0, 2.4472135955, 4.894427191)
        """
        if isinstance(other, numbers.Number):
            # then add to the length of the vector
            # multiply the number by the normalized self, and then
            # add the multiplied vector to self
            return self.normalized() * other + self

        elif isinstance(other, Vector3d):
            # add all the coordinates together
            # there are probably more efficient ways to do this
            return Vector3d(*(sum(p) for p in zip(self, other)))
        else:
            raise NotImplementedError

    def __sub__(self, other):
        """Subtract a vector or number
            >>> v2 = Vector3d(-4.0, 1.2, 3.5)
            >>> v1 = Vector3d(2.0, 1.1, 0.0)
            >>> v2 - v1
            Vector3d(-6.0, 0.1, 3.5)
        """
        return self.__add__(other * -1)

    def __mul__(self, other):
        """if with a number, then scalar multiplication of the vector,
            if with a Vector, then dot product, I guess for now, because
            the asterisk looks more like a dot than an X.
            >>> v2 = Vector3d(-4.0, 1.2, 3.5)
            >>> v1 = Vector3d(2.0, 1.1, 0.0)
            >>> v2 * 1.25
            Vector3d(-5.0, 1.5, 4.375)
            >>> v2 * v1 #dot product
            -6.6799999999999997
        """
        if isinstance(other, numbers.Number):
            # scalar multiplication for numbers
            return Vector3d( *((n * other) for n in self))

        elif isinstance(other, Vector3d):
            # dot product for other vectors
            return self.dot(other)

    def __hash__(self):
        """This method provides a hashing value that is the same hashing value
        returned by the vector's coordinate tuple. This allows for testing for
        equality between vectors and tuples, as well as between vectors.

        Two vector instances (a and b) with the same coordinates would return True
        when compared for equality: a == b, a behavior that I would love to
        have, and which would seem very intuitive.

        They would also return true when compared for equality with a tuple
        equivalent to their coordinates. My hope is that this will greatly aid
        in filtering duplicate points where necessary - something I presume
        many geometry algorithms will need to look out for.

        I'm not sure it is a bad idea, but I intend this class to basically be a
        tuple of floats wrapped with additional functionality.
        """
        return self.coords.__hash__()

    def __eq__(self, other):
        """I am allowing these to compared to tuples, and to say that yes, they
        are equal. the idea here is that a Vector3d _is_ a tuple of floats, but
        with some extra methods.
        """
        return self.coords.__eq__(other)

    def __repr__(self):
        return 'Vector3d(%s, %s, %s)' % self.coords



class Point3d(Vector3d):
    """Works like a Vector3d. I might add some point specific methods.
    """
    def __init__(self, *args, **kwargs):
        super(Point3d, self).__init__(*args, **kwargs)

    def __repr__(self):
        return 'Point3d(%s, %s, %s)' % self.coords

    def distanceTo(self, other):
        """Find the distance between this point and another.
            >>> p1 = Point3d(-2.2, -0.5, 0.0034)
            >>> p2 = Point3d(3.45, 0.01, -2004.665)
            >>> p1.distanceTo(p2)
            2004.676426897508
        """
        return (other - self).length

    def vectorTo(self, other):
        """Find the vector to another point.
            >>> p1 = Point3d(-2.2, -0.5, 0.0034)
            >>> p2 = Point3d(3.45, 0.01, -2004.665)
            >>> p1.distanceTo(p2)
            2004.676426897508
            >>> p1.distanceTo(p2)
            2004.676426897508
            >>> p2.vectorTo(p1)
            Vector3d(-5.65, -0.51, 2004.6684)
            >>> p1 - p2
            Vector3d(-5.65, -0.51, 2004.6684)
        """
        return other - self




class PointSet(object):
    """This class is meant to hold a set of *unique* points.
    It enforces this using python's built in `set` type. But points may still
    be within some tolerance of each other.

    This doesn't yet exclude matching points

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
        # intialize the dictionary and list first
        # becasue any input points will be placed there to start
        self.pointList = []
        self.pointDict = {}
        if points:
            # parse the points to create the pointList and pointDict
            # we want to be able to accept points as tuples, as lists, as
            # Point3d objects, and as Vector3d objects. I guess if I add them
            # as iterables, that would be the simplest.
            self.points = points

    @property
    def points(self):
        # go through the list and get each tuple as Point3d object
        return [Point3d(*c) for c in self.pointList]

    @points.setter
    def points(self, values):
        """This method parses incoming values being used to define points and
        filters them if necessary.

        This creates an internal PointList and PointDict, which together mimick
        the OrderedDict in Python 3.0. I'm combining these two pieces for backwards
        compatibility.
        """
        for i, val in enumerate(values):
            # Vector3ds will need to be unwrapped
            if isinstance(val, Vector3d):
                point = Point3d(*val)
            else:
                # just assume it is some sort of iterable
                point = Point3d(*(val[v] for v in range(3)))
            # here will build the dictionary, using indices as the only
            # value any given tuple refers to
            self.pointDict[point] = i
            # and here we also build up a list, for lookups by index
            self.pointList.append(point)

    def __getitem__(self, key):
        """This builds a dictionary / list-like api on the PointSet.
        The `key` might be an integer or a coordinate tuple, or a point.

        There is a design question here: should it initialize the object as a
        Point3d?

        An if Point3ds are already hashable, why am I using simple tuples when
        I could use Point3ds?
        """
        # if it's a tuple or point3d and return the index
        if isinstance(key, tuple) or isinstance(key, Vector3d):
            return self.pointDict[key]
        else:
            # assume it is an index or slice
            return self.pointList[key]

    def __iter__(self):
        """Uses the internal list for iteration"""
        return self.pointList.__iter__()

    def __len__(self):
        """returns the number of Points it has."""
        return self.pointList.__len__()

    def __contains__(self, other):
        """checks to see if this set has an item that matches other
            other in self
        """
        return self.pointDict.__contains__(other)

    def issubset(self, other):
        """Used to see if all the items of an iterable are contained in this
        pointSet.
            self <= other
        """
        for n in other:
            if n not in self:
                return False
        return True

    def __le__(self, other):
        return self.issubset(other)

    def issuperset(self, other):
        """Used to see of all of the items in this object are contained in an
        other object.
            self >= other
        """
        for n in self:
            if n not in other:
                return False
        return True
    def __ge__(self, other):
        return self.issuperset(other)

    def union(self, other):
        """returns a new PointSet with the points from self and the points from
        other.
        self | other
        """
        newList = []
        for p in self:
            newList.append(p)
        for p in other:
            newList.append(p)
        return PointSet(newList)
    def __or__(self, other):
        return self.union(other)

    def intersection(self, other):
        """returns the set intersection between self and other
            self & other
        """
        newList = []
        for p in other:
            if p in self:
                newList.append(p)
        return PointSet(newList)
    def __and__(self, other):
        return self.intersection(other)

    def difference(self, other):
        """
            self - other
        """
        newList = []
        for p in self:
            if p not in other:
                newList.append(p)
        return PointSet(newList)
    def __sub__(self, other):
        return self.difference(other)

    def symmetric_difference(self, other):
        """ Returns all the points in self and other that are not in the
            intersection of self and other.
            self ^ other
        """
        newList = []
        for p in self:
            if p not in other:
                newList.append(p)
        for p in other:
            if p not in self:
                newList.append(p)
        return PointSet(newList)
    def __xor__(self, other):
        return self.symmetric_difference(other)

    def copy(self):
        """ returns a shallow copy of this pointset
        """
        newList = []
        for p in self:
            newList.append(p)
        return PointSet(newList)

    def extend(self, other):
        """Adds an iterable of new points to the set.
        """
        length = len(self)
        for i, p in enumerate(other):
            self.pointList.append(p)
            self.pointDict[p] = i + length
    def __ior__(self, other):
        return self.extend(other)

    def append(self, other):
        """Adds a new point to the set.
        """
        length = len(self)
        self.pointList.append(other)
        self.pointDict[other] = length


WorldX = Vector3d(1.0, 0.0, 0.0)
WorldY = Vector3d(0.0, 1.0, 0.0)
WorldZ = Vector3d(0.0, 0.0, 1.0)



