"""This module implements a plane object and related functions
"""


from line import Line3d
from vector import Point3d, Vector3d

class Plane3d(object):
    """A 3d plane object
    This plane class has an infinite size.

    A plane can be initialized with point on the plane and a vector normal to
    the plane, or with three points

    Planes are infinite and currently have no origin.
    """
    def __init__(self, *args, **kwargs):

        if len(args) == 2:
            # assume we have a point and vector
            self.point = args[0]
            self.normal = args[1]

        elif len(args) == 3:
            # assume we have 3 points
            v1 = args[2] - args[1]
            v2 = args[1] - args[0]
            normal = v1.cross( v2 )
            self.point = args[0]
            self.normal = normal


    def angleTo(self, other):
        """measures the angle between this plane and another plane. Units
        expressed in radians.
        """
        pass


    def intersect(self, other):
        """Finds the intersection of this plane with another object.
        """
        if isinstance(other, Plane3d):
            # return the line intersection of two planes
            pass
        elif isinstance(other, Line3d):
            # return the point intersection of a line and a plane
            pass
        pass

    def __repr__(self):
        return 'Plane3d( %s, %s )' % (self.point, self.normal)
