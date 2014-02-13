"""This module implements a plane object and related functions
"""
from line import Line3d
from vector3d import Vector3d
from point3d import Point3d
from core import isRoughlyZero

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

        self.d = -(self.normal.dot(self.point))


    def angleTo(self, other):
        """measures the angle between this plane and another plane. This uses
        that angle between two normal vectors.
        Units expressed in radians.
        """
        if isinstance(other, Plane3d):
            otherVect = other.normal
        elif isinstance(other, Vector3d):
            otherVect = other
        return self.normal.angleTo(otherVect)


    def intersect(self, other):
        """Finds the intersection of this plane with another object.
        """
        if isinstance(other, Plane3d):
            # return the line intersection of two planes
            # first, get the cross product of the two plane normals
            # which is a vector parallel to L
            vector = self.normal.cross(other.normal)
            absCoords = [abs(c) for c in vector]
            if isRoughlyZero(sum(absCoords)):
                # the planes are parallel and do not intersect
                return None
            else:
                # the planes intersect in a line
                # first find the largest coordinate in the vector
                cNum = None
                cMax = 0
                for i, c in enumerate(absCoords):
                    if c > cMax:
                        cMax = c
                        cNum = i
                dims = ["x","y","z"]
                biggestDim = dims.pop(cNum)
                p = {}
                p[biggestDim] = 0
                if biggestDim == "x":
                    p["y"] = (other.d * self.normal.z - self.d * other.normal.z)/vector.x
                    p["z"] = (self.d * other.normal.y - other.d * self.normal.y)/vector.x
                elif biggestDim == "y":
                    p["x"] = (self.d * other.normal.z - other.d * self.normal.z)/vector.y
                    p["z"] = (other.d * self.normal.x - self.d * other.normal.x)/vector.y
                else: # biggest dim is z
                    p["x"] = (other.d * self.normal.y - self.d * other.normal.y)/vector.z
                    p["y"] = (self.d * other.normal.x - other.d * self.normal.x)/vector.z
                point = Point3d(**p)
                return Line3d(vector, point)

        elif isinstance(other, Line3d):
            # return the point intersection of a line and a plane
            pass
        pass

    def __repr__(self):
        return 'Plane3d( %s, %s )' % (self.point, self.normal)

