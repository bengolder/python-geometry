from point3d import Point3d

class PointSet(object):
    """This class is meant to hold a set of *unique* points.

    Basically this provides hooks to using a python 'set' containing tuples of
    the point coordinates.
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
        return self.pointList

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

